from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Funcionario(models.Model):
    nome = models.CharField(max_length=255)
    user = models.OneToOneField(User, related_name='funcionario', on_delete=models.CASCADE)
    salario = models.FloatField()

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    dataNasc = models.DateField()
    cpf = models.CharField(max_length=50)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome

class Genero(models.Model):
    descricao = models.CharField(max_length=255)

    class Meta:
        ordering = ('descricao',)

    def __str__(self):
        return self.descricao

class Filme(models.Model):
    nome = models.CharField(max_length=255)
    valor = models.FloatField()
    categoria = models.ForeignKey(Genero, related_name='filmes', on_delete=models.CASCADE)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome

class Aluguel(models.Model):
    dataAluguel = models.DateField()
    dataPrevistaDevolucao = models.DateField()
    dataDevolucao = models.DateField(null=True)
    multa = models.FloatField(null=True)
    valor = models.FloatField(null=True)
    filme = models.ForeignKey(Filme, related_name='alugueis', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='alugueis', on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, related_name='alugueis', on_delete=models.CASCADE)


