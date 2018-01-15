# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from perfis.forms import *
from datetime import datetime


# Create your views here.

@login_required
def index(request):
    if (get_perfil_logado(request).ativo == False):
        return redirect('ativarPerfil')
    else:
        ids_contatos = [r.id for r in get_perfil_logado(request).contatos.all()]
        ids_contatos.append(get_perfil_logado(request).id)

        postagens = Postagem.objects.filter(perfil_id__in=ids_contatos).order_by('-id')

        return render(request, 'funcionarios.html', {'perfil_logado': get_perfil_logado(request),
                                              'postagens': postagens})


@login_required
def exibir(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    ja_eh_contato = perfil in perfil_logado.contatos.all()
    convite = Convite.objects.filter(solicitante=perfil_logado, convidado=perfil)

    ja_eh_convidado = (convite.count() != 0)

    bloqueados = [p.bloqueado for p in Bloqueado.objects.filter(solicitante=perfil_logado)]
    bloqueado_feitos = bloqueados.__contains__(perfil);

    solicitantes = [p.solicitante for p in Bloqueado.objects.filter(bloqueado=perfil_logado)]
    bloqueio_recebido = solicitantes.__contains__(perfil);

    postagens = Postagem.objects.filter(perfil=perfil).order_by('-id')

    return render(request, 'perfil.html', {'perfil': perfil,
                                           'perfil_logado': perfil_logado,
                                           'ja_eh_contato': ja_eh_contato,
                                           'ja_eh_convidado': ja_eh_convidado,
                                           'bloqueado': bloqueado_feitos,
                                           'bloqueio_recebido': bloqueio_recebido,
                                           'postagens': postagens})


@login_required
def convidar(request, perfil_id):
    perfil_convidado = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_convidado)
    return redirect('index')


@login_required
def aceitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('index')


@login_required
def get_perfil_logado(request):
    return request.user.perfil


@login_required
def configuracoes(request):
    return render(request, 'configuracoes.html', {'perfil_logado': get_perfil_logado(request)})


@login_required
def bloquear(request, perfil_id):
    perfil_bloqueado = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.bloquear(perfil_bloqueado)
    return redirect('index')


@login_required
def desbloquear(request, perfil_id):
    perfil_bloqueado = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.desbloquear(perfil_bloqueado)
    return redirect('index')


@login_required
def desativarPerfil(request):
    return render(request, 'desativarPerfil.html', {'perfil_logado': get_perfil_logado(request)})


class ConfimarDesativacao(View):
    form_class = DesativarPerfil

    def get(self, request):
        return render(request, 'desativarPerfil.html', {'perfil_logado': get_perfil_logado(request)})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if (form.is_valid()):
            dados = form.cleaned_data
            get_perfil_logado(request).desativarPerfil(dados['justificativa'])
            return redirect('logout')

        return render(request, 'desativarPerfil.html', {'form': form})


@login_required
def ativarPerfil(request):
    return render(request, 'ativarPerfil.html')


@login_required
def confirmarAtivacao(request):
    get_perfil_logado(request).ativarPerfil()
    return redirect('index')


class BuscarUsuario(View):
    form_class = BuscarUsuario

    def get(self, request):
        return render(request, 'buscarUsuario.html', {'perfil_logado': get_perfil_logado(request)})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if (form.is_valid()):
            dados = form.cleaned_data

            perfis = Perfil.objects.filter(nome__contains=dados['nome']).exclude(id=get_perfil_logado(request).id)

            return render(request, 'buscarUsuario.html',
                          {'perfil_logado': get_perfil_logado(request), "perfis": perfis})

        return render(request, 'index', {'form': form})


@login_required
def amigos(request):
    return render(request, 'amigos.html', {'perfil_logado': get_perfil_logado(request)})


@login_required
def convites(request):
    return render(request, 'convites.html', {'perfil_logado': get_perfil_logado(request)})


@login_required
def todosPerfis(request):
    perfis = Perfil.objects.all()
    return render(request, 'todosPerfis.html', {'perfis': perfis, 'perfil_logado': get_perfil_logado(request)})


@login_required
def excluirPerfil(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    perfil.excluir()
    return redirect('todosPerfis')


class AlterarImagemPerfil(View):
    form_class = AlterarImagemPerfil

    def get(self, request):
        pass

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if (form.is_valid(request)):
            dados = form.cleaned_data

            perfil = get_perfil_logado(request)
            perfil.imagem = dados['imagem']
            perfil.save()

            return redirect('exibir', get_perfil_logado(request).id)

        return redirect('exibir', get_perfil_logado(request).id)


@login_required
def perfisBloqueados(request):
    bloqueados = Bloqueado.objects.filter(solicitante=get_perfil_logado(request));
    return render(request, 'perfisBloqueados.html',
                  {'perfil_logado': get_perfil_logado(request), 'bloqueados': bloqueados})
