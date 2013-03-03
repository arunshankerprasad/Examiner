from google.appengine.ext import ndb


# Create your models here.
class Question(ndb.Model):
    text = ndb.StringProperty(required=True)
    typ = ndb.StringProperty(required=False)
    help_text = ndb.TextProperty(required=True)
    marks = ndb.FloatProperty(required=False)

    lastUpdatedOn = ndb.DateTimeProperty(auto_now = True)


class Questionaire(ndb.Model):
    questions = ndb.KeyProperty(repeated=True)

    lastUpdatedOn = ndb.DateTimeProperty(auto_now=True)
