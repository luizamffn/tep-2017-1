# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from perfis.views import *

from django.shortcuts import render
from usuarios.urls import *

# Create your views here.


from django.shortcuts import render
from django.views.generic.base import View
from usuarios.forms import *
from django.contrib.auth.models import User
from perfis.models import Perfil
from django.shortcuts import redirect

# Create your views here.


class RegistrarUsuarioView(View):

	def get(self, request):
		usuario = User.objects.filter(is_superuser = 1)
		if (usuario != None):
			ja_tem_adm = True
		else:
			ja_tem_adm = False
		return render(request, 'registrar.html', {'ja_tem_adm' : ja_tem_adm})

	def post(self, request):
		form = RegistrarUsuarioForm(request.POST)

		if (form.is_valid()) :
			dados = form.cleaned_data

			if(dados['administrador'] == 'Sim'):
				usuario = User.objects.create_user(username= dados['nome'],
				email = dados['email'],
				password= dados['senha'],
				is_superuser = 1)
			else:
				usuario = User.objects.create_user(username= dados['nome'],
							   email= dados['email'],
							   password= dados['senha'])


			perfil = Perfil(nome = usuario.username, 
							nome_empresa = dados['nome_empresa'],
							telefone = dados['telefone'],
							usuario = usuario,
							pergunta = dados['pergunta'],
							resposta = dados['resposta'])
			perfil.save()
			return redirect('index')
		
		return render(request, 'registrar.html', {'form': form})

class AlterarSenha(View):
	form_class = AlterarSenha
	def get(self, request):
		return render(request, 'alterarSenha.html')

	def post(self, request,*args, **kwargs):
		form = self.form_class(request.POST)
		perfil = get_perfil_logado(request)

		if (form.is_valid(perfil.id)) :
			dados = form.cleaned_data

			perfil.usuario.set_password(dados['nova_senha'])
			perfil.usuario.save()

			return redirect('index')

		return render(request, 'alterarSenha.html', {'form': form})

class RecuperarSenha(View):
	form_class = RecuperarSenha
	def get(self, request):
		return render(request, 'recuperarSenha.html')

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)

		if (form.is_valid()):
			dados = form.cleaned_data

			perfil = Perfil.objects.filter(nome = dados['nome'],
										   telefone= dados['telefone'],
										   nome_empresa= dados['nome_empresa'],
										   pergunta=dados['pergunta'],
										   resposta=dados['resposta'])

			perfil_alterar(perfil[0])

			return redirect('recuperarSenhaUsuario')

		return render(request, 'recuperarSenha.html', {'form': form})



class RecuperarSenhaUsuario(View):
	form_class = RecuperarSenhaUsuario
	def get(self, request):
		return render(request, 'recuperarSenhaUsuario.html', )

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)

		if (form.is_valid()):
			dados = form.cleaned_data
			recuperarSenha(dados['nova_senha'])
			return redirect('index')

		return render(request, 'recuperarSenha.html', {'form': form})

def perfil_alterar(perfil2):
	global perfilParaAlterar
	perfilParaAlterar = perfil2

def recuperarSenha(senha):
	print(perfilParaAlterar.nome)
	perfilParaAlterar.usuario.set_password(senha)
	perfilParaAlterar.usuario.save()


