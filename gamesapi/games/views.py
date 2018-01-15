"""
Book: Building RESTful Python Web Services
Chapter 2: Working with class based views and hyperlinked APIs in Django
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import *
from .serializers import *
from datetime import datetime
from django.utils import timezone
from rest_framework import generics
from rest_framework import permissions
from .permissions import *
from rest_framework.throttling import ScopedRateThrottle

# @api_view(['GET', 'POST'])
# def game_list(request):
#     if request.method == 'GET':
#         games = Game.objects.all()
#         games_serializer = GameSerializer(games, many = True)
#         return Response(games_serializer.data)
#     elif request.method == 'POST':
#         games_serializer = GameSerializer(data=request.data)
#         if games_serializer.is_valid(request):
#             games_serializer.save()
#             return Response(games_serializer.data,
#                             status=status.HTTP_201_CREATED)
#         return Response(games_serializer.errors,
#                         status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def game_detail(request, pk):
#     try:
#         game = Game.objects.get(pk=pk)
#     except Game.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         game_serializer = GameSerializer(game)
#         return Response(game_serializer.data)
#     elif request.method == 'PUT':
#         games_serializer = GameSerializer(game, data=request.data)
#         if games_serializer.is_valid(request):
#             games_serializer.save()
#             return Response(games_serializer.data)
#         return Response(games_serializer.errors,
#                         status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         data = timezone.make_aware(datetime.now(), timezone.get_current_timezone())
#         if data < game.release_date:
#             game.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         else:
#             return Response({"Este jogo ainda não foi lançado"}, status=status.HTTP_403_FORBIDDEN)

class GameCategoryList(generics.ListCreateAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name ='gamecategory-list'
    throttle_scope = 'game-categories'
    throttle_classes = (ScopedRateThrottle,)

class GameCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-detail'

    throttle_scope = 'game-categories'
    throttle_classes = (ScopedRateThrottle,)

class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-list'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-detail'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly)


class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-list'

class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-detail'

class ScoreList(generics.ListCreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    name = 'score-list'

class ScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    name = 'score-detail'

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserGameSerializer
    name = 'user-list'

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'players': reverse(PlayerList.name,request=request),
            'game-categories': reverse(GameCategoryList.name,request=request),
            'games': reverse(GameList.name,request=request),
            # 'game-categories': reverse(GameCategoryList.name,request=request),
            'scores': reverse(ScoreList.name,request=request),
            'users': reverse(UserList.name, request=request)
        })

