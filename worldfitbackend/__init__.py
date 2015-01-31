from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import initialize_sql

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)

    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('home', '/')

    config.add_route('user_list', '/users', request_method="GET")
    config.add_route('user_new', '/users', request_method="POST")
    config.add_route('user_show', '/users/{hash}', request_method="GET")

    config.scan()

    return config.make_wsgi_app()
