import logging

from django.template import Context, loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from models import Question
from forms import QuestionForm

## http://stackoverflow.com/questions/2249792/json-serializing-django-models-with-simplejson
from django.core.serializers import serialize
from django.utils.simplejson import dumps, loads, JSONEncoder
from django.db.models.query import QuerySet
from django.db.models import Model
from django.utils.functional import curry

class DjangoJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, QuerySet) or isinstance(obj, model):
            # `default` must return a python serializable
            # structure, the easiest way is to load the JSON
            # string produced by `serialize` and return it
            return loads(serialize('json', obj))
        return JSONEncoder.default(self,obj)

# partial function, we can now use dumps(my_dict) instead
# of dumps(my_dict, cls=DjangoJSONEncoder)


@csrf_exempt
def search(request):
    r = {}

    form = QuestionForm(data=request.GET)
    if form.is_valid():
        r['is_success'] = True
        # r['users'] = loads(serialize('json', users[:100]))
    else:
        r['is_success'] = False
        r.update(form.errors)

    return HttpResponse(dumps(r), mimetype='application/json')
