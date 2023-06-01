from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restx import Resource, reqparse

from api import api
from api.utilities.notes import get_all_notes_of_user
from api.utilities.common import remove_dict_fields
from api.utilities.catalog import get_catalog_name_by_id

get_parser = reqparse.RequestParser()
get_parser.add_argument('Authorization', type=str,
                        required=True, help='Bearer token', location='headers')


@api.route('/notes')
@api.doc(description='Endpoint for getting all notes of a user.')
class Notes(Resource):
    @api.expect(get_parser)
    @api.doc(description='Get all notes of a user.')
    @api.response(200, 'Success')
    @api.response(400, 'Bad Request')
    @api.response(401, 'Unauthorized')
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        notes = get_all_notes_of_user(user_id)

        uncataloged = [remove_dict_fields(note.to_dict(), ['body', 'catalog_id'])
                       for note in notes if note.catalog_id is None]
        catalogs = []

        # This is not the most readable solution due to all of the list comprehensions,
        # but all it does is check if the note has a catalog_id, and if it does,
        # it checks if the catalog_id is already in the list of catalogs. If it isn't,
        # it adds it to the list of catalogs along with all of the notes which have the
        # same catalog_id.

        for note in notes:
            catalog_id = note.catalog_id
            if catalog_id is not None and \
                    catalog_id not in [catalog['catalog_id'] for catalog in catalogs]:
                catalogs.append(
                    {
                        'catalog_name': get_catalog_name_by_id(catalog_id),
                        'catalog_id': catalog_id,
                        'notes': [remove_dict_fields(note.to_dict(),
                                                     ['body', 'catalog_id'])
                                  for note in notes
                                  if note.catalog_id == catalog_id and note.catalog_id]
                    }
                )

        return {
            'uncataloged': uncataloged,
            'catalogs': catalogs
        }, 200
