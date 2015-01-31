import transaction

from datetime import datetime

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPInternalServerError, HTTPBadRequest, HTTPFound

from worldfitbackend.models import DBSession, Challenge

class Challenges:

    def __init__(self, request):
        self.request = request


    @view_config(route_name='challenge_list', renderer='json')
    def list(self):
        return [challenge.to_dict() for challenge in DBSession.query(Challenge).all()]

    @view_config(route_name='challenge_new', renderer='json')
    def new(self):
        request = self.request.json_body
        with transaction.manager:
            challenge = Challenge()
            challenge.name = request['name']
            challenge.owner = request['owner']
            challenge.challenge_type = request['challenge_type']
            challenge.init = datetime.strptime(request["init"], "%Y/%m/%d")
            challenge.end = datetime.strptime(request["end"], "%Y/%m/%d")

            DBSession.add(challenge)

        return "OK"
