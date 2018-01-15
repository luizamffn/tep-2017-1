
from django.conf.urls import url
from cliente.views import *
from django.contrib.auth import views

urlpatterns = [
    url(r'^base/$', base, name="base"),
    url(r'^index/$', index, name="index"),
    url(r'^login/$', login, name='login'),
    url(r'^home/$', home, name='home'),
    url(r'^list_generos/$', generos, name='list_generos'),
    url(r'^list_filmes/$', filmes, name='list_filmes'),
    url(r'^list_filmes_not_atuh/$', filmes_not_auth, name='list_filmes_not_auth'),
    url(r'^list_clientes/$', clientes, name='list_clientes'),
    url(r'^list_alugueis/$', alugueis, name='list_alugueis'),
    url(r'^permission/$', permission, name='permission'),
    # url(r'^user/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name=UserDetail.name),
    # url(r'^funcionarios/$', FuncionarioList.as_view(), name=FuncionarioList.name),
    # url(r'^funcionario/(?P<pk>[0-9]+)/$', FuncionarioDetail.as_view(), name=FuncionarioDetail.name),
    # url(r'^clientes/$', ClienteList.as_view(), name=ClienteList.name),
    # url(r'^cliente/(?P<pk>[0-9]+)/$', ClienteDetail.as_view(), name=ClienteDetail.name),
    # url(r'^generos/$', GeneroList.as_view(), name=GeneroList.name),
    # url(r'^genero/(?P<pk>[0-9]+)/$', GeneroDetail.as_view(), name=GeneroDetail.name),
    # url(r'^filmes/$', FilmeList.as_view(), name=FilmeList.name),
    # url(r'^filme/(?P<pk>[0-9]+)/$', FilmeDetail.as_view(), name=FilmeDetail.name),
    # url(r'^alugueis/$', AluguelList.as_view(), name=AluguelList.name),
    # url(r'^aluguel/(?P<pk>[0-9]+)/$', AluguelDetail.as_view(), name=AluguelDetail.name),
]
