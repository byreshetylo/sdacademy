from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'courses.views.index', name='index'),
    url(r'^(?P<pk>[0-9]+)/$', 'courses.views.detail', name='detail'),
    url(r'^(?P<pk>[0-9]+)/add_lesson$', 'courses.views.add_lesson', name='add_lesson'),
    url(r'^add/$', 'courses.views.add', name='add'),
    url(r'^edit/(?P<pk>[0-9]+)/$', 'courses.views.edit', name='edit'),
    url(r'^remove/(?P<pk>[0-9]+)/$', 'courses.views.remove', name='remove'),
)
