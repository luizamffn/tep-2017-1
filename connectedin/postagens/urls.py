from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^perfil/publicar$', Publicar.as_view(), name='publicar'),
    url(r'^perfil/(?P<publicacao_id>\d+)/excluirPublicacao$', ExcluirPublicacao, name='excluirPublicacao'),
    url(r'^perfil/(?P<publicacao_id>\d+)/editarPublicacao$', EditarPublicacao, name='editarPublicacao'),
    url(r'^perfil/SalvarAlteracao$', SalvarAlteracao.as_view(), name='salvarAlteracao'),

]


