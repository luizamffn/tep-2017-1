from django.conf.urls import url
from aplicacao import views

urlpatterns = [
    url(r'^users/$', views.UserList.as_view(),name=views.UserList.name),
    url(r'^posts/$',views.PostList.as_view(),name=views.PostList.name),
    url(r'^comments/$',views.CommentList.as_view(),name=views.CommentList.name),
    url(r'^pessoas/$',views.PessoaList.as_view(),name=views.PessoaList.name),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(),name=views.UserDetail.name),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(),name=views.PostDetail.name),
    url(r'^comments/(?P<pk>[0-9]+)/$', views.CommentDetail.as_view(),name=views.CommentDetail.name),
    url(r'^pessoas/(?P<pk>[0-9]+)/$', views.PessoaDetail.as_view(), name=views.PessoaDetail.name),
    url(r'^$', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    # url(r'^game-categories/(?P<pk>[0-9]+)/$', views.GameCategoryDetail.as_view(),
    #     name=views.GameCategoryDetail.name),
    # url(r'^games/$',views.GameList.as_view(),name=views.GameList.name),
    # url(r'^games/(?P<pk>[0-9]+)/$',views.GameDetail.as_view(),name=views.GameDetail.name),
    # url(r'^players/$',views.PlayerList.as_view(),name=views.PlayerList.name),
    # url(r'^players/(?P<pk>[0-9]+)/$',views.PlayerDetail.as_view(),name=views.PlayerDetail.name),
    # url(r'^scores/$',views.ScoreList.as_view(),name=views.ScoreList.name),
    # url(r'^scores/(?P<pk>[0-9]+)/$',views.ScoreDetail.as_view(),name=views.ScoreDetail.name),
    # url(r'^$',views.ApiRoot.as_view(),name=views.ApiRoot.name),
]
