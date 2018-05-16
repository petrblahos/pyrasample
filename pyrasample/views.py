from pyramid.view import view_config
from pyramid.httpexceptions import (
    HTTPFound,
)


@view_config(context="pyrasample.resources.TopContext",
             renderer="templates/named_view.mako",
             name="namedview")
def named_view_in_root(request):
    return {}


@view_config(context="pyrasample.resources.TopContext",
             renderer="templates/home.mako")
def home(context, request):
    return {}


@view_config(context="pyrasample.resources.DBContext", renderer="templates/dbtable.mako")
def dbtable(request):
    return {}


@view_config(context="pyrasample.resources.DBContext", name="next")
def dbitem_next(context, request):
    context.page = context.page + 1
    return HTTPFound(location=request.resource_url(context))


@view_config(context="pyrasample.resources.DBContext", name="prev")
def dbitem_prev(context, request):
    context.page = max((context.page - 1, 0))
    return HTTPFound(location=request.resource_url(context))


@view_config(context="pyrasample.resources.ItemContext", renderer="templates/dbitem.mako")
def dbitem(request):
    return {}
