from google.appengine.ext import ndb

# Create your models here.

class Question(ndb.Model):
    host = ndb.StringProperty(required = True)
    title = ndb.StringProperty(required = True)
    description = ndb.TextProperty(required = True)
    when = ndb.DateProperty(required = True)
    where = ndb.TextProperty(required = True)
    agenda = ndb.JsonProperty(required = True)

    lastUpdatedOn = ndb.DateTimeProperty(auto_now = True)
    # lastUpdatedBy = ndb.ReferenceProperty(Member)
