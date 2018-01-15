from django.conf.urls import url
from pools import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^question/(?P<question_id>\d+)$', views.question, name='question'),
    url(r'^question/(?P<question_id>\d+)/results$', views.resultados, name='resultados'),
    url(r'^question/(?P<choice_id>\d+)/votar$', views.votar, name='votar'),
    url(r'^question/(?P<question_id>\d+)/manage$', views.manage, name='manage'),
    url(r'^question/(?P<choice_id>\d+)/remover$', views.remover, name='remover'),
    url(r'^question/(?P<question_id>\d+)/abirStatus$', views.abirStatus, name='abirStatus'),
    url(r'^question/(?P<question_id>\d+)/fecharStatus$', views.fecharStatus, name='fecharStatus'),
]
