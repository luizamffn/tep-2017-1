from django.conf.urls import url
from .views import *
from django.contrib.auth import views

urlpatterns = [
    url(r'^$', projeto, name='projeto'),
    url(r'^login/$', views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(template_name='login.html'), name="logout"),
    url(r'^pessoa$', pessoa, name='pessoa'),
    url(r'^atividade', atividade, name='atividade'),
    url(r'^cadastrarProjeto/$', CadastrarProjeto.as_view() , name = 'cadastrarProjeto'),
    url(r'^cadastrarPessoa/$', CadastrarPessoa.as_view() , name = 'cadastrarPessoa'),
    url(r'^cadastraratividade/$', CadastrarAtividade.as_view() , name = 'cadastrarAtividade'),
]


