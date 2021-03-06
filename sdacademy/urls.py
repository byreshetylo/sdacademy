from django.conf.urls import patterns, include, url
from django.contrib import admin
import feedbacks.views


urlpatterns = patterns('',
    url(r'^$', 'sdacademy.views.index', name='index'),
    url(r'^contact/', 'sdacademy.views.contact', name='contact'),

    url(r'^feedback/$', feedbacks.views.FeedbackView.as_view(), name='feedback'),

    url(r'^student_list/', 'sdacademy.views.student_list', name='student_list'),
    url(r'^student_detail/', 'sdacademy.views.student_detail', name='student_detail'),

    url(r'^quadratic/', 'quadratic.views.quadratic_results', name='results'),

    url(r'^courses/', include('courses.urls', namespace='courses')),
    url(r'^students/', include('students.urls', namespace='students')),
    url(r'^coaches/', include('coaches.urls', namespace='coaches')),

    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^admin/', include(admin.site.urls)),
)
