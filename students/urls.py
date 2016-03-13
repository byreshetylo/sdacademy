from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'students.views.list_view', name='list_view'),
    url(r'^(?P<pk>[0-9]+)/$', 'students.views.detail', name='detail'),
    url(r'^add/$', 'students.views.create', name='add'),
    url(r'^edit/(?P<pk>[0-9]+)/$', 'students.views.edit', name='edit'),
    url(r'^remove/(?P<pk>[0-9]+)/$', 'students.views.remove', name='remove'),
)