import logging

from flask_restx import reqparse

from utils.parse_query import parse_query

LOG = logging.getLogger('Utils get_parser_data function')

def get_parser_data(get_services, field):
    parser = reqparse.RequestParser()
    search_arg, page_arg, limit_arg = parse_query(parser)
    if field is not None:
        collection, rows, page, limit = get_services(field, page_arg, limit_arg)
        return collection, rows, page, limit

    collection, rows, page, limit = get_services(search_arg, page_arg, limit_arg)
    return collection, rows, page, limit
