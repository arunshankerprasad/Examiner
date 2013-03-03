from django import forms


class QuestionForm(forms.Form):
    text = forms.CharField(max_length=400, required=True)
    typ = forms.ChoiceField(choices=((0, 'Multiple Choice'), (1, 'Descriptive')), required=False)
    help_text = forms.CharField(max_length=400, required=False)
    marks = forms.CharField(max_length=400, required=False)
