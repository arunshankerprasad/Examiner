import os, sys

# First set the path for external libs
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'),)

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'hellodjango')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'examiner.settings'


import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

