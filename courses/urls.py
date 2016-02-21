from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'courses.views.index', name='index'),
    url(r'^(?P<pk>[0-9]+)/$', 'courses.views.detail', name='detail'),
)
