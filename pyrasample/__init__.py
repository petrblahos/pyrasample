from pyramid.config import Configurator

from pyrasample.resources import TopContext


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings, root_factory=TopContext)
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.include('pyramid_mako')      # runs pyramid_mako.includeme
    config.include('pyrasample.model')  # runs pyrasample.model.includeme
    config.add_renderer(".xlsx", "pyrasample.xlsxrenderer.XLSXRenderer")

    config.scan()

    return config.make_wsgi_app()
