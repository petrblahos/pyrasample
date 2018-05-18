"""
system["context"] is supposed to be a sqlalchemy table metadata.
Returns the header - a list of column names and table rows from
the query as defined by context.get_query()
"""

def get_header(system, value):
    return [str(col) for col in system["context"].model.columns]


def iterate_rows(system, value):
    request = system["request"]
    context = system["context"]
    for row in request.db.execute(context.get_query()):
        yield [row[col.name] for col in context.model.columns]
