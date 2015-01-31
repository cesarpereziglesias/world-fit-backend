from pyramid.view import view_config

class Main:

    def __init__(self, request):
        self.request = request

    @view_config(route_name='home', renderer='main/home.mako')
    def home(self):
        return {}
