from django.db import models

# Create your models here.

class Time(models.Model):
    nome = models.CharField(max_length=150)

class Jogador(models.Model):
    cpf = models.CharField(max_length=20)
    nome = models.CharField(max_length=150)
    posicao = models.IntegerField()
    numCamisa = models.IntegerField()
    time = models.ForeignKey(Time, on_delete= models.PROTECT)

class Comisao(models.Model):
    cpf = models.CharField(max_length=20)
    nome = models.CharField(max_length=150)
    funcao = models.CharField(max_length=100)
    time = models.ForeignKey(Time, on_delete=models.PROTECT)

class Estadio(models.Model):
    nome = models.CharField(max_length=150)
    lotacao = models.IntegerField()
    endereco = models.CharField(max_length=150)

class Jogo(models.Model):
    timeMandate = models.ForeignKey(Time, on_delete=models.PROTECT, related_name="time_mandante")
    timeVisitante = models.ForeignKey(Time, on_delete=models.PROTECT, related_name="time_visitante")

class Partida(models.Model):
    placarMandante = models.IntegerField()
    placarVisitante = models.IntegerField()
    data = models.DateTimeField()
    jogo = models.ForeignKey(Jogo, on_delete=models.PROTECT)
    estadio = models.ForeignKey(Estadio, on_delete=models.PROTECT)




