from django.conf.urls import url
from django.views.generic import RedirectView
from .views import *
from django.contrib.auth import views

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^people/$', people, name='people'),
    url(r'^projects/$', projects, name='projects'),
    url(r'^tasks/$', tasks, name='tasks'),
    url(r'^resources/$', resources, name='resources'),

    url(r'^people/new_person$', NewPersonView.as_view(), name='new_person'),
    url(r'^projects/new_project$', NewProjectView.as_view(), name='new_project'),
    url(r'^tasks/new_task$', NewTaskView.as_view(), name='new_task'),
    url(r'^resources/new_resource$', NewResourceView.as_view(), name='new_resource'),

    url(r'^project/(?P<project_id>\d+)$', project_detail, name='project_detail'),
    url(r'^person/(?P<person_id>\d+)$', person_detail, name='person_detail'),
    url(r'^resource/(?P<resource_id>\d+)$', resource_detail, name='resource_detail'),

    url(r'^task/(?P<task_id>\d+)/check$', check_task, name='check_task'),
    url(r'^task/(?P<task_id>\d+)/uncheck$', uncheck_task, name='uncheck_task'),
    url(r'^task/(?P<task_id>\d+)/delete$', delete_task, name='delete_task'),
    url(r'^project/(?P<project_id>\d+)/delete$', delete_project, name='delete_project'),
    url(r'^resource/(?P<resource_id>\d+)/delete$', delete_resource, name='delete_resource'),
    url(r'^person/(?P<person_id>\d+)/delete$', delete_person, name='delete_person'),

    url(r'^login/$', views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(template_name='login.html'), name='logout'),
    url(r'^register/$', RegisterUserView.as_view(), name='register'),

    url(r'^luki/$', RedirectView.as_view(url='http://lukinow.com'), name='luki')
]