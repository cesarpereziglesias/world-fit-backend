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

    @view_config(route_name='challenge_show', renderer='json')
    def show(self):
        challenge = Challenge.get_by_id(self.request.matchdict.get('id', None))
        if challenge is None:
            return HTTPNotFound()

        response = challenge.to_dict()
        response['result'] = self._get_challenge_result(challenge)
        return response

    def _get_challenge_result(self, challenge):
        results = []
        for participant in challenge.participants:
            result = {}
            result["mail"] = participant.mail
            value = 0
            for activity in participant.activities:
                if activity.date <= challenge.end and activity.date >= challenge.init:
                    value = value + activity.value
            result["value"] = value
            results.append(result)

        return results
