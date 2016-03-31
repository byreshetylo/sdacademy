from django.conf.urls import patterns, url
import courses.views

urlpatterns = patterns('',
    # url(r'^$', courses.views.CourseDetailView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', courses.views.CourseDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/add_lesson$', courses.views.add_lesson, name='add_lesson'),
    url(r'^add/$', courses.views.CourseCreateView.as_view(), name='add'),
    url(r'^edit/(?P<pk>[0-9]+)/$', courses.views.CourseUpdateView.as_view(), name='edit'),
    url(r'^remove/(?P<pk>[0-9]+)/$', courses.views.CourseDeleteView.as_view(), name='remove'),
)
