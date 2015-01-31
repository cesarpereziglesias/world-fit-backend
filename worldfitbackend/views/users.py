import transaction

from datetime import datetime

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPInternalServerError, HTTPBadRequest, HTTPFound

from worldfitbackend.models import DBSession, User, Activity

class Users:

    def __init__(self, request):
        self.request = request

    @view_config(route_name='user_list', renderer='json')
    def list(self):
        return [user.to_dict() for user in DBSession.query(User).all()]

    @view_config(route_name='user_new', renderer='json')
    def new(self):
        request = self.request.json_body
        user_hash = User.create_hash(request['email'])
        user = User.get_by_hash(user_hash)
        if user is None:
            with transaction.manager:
                user = User(**request)
                DBSession.add(user)

        # FIXME: It's more cool if we use user instance. Here, we're out
        # of the session. Study the way
        return user_hash

    @view_config(route_name='user_show', renderer='json')
    def show(self):
        user = User.get_by_hash(self.request.matchdict.get('hash', None))
        if user is None:
            return HTTPNotFound()
        return user.to_dict()

    @view_config(route_name='user_activities_register', renderer='json')
    def activities_register(self):
        user = User.get_by_hash(self.request.matchdict.get('hash', None))
        if user is None:
            return HTTPNotFound()

        activity_type = self.request.matchdict.get('type', None)
        if activity_type not in Activity.TYPES:
            return HTTPBadRequest()

        activities = self.request.json_body
        with transaction.manager:
            for activity_data in activities:
                activity_date = datetime.strptime(activity_data["date"], "%Y/%m/%d")
                activity = DBSession.query(Activity).filter_by(user=user, date=activity_date).first()
                if activity is None:
                    activity = Activity()
                    activity.activity_type = activity_type
                    activity.date = activity_date
                    activity.user = user

                activity.value = activity_data["value"]

                DBSession.add(activity)

        return "OK"
