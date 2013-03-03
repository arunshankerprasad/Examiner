import os

from google.appengine.api import users


def media(request):
    # Sets the Build
    BUILD = 'PRODUCTION'
    if 'Dev' in os.getenv('SERVER_SOFTWARE'):
        BUILD = 'DEVELOPMENT'

    return {
        'BUILD': BUILD,
        'CURRENT_VERSION_ID': os.getenv('CURRENT_VERSION_ID'),  # Sets the CURRENT_VERSION_ID
        'user': users.get_current_user(),
        'logout_url': users.create_logout_url(request.path)
    }


def main(request):
    return {}
