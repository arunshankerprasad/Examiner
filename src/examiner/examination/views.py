from django.template import RequestContext
from django.shortcuts import render_to_response

from google.appengine.ext import ndb
from google.appengine.api import users

from examiner.questionaire.models import Questionaire
from examiner.decorators import login_required
from models import Answer


@login_required
def exam_welcome_view(request):
    """ Simple Hello World View """
    a = Answer.query(Answer.answered_by == users.get_current_user()).get()
    c = {
        'already_answered': a is not None
    }
    if not a:
        q = Questionaire.query().get()
        import logging
        logging.info(q.questions)
        c['questions'] = ndb.get_multi(q.questions) if q else []

    return render_to_response('examination.html', c, context_instance=RequestContext(request))
