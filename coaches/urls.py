from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^(?P<pk>[0-9]+)/$', 'coaches.views.detail', name='detail'),
)