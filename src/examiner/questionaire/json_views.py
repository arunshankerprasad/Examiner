import logging

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.simplejson import dumps, loads
from django.conf import settings

from google.appengine.ext import ndb

from models import Question, Questionaire
from forms import QuestionForm
from examiner.examination.models import Answer
from examiner.decorators import login_required, must_be_one_of_these_users


@must_be_one_of_these_users(settings.TEACHERS)
@login_required
@csrf_exempt
def questionaire_save(request):

    r = {'errors': []}
    is_success = True
    counter = 0
    question_forms = []

    forms = loads(request.body)
    for form in forms:
        form = QuestionForm(data=form)
        question_forms.append(form)
        if not form.is_valid():
            is_success = False
            r['errors'].append({'form': 'form_%s' % counter, 'errors': form.errors})

        r['is_success'] = is_success
        if is_success:
            questions = []
            for form in question_forms:
                questions.append(Question(text=form.cleaned_data.get('text'), help_text=form.cleaned_data.get('help_text')))

        counter += 1

    Questionaire(questions=ndb.put_multi(questions)).put()

    return HttpResponse(dumps(r), mimetype='application/json')


@must_be_one_of_these_users(['arunshankerprasad@gmail.com', 'test@example.com'])
@login_required
def questionaire_responses(request):
    r = []
    answers = Answer.query()
    for answer in answers:
        r.append({
            'key': answer.key.urlsafe(),
            'question_text': answer.question.get().text,
            'text': answer.text,
            'answered_by': answer.answered_by.email(),
            'is_evaluated': answer.is_evaluated,
            'is_correct': answer.is_correct
        })
    return HttpResponse(dumps(r), mimetype='application/json')
