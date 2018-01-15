"""
Book: Building RESTful Python Web Services
Chapter 2: Working with class based views and hyperlinked APIs in Django
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from django.conf.urls import url
from games import views

urlpatterns = [
    # url(r'^games/$', views.game_list),
    # url(r'^games/(?P<pk>[0-9]+)/$', views.game_detail),
    url(r'^game-categories/$', views.GameCategoryList.as_view(),
        name=views.GameCategoryList.name),
    url(r'^game-categories/(?P<pk>[0-9]+)/$', views.GameCategoryDetail.as_view(),
        name=views.GameCategoryDetail.name),
    url(r'^games/$',views.GameList.as_view(),name=views.GameList.name),
    url(r'^games/(?P<pk>[0-9]+)/$',views.GameDetail.as_view(),name=views.GameDetail.name),
    url(r'^players/$',views.PlayerList.as_view(),name=views.PlayerList.name),
    url(r'^players/(?P<pk>[0-9]+)/$',views.PlayerDetail.as_view(),name=views.PlayerDetail.name),
    url(r'^scores/$',views.ScoreList.as_view(),name=views.ScoreList.name),
    url(r'^scores/(?P<pk>[0-9]+)/$',views.ScoreDetail.as_view(),name=views.ScoreDetail.name),
    url(r'^users/$', views.UserList.as_view(), name=views.UserList.name),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name=views.UserDetail.name),
    url(r'^$',views.ApiRoot.as_view(),name=views.ApiRoot.name),
]
