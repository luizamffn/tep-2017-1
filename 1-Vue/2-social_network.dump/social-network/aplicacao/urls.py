from django.conf.urls import url
from aplicacao import views

urlpatterns = [
    url(r'^users/$', views.UserList.as_view(),name=views.UserList.name),
    url(r'^posts/$',views.PostList.as_view(),name=views.PostList.name),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(),name=views.PostDetail.name),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(),name=views.UserDetail.name),

    url(r'^$', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
