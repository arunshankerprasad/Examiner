import logging

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.simplejson import dumps, loads

from google.appengine.ext import ndb
from google.appengine.api import users

from forms import AnswerForm
from models import Answer
from examiner.decorators import login_required


@login_required
@csrf_exempt
def answers_save(request):

    r = {'errors': []}
    is_success = True
    counter = 0
    answer_forms = []

    forms = loads(request.body)
    for form in forms:
        form = AnswerForm(data=form)
        answer_forms.append(form)
        if not form.is_valid():
            is_success = False
            r['errors'].append({'form': 'form_%s' % counter, 'errors': form.errors})

        r['is_success'] = is_success
        if is_success:
            answers = []
            for form in answer_forms:
                answers.append(Answer(text=form.cleaned_data.get('text'), question=form.cleaned_data.get('question'), answered_by = users.get_current_user()))

            ndb.put_multi(answers)

        counter += 1

    return HttpResponse(dumps(r), mimetype='application/json')


@login_required
@csrf_exempt
def answer_evaluate(request):

    r = {'is_success': True}
    answer = loads(request.body)

    a = ndb.Key(urlsafe=answer['key']).get()
    a.is_correct = answer['is_correct']
    a.is_evaluated = True
    a.put()

    return HttpResponse(dumps(r), mimetype='application/json')
