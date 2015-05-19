# -*- coding: utf-8 -*-
from pyramid.view import view_config

class Worldfit:

    def __init__(self, request):
        self._request = request

    @view_config(route_name='Worldfit', renderer='json')
    def list(self):
        return {'project': 'worldfit'}
