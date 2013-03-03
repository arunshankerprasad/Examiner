from django.conf.urls.defaults import patterns, url
# import the view from examiner app
from questionaire.views import welcome_view
from questionaire.json_views import questionaire_save, questionaire_responses
from examination.views import exam_welcome_view
from examination.json_views import answers_save, answer_evaluate

urlpatterns = patterns(
    '',
    url(r'^$', view=welcome_view, name='welcome_page'),
    url(r'^questionaire/save/?$', view=questionaire_save, name='questionaire_save'),
    url(r'^questionaire/responses/?$', view=questionaire_responses, name='questionaire_responses'),
    url(r'^answer/?$', view=exam_welcome_view, name='exam_welcome_view'),
    url(r'^answers/save/?$', view=answers_save, name='answers_save'),
    url(r'^answer/evaluate/?$', view=answer_evaluate, name='answer_evaluate'),
)
