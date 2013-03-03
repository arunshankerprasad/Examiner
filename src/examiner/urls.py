from django.conf.urls.defaults import patterns, include, url
# import the view from helloapp
from questionaire.views import welcome_view
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', view=welcome_view, name='welcome_page'),
#    url(r'^admin/', include(admin.site.urls)),
)
