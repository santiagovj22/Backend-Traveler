def parse_query(parser):
    '''Parse args'''
    parser.add_argument('search')
    parser.add_argument('limit', type=int)
    parser.add_argument('page', type=int)
    args = parser.parse_args()

    search_arg = args['search']
    limit_arg = args['limit']
    page_arg = args['page']

    #default
    if limit_arg is None:
        limit_arg = 5

    if page_arg is None:
        page_arg = 1

    return search_arg, page_arg, limit_arg
