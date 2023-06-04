from flask import request
from flask_restx import Resource, reqparse
from api.models.tag import TagModel, TagService, NoteTagModel
from api.utilities.auth import user_has_permission
from api.utilities.note import check_if_note_exists
from api import api
from flask_jwt_extended import get_jwt_identity, jwt_required
from ..utilities.tag import owns_note

# Parsers
post_parser = reqparse.RequestParser()
post_parser.add_argument('note_id', type=int, required=True, help='Note ID')
post_parser.add_argument('tag_name', type=str, required=True, help='Tag name')
post_parser.add_argument('Authorization', type=str, required=True, help='Bearer token', location='headers')

get_parser = reqparse.RequestParser()
get_parser.add_argument('note_id', type=int, required=True, help='Note ID')
get_parser.add_argument('Authorization', type=str, required=True, help='Bearer token', location='headers')

delete_parser = reqparse.RequestParser()
delete_parser.add_argument('tag_id', type=int, required=True, help='Tag ID')
delete_parser.add_argument('Authorization', type=str, required=True, help='Bearer token', location='headers')

put_parser = reqparse.RequestParser()
put_parser.add_argument('tag_id', type=int, required=True, help='Tag ID')
put_parser.add_argument('tag_name', type=str, required=True, help='Tag name')
put_parser.add_argument('Authorization', type=str, required=True, help='Bearer token', location='headers')


@api.route("/note/tags")
@api.doc(description='Endpoint for creating, updating, deleting and fetching tags for a note.')
class Tag(Resource):

    @api.expect(post_parser)
    @api.doc(description='Creates a new tag for a specific note.')
    @api.doc(responses={400: 'Invalid request.',
                        404: 'Note not found.',
                        403: 'Forbidden.',
                        201: 'Tag successfully created.'})
    @jwt_required()
    def post(self):
        """
        Creates a new tag for a specific note.
        """
        args = post_parser.parse_args()
        note_id = args['note_id']
        tag_name = args['tag_name']

        if not note_id or not tag_name:
            return {"message": "Invalid request body. Ensure that note_id and tag_name are present and in the correct format."}, 400

        if not check_if_note_exists(note_id):
            return {"message": f"Note with ID {note_id} not found."}, 404

        current_user = get_jwt_identity() 
        if not user_has_permission(current_user, note_id):
            return {"message": "You do not have permission to create tags for this note."}, 403
        
        existing_tag = TagService.get_existing_tag(note_id, tag_name)
        if existing_tag:
            return {"message": f"Tag '{tag_name}' already exists for note {note_id}"}, 400

        try:
            new_tag = TagService.create_tag(note_id, tag_name)
        except:
            return {"message": "An error occurred while creating the tag. Please try again."}, 500

        return {"message": f"Tag '{tag_name}' has been successfully created.", "tag_id": new_tag.tag_id}, 201

    @api.expect(get_parser)
    @api.doc(description='Retrieves a list of tags associated with a specific note ID')
    @api.doc(responses={400: 'Invalid request.',
                        404: 'Note not found.',
                        403: 'Forbidden.',
                        200: 'Success.'})
    @jwt_required()
    def get(self):
        """
        Retrieves a list of tags associated with a specific note ID
        """
        current_user = get_jwt_identity()
        args = get_parser.parse_args()
        note_id = args.get('note_id')

        if not note_id:
            return {"message": "Invalid request. Ensure that note_id is present and in the correct format."}, 400

        if not check_if_note_exists(note_id):
            return {"message": f"Note with ID {note_id} not found."}, 404

        if not user_has_permission(current_user, note_id):
            return {"message": "You do not have permission to view tags for this note."}, 403

        note_tags = NoteTagModel.query.filter_by(note_id=note_id).all()

        if not note_tags:
            return {"message": f"No tags found associated with note ID {note_id}."}, 404

        tags = [TagModel.query.get(note_tag.tag_id) for note_tag in note_tags]

        if not tags:
            return {"message": "No tags found for this note."}, 404

        return {"tags": [tag.to_dict() for tag in tags]}, 200


    @api.expect(delete_parser)
    @api.doc(description='Deletes a tag of a specific ID for a note.')
    @api.doc(responses={400: 'Invalid request.',
                        404: 'Tag not found.',
                        403: 'Forbidden.',
                        200: 'Tag successfully deleted.'})
    @jwt_required()
    def delete(self):
        """
        Deletes a tag of a specific ID for a note.
        """
        args = delete_parser.parse_args()
        tag_id = args['tag_id']

        if not tag_id:
            return {"message": "Invalid request body. Ensure that tag_id is present and in the correct format."}, 400

        tag = TagModel.query.get(tag_id)

        if not tag:
            return {"message": f"Tag with ID {tag_id} not found."}, 404

        note_tag = NoteTagModel.query.filter_by(tag_id=tag.tag_id).first()
        if not note_tag:
            return {"message": f"No note found associated with tag ID {tag_id}."}, 404

        current_user = get_jwt_identity()
        if not user_has_permission(current_user, note_tag.note_id):
            return {"message": "You do not have permission to delete tags for this note."}, 403

        note_tag.delete()
        
        remaining_associations = NoteTagModel.query.filter_by(tag_id=tag.tag_id).first()
        if not remaining_associations:
            tag.delete()

        return {"message": f"Tag with ID {tag_id} has been successfully deleted."}, 200


    @api.expect(put_parser)
    @api.doc(description='Updates a tag of a specific ID for a note.')
    @api.doc(responses={400: 'Invalid request.',
                        404: 'Tag not found.',
                        403: 'Forbidden.',
                        200: 'Tag successfully updated.'})
    @jwt_required()
    def put(self):
        """
        Updates a tag of a specific ID for a note.
        """
        args = put_parser.parse_args()
        tag_id = args['tag_id']
        tag_name = args['tag_name']

        if not tag_id or not tag_name:
            return {"message": "Invalid request body."}, 400

        tag = TagModel.query.get(tag_id)
        if not tag:
            return {"message": f"Tag with ID {tag_id} not found."}, 404

        note_tag = NoteTagModel.query.filter_by(tag_id=tag.tag_id).first()
        if not note_tag:
            return {"message": f"No note found associated with tag ID {tag_id}."}, 404

        current_user = get_jwt_identity()
        if not user_has_permission(current_user, note_tag.note_id):
            return {"message": "You do not have permission to update this tag."}, 403

        tag.update(tag_name)

        return {"tag_id": note_tag.tag_id, "note_id": note_tag.note_id, "tag_name": tag.name}, 200
