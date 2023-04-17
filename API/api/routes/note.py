
from time import strftime

from flask_restx import Resource, reqparse

from api import api
from api.models.note import NoteModel
from api.models.user_note import UserNoteModel
from api.utilities import note as note_util
from api.utilities import user_note as user_note_util
from api.utilities.db_utils import (check_if_catalog_exists,
                                    check_if_user_exists)

#
#   Parsers
#

# Get parser
get_parser = reqparse.RequestParser()
get_parser.add_argument('note_id', type=int, required=True, help='Note ID')

# Post parser
post_parser = reqparse.RequestParser()
post_parser.add_argument('user_id', type=int, required=True, help='User ID')
post_parser.add_argument(
    'title', type=str, help='Note title', default='Untitled')
post_parser.add_argument('catalog_id', type=int,
                         help='Catalog ID', default=None)
post_parser.add_argument('description', type=str,
                         help='Note description', default=None)
post_parser.add_argument('body', type=str, help='Note body', default=None)

# Put parser
put_parser = reqparse.RequestParser()
put_parser.add_argument('note_id', type=int, required=True, help='Note ID')
put_parser.add_argument(
    'title', type=str, help='Note title')
put_parser.add_argument('catalog_id', type=int,
                        help='Catalog ID')
put_parser.add_argument('description', type=str,
                        help='Note description')
put_parser.add_argument('body', type=str, help='Note body')

# Delete parser
delete_parser = reqparse.RequestParser()
delete_parser.add_argument('note_id', type=int, required=True, help='Note ID')


@api.route('/note')
@api.doc(description='Main note endpoint. Used for creating, updating, and deleting single notes.')
class Note(Resource):
    @api.expect(get_parser)
    @api.doc(description='Gets a note by its ID.')
    @api.doc(responses={404: 'Note not found.', 200: 'Success.'})
    def get(self):
        args = get_parser.parse_args()
        note_id = args['note_id']

        if not note_util.check_if_note_exists(note_id):
            return {"message": "Note not found."}, 404

        note = note_util.get_note_by_id(note_id)

        note_dict = note.to_dict()

        return note_dict, 200

    @api.expect(post_parser)
    @api.doc(description='Creates a note and its associated user_note.')
    @api.doc(responses={404: 'User or catalog not found.', 400: 'Bad request.', 201: 'Success.'})
    def post(self):
        args = post_parser.parse_args()

        if check_if_user_exists(args['user_id']) is False:
            return {"message": "User not found."}, 404
        elif args['catalog_id'] is not None and check_if_catalog_exists(args['catalog_id']) is False:
            return {"message": "Catalog not found."}, 404

        note = NoteModel(
            catalog_id=args['catalog_id'],
            title=args['title'],
            description=args['description'],
            body=args['body'],
            created_date=strftime("%Y-%m-%d %H:%M:%S"),
            updated_date=strftime("%Y-%m-%d %H:%M:%S")
        )

        note_id = note.save()

        user_note = UserNoteModel(
            user_id=args['user_id'],
            note_id=note_id
        )

        user_note.save()

        return {"note_id": note_id}, 201

    @api.expect(put_parser)
    @api.doc(description='Updates a note.')
    @api.doc(responses={404: 'Note or catalog not found.', 400: 'Bad request.', 200: 'Success.'})
    def put(self):
        args = put_parser.parse_args()
        args = {k: v for k, v in args.items() if v is not None}

        if len(args) == 1:
            return {"message": "No data to update."}, 400

        if not note_util.check_if_note_exists(args['note_id']):
            return {"message": "Note not found."}, 404

        if 'catalog_id' in args and not check_if_catalog_exists(args['catalog_id']):
            return {"message": "Catalog not found."}, 404

        note = note_util.get_note_by_id(args['note_id'])

        modified_note_fields = {k: v for k,
                                v in args.items() if k != 'note_id'}

        note.update(modified_note_fields)

        return {"message": "Note updated."}, 200

    @api.expect(delete_parser)
    @api.doc(description='Deletes a note and its associated user_note.')
    @api.doc(responses={404: 'Note not found.', 200: 'Success.'})
    def delete(self):
        args = delete_parser.parse_args()
        note_id = args['note_id']

        if not note_util.check_if_note_exists(note_id):
            return {"message": "Note not found."}, 404

        note = note_util.get_note_by_id(note_id)
        user_note = user_note_util.get_user_note_by_note_id(note_id)

        user_note.delete()
        note.delete()

        return {"message": "Note deleted."}, 200
