from datetime import datetime

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings

from models import Questionaire
from examiner.decorators import login_required, must_be_one_of_these_users


@must_be_one_of_these_users(settings.TEACHERS)
@login_required
def welcome_view(request):
    """ Simple Hello World View """
    c = {
        'current_time': datetime.now(),
        'questionaire': Questionaire.query().get()
    }
    return render_to_response('welcome.html', c, context_instance=RequestContext(request))
