
from django.conf.urls import url
from aluguel.views import *
from django.contrib.auth import views

urlpatterns = [
    url(r'^$', ApiRoot.as_view(),name=ApiRoot.name),

    # url(r'^login/$', views.LoginView.as_view, name='login'),
    url(r'^users/$', UserList.as_view(), name=UserList.name),
    url(r'^user/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name=UserDetail.name),
    url(r'^funcionarios/$', FuncionarioList.as_view(), name=FuncionarioList.name),
    url(r'^funcionario/(?P<pk>[0-9]+)/$', FuncionarioDetail.as_view(), name=FuncionarioDetail.name),
    url(r'^clientes/$', ClienteList.as_view(), name=ClienteList.name),
    url(r'^cliente/(?P<pk>[0-9]+)/$', ClienteDetail.as_view(), name=ClienteDetail.name),
    url(r'^generos/$', GeneroList.as_view(), name=GeneroList.name),
    url(r'^genero/(?P<pk>[0-9]+)/$', GeneroDetail.as_view(), name=GeneroDetail.name),
    url(r'^filmes/$', FilmeList.as_view(), name=FilmeList.name),
    url(r'^filme/(?P<pk>[0-9]+)/$', FilmeDetail.as_view(), name=FilmeDetail.name),
    url(r'^alugueis/$', AluguelList.as_view(), name=AluguelList.name),
    url(r'^aluguel/(?P<pk>[0-9]+)/$', AluguelDetail.as_view(), name=AluguelDetail.name),
]
