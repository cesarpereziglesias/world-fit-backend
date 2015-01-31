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

    config.add_route('user_activities', '/users/{hash}/activities', request_method="GET")
    config.add_route('user_activities_register', '/users/{hash}/activities', request_method="POST")


    config.add_route('challenge_list', '/challenges', request_method="GET")
    config.add_route('challenge_new', '/challenges', request_method="POST")
    config.add_route('challenge_show', '/challenges/{id}', request_method="GET")
    config.add_route('challenge_subscribe', '/challenges/{id}/subscribe', request_method="POST")

    config.scan()

    return config.make_wsgi_app()
