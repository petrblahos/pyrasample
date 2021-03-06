from urllib.parse import parse_qs

from pyrasample.model.meta import metadata


class TopContext(object):
    """
    Just a plain python object, needs __name__, __parent__, __init__
    and __getitem__.

    """
    __name__ = ""
    __parent__ = None

    def __init__(self, request):
        self.request = request
        self.tables = metadata.tables

    def __getitem__(self, key):
        """
        Will raise KeyError if the key is not found.
        """
        return DBContext(self, key)


class DBContext(object):
    """
    Automatically paging objects. The schema is:
        tablename.page
    or just
        tablename
    for the first page.
    """
    ITEMS_PER_PAGE = 50

    def __init__(self, parent, name):
        self.request = parent.request
        self.__parent__ = parent
        if "." in name:
            (self.table_name, self.page) = name.split(".")
            self.page = int(self.page)
        else:
            self.table_name = name
            self.page = 0

        self.model = metadata.tables[self.table_name]

    def get_query(self):
        return self.model.select().limit(self.ITEMS_PER_PAGE).offset(
            self.page * self.ITEMS_PER_PAGE)

    def get_name(self):
        return "%s.%s" % (self.table_name, self.page)

    def __getitem__(self, name):
        """
        Returns the child context, by the primary key.
        """
        params = parse_qs(name)
        q = self.request.db.query(self.model)
        for pk in self.model.primary_key:
            q = q.filter(pk == params[pk.name][0])
        return ItemContext(self, name, q.one())

    __name__ = property(get_name)


class ItemContext(object):
    """
    The item is looked up within the parent (DBContext) context,
    using primary key.
    """
    def __init__(self, parent, name, item):
        self.request = parent.request
        self.__parent__ = parent
        self.__name__ = name
        self.item = item
