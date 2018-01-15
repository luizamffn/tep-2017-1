from django.conf.urls import url
from .views import *
from perfis.views import *
from django.contrib.auth import views

urlpatterns = [
	url(r'^registrar/$', RegistrarUsuarioView.as_view() , name = 'registrar'),
	url(r'^login/$', views.LoginView.as_view(template_name='login.html'), name = 'login'),
    url(r'^logout/$', views.LogoutView.as_view(template_name='login.html'), name="logout"),
	url(r'^alterarSenha/$', AlterarSenha.as_view() , name = 'alterarSenha'),
	url(r'^recuperarSenha/$', RecuperarSenha.as_view() , name = 'recuperarSenha'),
	url(r'^recuperarSenhaUsuario/$', RecuperarSenhaUsuario.as_view() ,name = 'recuperarSenhaUsuario'),
]