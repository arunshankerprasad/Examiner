from google.appengine.ext import ndb


# Create your models here.
class Answer(ndb.Model):
    text = ndb.StringProperty(required=True)
    marks = ndb.FloatProperty(required=False)
    question = ndb.KeyProperty(required=True)
    answered_by = ndb.UserProperty(required=True)
    is_evaluated = ndb.BooleanProperty(required=False)
    is_correct = ndb.BooleanProperty(required=False)

    lastUpdatedOn = ndb.DateTimeProperty(auto_now = True)
