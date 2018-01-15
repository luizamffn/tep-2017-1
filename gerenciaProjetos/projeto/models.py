from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Responsavel(models.Model):
    nome = models.CharField(max_length=255)
    salario = models.FloatField()
    funcao = models.CharField(max_length=255)

class Projeto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    valor = models.FloatField(null=True)
    user = models.ForeignKey(User, related_name="projetos", on_delete=models.CASCADE)
    # gerente = models.ForeignKey(Responsavel, related_name="projetos", on_delete=models.CASCADE)
    dataCadastro = models.DateField(null=False)

class Recurso(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    valor = models.FloatField()

class Atividade(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    dataInicio = models.DateField()
    dataFim = models.DateField()
    projeto = models.ForeignKey(Projeto, related_name="atividades", on_delete=models.CASCADE)
    responsavel = models.ForeignKey(Responsavel, related_name="atividades")
    recursos = models.ManyToManyField(Recurso, related_name="atividades", null=True)