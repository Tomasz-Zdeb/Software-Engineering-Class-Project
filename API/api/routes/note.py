
from time import strftime

from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restx import Resource, reqparse

from api import api
from api.models.note import NoteModel
from api.models.user_note import UserNoteModel
from api.models.tag import NoteTagModel, TagModel
from api.utilities import note as note_util
from api.utilities import user_note as user_note_util
from api.utilities.db_utils import (check_if_catalog_exists,
                                    check_if_user_exists)
from api.utilities.auth import user_has_permission

#
#   Parsers
#

# Get parser
get_parser = reqparse.RequestParser()
get_parser.add_argument('note_id', type=int, required=True, help='Note ID')
get_parser.add_argument('Authorization', type=str,
                        required=True, help='Bearer token', location='headers')

# Post parser
post_parser = reqparse.RequestParser()
post_parser.add_argument(
    'title', type=str, help='Note title', default='Untitled')
post_parser.add_argument('catalog_id', type=int,
                         help='Catalog ID', default=None)
post_parser.add_argument('description', type=str,
                         help='Note description', default=None)
post_parser.add_argument('body', type=str, help='Note body', default=None)
post_parser.add_argument('Authorization', type=str,
                         required=True, help='Bearer token', location='headers')

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
put_parser.add_argument('Authorization', type=str,
                        required=True, help='Bearer token', location='headers')

# Delete parser
delete_parser = reqparse.RequestParser()
delete_parser.add_argument('note_id', type=int, required=True, help='Note ID')
delete_parser.add_argument('Authorization', type=str,
                           required=True, help='Bearer token', location='headers')


@api.route('/note')
@api.doc(description='Main note endpoint. Used for creating, updating, and deleting single notes.')  # noqa
class Note(Resource):
    @api.expect(get_parser)
    @api.doc(description='Gets a note by its ID.')
    @api.doc(responses={404: 'Note not found.',
                        200: 'Success.',
                        401: 'Unauthorized.',
                        422: 'Invalid token.',
                        403: 'Forbidden.'})
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()

        args = get_parser.parse_args()
        note_id = args['note_id']

        # The error messages should be more vague and shouldn't reveal if
        # the note or user exists. However for our purposes this is fine, as
        # it helps with debugging.

        if not note_util.check_if_note_exists(note_id):
            return {"message": "Note not found."}, 404

        if not user_has_permission(user_id, note_id):
            return {"message": "Forbidden."}, 403

        note = note_util.get_note_by_id(note_id)

        note_dict = note.to_dict()

        # Get the tags associated with this note
        note_tags = NoteTagModel.query.filter_by(note_id=note.note_id).all()

        # Get the TagModel for each NoteTagModel and convert to a list of dictionaries
        note_dict["tags"] = [{"tag_id": note_tag.tag_id, "tag_name": TagModel.query.get(
            note_tag.tag_id).name} for note_tag in note_tags]

        return note_dict, 200

    @api.expect(post_parser)
    @api.doc(description='Creates a note and its associated user_note.')
    @api.doc(responses={404: 'User or catalog not found.',
                        400: 'Bad request.',
                        201: 'Success.',
                        401: 'Unauthorized.',
                        422: 'Invalid token.'})
    @jwt_required()
    def post(self):
        args = post_parser.parse_args()
        user_id = get_jwt_identity()

        if check_if_user_exists(user_id) is False:
            return {"message": "User not found."}, 404
        elif (args['catalog_id'] is not None and
              check_if_catalog_exists(args['catalog_id']) is False):
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
            user_id=user_id,
            note_id=note_id
        )

        user_note.save()

        return {"note_id": note_id}, 201

    @api.expect(put_parser)
    @api.doc(description='Updates a note.')
    @api.doc(responses={404: 'Note or catalog not found.',
                        400: 'Bad request.',
                        200: 'Success.',
                        401: 'Unauthorized.',
                        422: 'Invalid token.',
                        403: 'Forbidden.'})
    @jwt_required()
    def put(self):
        args = put_parser.parse_args()
        args = {k: v for k, v in args.items() if v is not None}

        user_id = get_jwt_identity()

        if len(args) == 2 and 'note_id' in args and 'Authorization' in args:
            return {"message": "No data to update."}, 400

        if not note_util.check_if_note_exists(args['note_id']):
            return {"message": "Note not found."}, 404

        if 'catalog_id' in args and not check_if_catalog_exists(args['catalog_id']):
            return {"message": "Catalog not found."}, 404

        if not user_has_permission(user_id, args['note_id']):
            return {"message": "Forbidden."}, 403

        note = note_util.get_note_by_id(args['note_id'])

        modified_note_fields = {k: v for k,
                                v in args.items() if k != 'note_id'}

        note.update(modified_note_fields)

        return {"message": "Note updated."}, 200

    @api.expect(delete_parser)
    @api.doc(description='Deletes a note and its associated user_note.')
    @api.doc(responses={404: 'Note not found.',
                        200: 'Success.',
                        401: 'Unauthorized.',
                        422: 'Invalid token.',
                        403: 'Forbidden.'})
    @jwt_required()
    def delete(self):
        args = delete_parser.parse_args()
        note_id = args['note_id']
        user_id = get_jwt_identity()

        if not note_util.check_if_note_exists(note_id):
            return {"message": "Note not found."}, 404

        if not user_has_permission(user_id, note_id):
            return {"message": "Forbidden."}, 403

        note = note_util.get_note_by_id(note_id)
        user_note = user_note_util.get_user_note_by_note_id(note_id)

        user_note.delete()
        note.delete()

        return {"message": "Note deleted."}, 200
