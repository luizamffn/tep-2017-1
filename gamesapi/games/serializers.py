from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


# class GameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Game
#         fields = ('id', 'name', 'release_date', 'game_category')
#
#     def is_valid(self, request):
#         print("data")
#         print(self.initial_data)
#         if(request.method == 'POST' or request.method == 'PUT'):
#             for f in self.fields:
#                 if f != 'id':
#                     if(self.initial_data[f] == None or self.initial_data[f] == ''):
#                          raise serializers.ValidationError("Nenhum valor pode ser vazio!")
#
#             game =Game.objects.filter(name=self.initial_data['name'])
#             if game.count() > 0:
#                 raise serializers.ValidationError("Esse jogo ja foi registrado!")
class GameSerializer(serializers.HyperlinkedModelSerializer):
    game_category = serializers.SlugRelatedField(queryset=GameCategory.objects.all(),
                                                 slug_field='name') #tras somente a descricao da categoria
    class Meta:
        model = Game
        fields = ('url',
                  'game_category',
                  'name',
                  'release_date',
                  'played')

class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = GameCategory
        fields = ('url', 'pk', 'name', 'games', 'owner')

class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    game = serializers.SlugRelatedField(queryset=Game.objects.all(),
                                                 slug_field='name')
    player = serializers.SlugRelatedField(queryset=Player.objects.all(),
                                                 slug_field='name')
    class Meta:
        model = Score
        fields = ('url',
                  'pk',
                  'score',
                  'score_date',
                  'player',
                  'game')

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    scores = ScoreSerializer(many=True, read_only=True)
    class Meta:
        model = Player
        fields = ('url',
                  'name',
                  'gender',
                  'scores')

class UserGameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('url','name')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    games = UserGameSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('url', 'pk','username','games')
