"""
system["context"] is supposed to be a sqlalchemy table metadata.
We have no header this time.
Rows are pairs: Column name, value.
"""


def iterate_rows(system, value):
    context = system["context"]
    for (field, value) in context.item._asdict().items():
        yield (field, value)
