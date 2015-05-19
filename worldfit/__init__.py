# -*- coding: utf-8 -*-
from pyramid.config import Configurator

from sqlalchemy import engine_from_config

from .models import initialize_sql

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)

    config = Configurator(settings=settings)

    config.add_route('Worldfit', '/')

    config.scan()

    return config.make_wsgi_app()
