from api.models.catalog import CatalogModel


def get_catalog_name_by_id(catalog_id):
    if catalog := CatalogModel.query.filter_by(catalog_id=catalog_id).first():
        return catalog.name
    else:
        return None


def get_catalog_id_by_name(catalog_name):
    if catalog := CatalogModel.query.filter_by(name=catalog_name).first():
        return catalog.catalog_id
    else:
        return None
