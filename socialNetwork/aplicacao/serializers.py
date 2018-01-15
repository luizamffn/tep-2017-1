from django.contrib.gis import serializers
from rest_framework import serializers
from .models import *

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    # post = serializers.HyperlinkedIdentityField(many=True, read_only=True)
    class Meta:
        model = Comment
        fields = ("url", "name", "email", "body", 'post')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(),
                                        slug_field="username")
    class Meta:
        model = Post
        fields = ("url", "title", "body", "user")

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("url", "username", "email")

class PessoaSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.HyperlinkedIdentityField(many=True, read_only=True)

    class Meta:
        model = Pessoa
        fields = ("url", "name", "email", "user")

class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='post-detail')
    class Meta:
        model = User
        fields = ("url", "username", "email", "posts")

class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(),
                                                slug_field="username")
    comentarios = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='comment-detail')

    class Meta:
         model = Post
         fields = ("url", "title", "body", "user", "comentarios")

# class UserGameSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Post
#         fields = ('url','title')

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     games = UserGameSerializer(many=True, read_only=True)
#     class Meta:
#         model = User
#         fields = ('url', 'pk','username','games')