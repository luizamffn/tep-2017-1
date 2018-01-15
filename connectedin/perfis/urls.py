from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', index, name = 'index'),
    url(r'^perfil/(?P<perfil_id>\d+)$', exibir, name = 'exibir'),
	url(r'^perfil/(?P<perfil_id>\d+)/convidar$', convidar, name = 'convidar'),
	url(r'^perfil/(?P<convite_id>\d+)/aceitar$', aceitar, name = 'aceitar'),
    url(r'^configuracoes/$', configuracoes , name = 'configuracoes'),
    url(r'^perfil/(?P<perfil_id>\d+)/bloquear$', bloquear, name = 'bloquear'),
    url(r'^perfil/(?P<perfil_id>\d+)/desbloquear$', desbloquear, name = 'desbloquear'),
    url(r'^perfil/desativar$', desativarPerfil, name='desativarPerfil'),
    url(r'^confimarDesativacao$', ConfimarDesativacao.as_view(), name='confimarDesativacao'),
    url(r'^perfil/ativar$', ativarPerfil, name='ativarPerfil'),
    url(r'^perfil/confirmarAtivacao$', confirmarAtivacao, name='confirmarAtivacao'),
    url(r'^perfil/buscarUsuario$', BuscarUsuario.as_view(), name='buscarUsuario'),
    url(r'^amigos/$', amigos, name='amigos'),
    url(r'^convites/$', convites, name='convites'),
    url(r'^todosPerfis/$', todosPerfis, name='todosPerfis'),
    url(r'^perfil/(?P<perfil_id>\d+)/excluirPerfil$', excluirPerfil, name='excluirPerfil'),
    url(r'^perfil/alterarImagemPerfil$', AlterarImagemPerfil.as_view(), name='alterarImagemPerfil'),
    url(r'^perfil/perfisBloqueados$', perfisBloqueados, name='perfisBloqueados'),
]


