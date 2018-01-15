from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .permissions import *
from rest_framework.throttling import ScopedRateThrottle
import django_filters.rest_framework
from rest_framework import filters, status
from django.utils import timezone
from django.contrib.auth.models import User


# Create your views here.

class UserList(generics.ListCreateAPIView):
    """
      get: Retorna a lista de usuários
      post: Adiciona um novo usuário
    """
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    name = 'user-list'
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('username', 'email')
    ordering_fields = ('username',)

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsUserOrReadOnly)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
     get: Exibe um usuario
     delete: Deleta um usuario
     put: Atualiza um usuario completo
     patch: Atualiza partes de um usuario
    """
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    name = 'user-detail'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsUserOrReadOnly)


class FuncionarioList(generics.ListCreateAPIView):
    """
      get: Retorna a lista de funcionários
      post: Adiciona um novo funcionário
    """
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    name = 'funcionario-list'
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('nome',)
    ordering_fields = ('nome',)

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsFuncionarioUserOrReadOnly)

    def create(self, request):
        serializer = FuncionarioSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = User.objects.create_user(username = serializer.validated_data.get('nome'),
                        email = str(serializer.validated_data.get('nome')) + '@gmail.com',
                        password = 123)
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FuncionarioDetail(generics.RetrieveUpdateDestroyAPIView):
    """
         get: Exibe um funcionário
         delete: Deleta um funcionáro
         put: Atualiza um funcionário completo
         patch: Atualiza partes de um funcionário
    """
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioDetailSerializer
    name = 'funcionario-detail'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsFuncionarioUserOrReadOnly)


class ClienteList(generics.ListCreateAPIView):
    """
      get: Retorna a lista de clientes
      post: Adiciona um novo cliente
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    name = 'cliente-list'
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('nome',)
    ordering_fields = ('nome', 'dataNasc')

    permission_classes = (
        permissions.IsAuthenticated,)
    # IsUserOrReadOnly)


class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    """
         get: Exibe um cliente
         delete: Deleta um cliente
         put: Atualiza um cliente completo
         patch: Atualiza partes de um cliente
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    name = 'cliente-detail'

    permission_classes = (
        permissions.IsAuthenticated,)
    # IsUserOrReadOnly)


class GeneroList(generics.ListCreateAPIView):
    """
      get: Retorna a lista de Gêneros
      post: Adiciona um novo Gênero
    """
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    name = 'genero-list'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,)
    # IsUserOrReadOnly)


class GeneroDetail(generics.RetrieveUpdateDestroyAPIView):
    """
         get: Exibe um gênero
         delete: Deleta um gênero
         put: Atualiza um gênero completo
         patch: Atualiza partes de um gênero
    """
    queryset = Genero.objects.all()
    serializer_class = GeneroDetailSerializer
    name = 'genero-detail'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,)
    # IsUserOrReadOnly)


class FilmeList(generics.ListCreateAPIView):
    """
      get: Retorna a lista de Filmes
      post: Adiciona um novo Filme
    """
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    name = 'filme-list'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,)
    # IsUserOrReadOnly)


class FilmeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
         get: Exibe um filme
         delete: Deleta um filme
         put: Atualiza um filme completo
         patch: Atualiza partes de um filme
    """
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    name = 'filme-detail'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,)
    # IsUserOrReadOnly)


class AluguelList(generics.ListCreateAPIView):
    """
        get: Retorna a lista de Alugueis
        post: Adiciona um novo Aluguel
    """
    queryset = Aluguel.objects.all()
    serializer_class = AluguelSerializer
    name = 'aluguel-list'

    permission_classes = (
        permissions.IsAuthenticated,)

    def create(self, request):
        serializer = AluguelSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            if serializer.validated_data.get('dataPrevistaDevolucao') < timezone.localdate():
                content = {
                    "detail": "A data de previsão para entrega não pode ser menor que a atual"
                }
                return Response(content, status=status.HTTP_403_FORBIDDEN)
            diferenca = serializer.validated_data.get('dataPrevistaDevolucao') - timezone.localdate()
            valor_total = serializer.validated_data.get('filme').valor * diferenca.days  # valorDias
            serializer.save(dataAluguel=timezone.localdate(), valor=valor_total, user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AluguelDetail(generics.RetrieveUpdateDestroyAPIView):
    """
         get: Exibe um aluguel
         delete: Deleta um aluguel
         put: Atualiza um aluguel completo
         patch: Atualiza partes de um aluguel
    """
    queryset = Aluguel.objects.all()
    serializer_class = AluguelSerializer
    name = 'aluguel-detail'

    permission_classes = (
        permissions.IsAuthenticated,)
    # IsUserOrReadOnly)


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'users': reverse(UserList.name, request=request),
            'funcionarios': reverse(FuncionarioList.name, request=request),
            'clientes': reverse(ClienteList.name, request=request),
            'generos': reverse(GeneroList.name, request=request),
            'filmes': reverse(FilmeList.name, request=request),
            'alugueis': reverse(AluguelList.name, request=request)
        })
