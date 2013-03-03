from functools import wraps
from google.appengine.api import users
from django.shortcuts import redirect


def login_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not users.get_current_user():
            request = args[0]
            return redirect(users.create_login_url(request.path))
        return func(*args, **kwargs)
    return decorated_view


class must_be_one_of_these_users(object):

    def __init__(self, users):
        self.users = users

    def __call__(self, func):

        @wraps(func)
        def decorated_view(*args, **kwargs):
            import logging

            if users.get_current_user() and users.get_current_user().email().lower() not in map(str.lower, self.users):
                request = args[0]
                logging.info("Current user (%s) is not one of the permitted users (%s) for this URL (%s)." % (users.get_current_user().email(), self.users, request.path))
                return redirect('/answer')
            return func(*args, **kwargs)
        return decorated_view
