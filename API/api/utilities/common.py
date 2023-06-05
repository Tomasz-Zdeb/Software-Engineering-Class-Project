def remove_dict_fields(dict, fields):
    for field in fields:
        if field in dict:
            del dict[field]
    return dict
