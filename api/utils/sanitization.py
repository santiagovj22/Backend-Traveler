def sanitize_pagination(page, limit):
    if limit < 1 or limit > 10:
        limit = 10
    if page < 1:
        page = 1
    skip = (page - 1) * limit
    return page, limit, skip
