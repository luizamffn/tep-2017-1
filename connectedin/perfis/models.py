# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Perfil(models.Model):
    PERGUNTAS = (
        (1, "Onde você nasceu?"),
        (2, "Qual é o nome da sua mãe?"),
        (3, "Qual é o nome do seu melhor amigo?"),
    )

    nome = models.CharField(max_length=255, null=False)
    imagem = models.ImageField(upload_to='perfil/', default='perfil/person.png', null=True)
    email = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=255, null=False)
    nome_empresa = models.CharField(max_length=255, null=False)
    contatos = models.ManyToMafnyField('self')
    usuario = models.OneToOneField(User, related_name='perfil', on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)
    justificativa = models.CharField(max_length=255, null=False)
    pergunta = models.CharField(max_length=255, null=False)
    resposta = models.CharField(max_length=255, null=False)

    @property
    def email(self):
        return self.usuario.email

    def convidar(self, perfil_convidado):
        c = Convite(solicitante=self, convidado=perfil_convidado)
        c.save()

    def bloquear(self, perfil_bloqueado):
        Bloqueado.objects.create(solicitante=self, bloqueado=perfil_bloqueado)
        if self.contatos.filter(pk=perfil_bloqueado.pk) is not None:
            self.desfazerAmizade(perfil_bloqueado)
            perfil_bloqueado.desfazerAmizade(self)

        c_feito = Convite.objects.filter(solicitante=self, convidado=perfil_bloqueado)
        c_recebido = Convite.objects.filter(solicitante=perfil_bloqueado, convidado=self)
        if c_feito != None:
            c_feito.delete()

        if c_recebido != None:
            c_recebido.delete()

    def desbloquear(self, perfil_bloqueado):
        b = Bloqueado.objects.filter(solicitante=self, bloqueado=perfil_bloqueado)
        b.delete()

    def desativarPerfil(self, justificativa):
        self.ativo = False
        self.justificativa = justificativa
        self.save()

    def ativarPerfil(self):
        self.ativo = True
        self.save()

    def excluir(self):
        postagens = Postagem.objects.filter(perfil=self)
        for p in postagens:
            p.delete()

        self.usuario.delete()

    def desfazerAmizade(self, contato):
        self.contatos.remove(contato)

class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil, related_name='convites_feitos')
    convidado = models.ForeignKey(Perfil, related_name='convites_recebidos')

    def aceitar(self):
        self.solicitante.contatos.add(self.convidado)
        self.convidado.contatos.add(self.solicitante)
        self.delete()

    def excluir_c(self):
        self.delete()


class Postagem(models.Model):
    descricao = models.TextField(max_length=1000, null=False)
    perfil = models.ForeignKey(Perfil, related_name='postagens')
    data = models.DateField(null=True)
    imagem = models.ImageField(upload_to='posts/', null=True)

    def excluirPublicacao(self):
        self.delete()

class Bloqueado(models.Model):
    solicitante = models.ForeignKey(Perfil, related_name='bloqueios_feitos')
    bloqueado = models.ForeignKey(Perfil, related_name='bloqueios_recebidos')

