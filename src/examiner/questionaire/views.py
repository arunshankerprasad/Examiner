from datetime import datetime

from django.template import RequestContext
from django.shortcuts import render_to_response

def welcome_view(request):
    """ Simple Hello World View """
    c = {
        'current_time': datetime.now(),
    }
    return render_to_response('welcome.html', c, context_instance=RequestContext(request))
