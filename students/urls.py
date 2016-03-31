from django.conf.urls import patterns, url
import students.views

urlpatterns = patterns('',
    url(r'^$', students.views.StudentListView.as_view(), name='list_view'),
    url(r'^(?P<pk>[0-9]+)/$', students.views.StudentDetailView.as_view(), name='detail'),
    url(r'^add/$', students.views.StudentCreateView.as_view(), name='add'),
    url(r'^edit/(?P<pk>[0-9]+)/$', students.views.StudentUpdateView.as_view(), name='edit'),
    url(r'^remove/(?P<pk>[0-9]+)/$', students.views.StudentDeleteView.as_view(), name='remove'),
)