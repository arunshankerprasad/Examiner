from django import forms
from django.core.exceptions import ValidationError

from google.appengine.ext import ndb


class AnswerForm(forms.Form):
    text = forms.CharField(required=True)
    question = forms.CharField(required=True)

    def clean_question(self):
        question = self.cleaned_data['question']

        try:
            question = ndb.Key(urlsafe=question)
        except:
            raise ValidationError('Select a valid option.')

        return question
