from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')


class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Funcionario
        fields = ('url', 'nome', 'salario')


class FuncionarioDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Funcionario
        fields = ('url', 'nome', 'user')


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ('url', 'id', 'nome', 'dataNasc', 'cpf')


class GeneroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genero
        fields = ('url', 'id', 'descricao')


class GeneroDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genero
        fields = ('url', 'descricao', 'filmes')


class FilmeSerializer(serializers.HyperlinkedModelSerializer):
    categoria = serializers.SlugRelatedField(queryset=Genero.objects.all(),
                                                 slug_field='descricao')
    class Meta:
        model = Filme
        fields = ('url','id','nome', 'valor', 'categoria')


class AluguelSerializer(serializers.HyperlinkedModelSerializer):
    valor = serializers.ReadOnlyField()
    dataAluguel = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.username')
    filme = serializers.SlugRelatedField(queryset=Filme.objects.all(),
                                             slug_field='nome')

    cliente = serializers.SlugRelatedField(queryset=Cliente.objects.all(),
                                         slug_field='nome')

    class Meta:
        model = Aluguel
        fields = ('url', 'id', 'dataAluguel','dataPrevistaDevolucao','user','filme','cliente', 'valor')
