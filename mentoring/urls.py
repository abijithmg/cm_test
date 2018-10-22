from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', ment_stu_list, name='ment_stu_list'),
    url(r'^mentor_new$', mentor_create, name='mentor_new'),
    url(r'^mentor_edit/(?P<pk>\d+)$', mentor_edit, name='mentor_edit'),
    url(r'^mentor_delete/(?P<pk>\d+)$', mentor_delete, name='mentor_delete'),
    url(r'^student_new$', student_create, name='student_new'),
    url(r'^student_edit/(?P<pk>\d+)$', student_edit, name='student_edit'),
    url(r'^student_delete/(?P<pk>\d+)$', student_delete, name='student_delete'),
    url(r'^search_mentors/(?P<pk>\d+)$', search_mentors, name='search_mentors'),
]