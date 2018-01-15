# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from perfis.views import *

class RegistrarUsuarioForm(forms.Form):
	nome = forms.CharField(required=True)
	email = forms.EmailField(required=True)	
	senha = forms.CharField(required=True)
	telefone = forms.CharField(required=True)
	nome_empresa = forms.CharField(required=True)
	administrador = forms.CharField(required=False)
	pergunta = forms.CharField(required=True)
	resposta = forms.CharField(required=False)

	def is_valid(self): 
		valid = True

		if not super(RegistrarUsuarioForm, self).is_valid():
			self.adiciona_erro('Por favor, verifique os dados informados')
			valid = False

		user_exists = User.objects.filter(email=self.cleaned_data['email']).exists()

		if user_exists:
			self.adiciona_erro('Usuario já existente')
			valid = False
			
		return valid

	def adiciona_erro(self, message):
		errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		errors.append(message)

class AlterarSenha(forms.Form):
	senha = forms.CharField(required=True)
	nova_senha = forms.CharField(required=True)
	confirmar_senha = forms.CharField(required=True)

	def is_valid(self, id):
		valid = True

		if not super(AlterarSenha, self).is_valid():
			self.adiciona_erro('Por favor, verifique os dados informados')
			valid = False

		perfil = Perfil.objects.get(id = id)
		if (not perfil.usuario.check_password(self.cleaned_data['senha'])):
			self.adiciona_erro('Senha incorreta!')
			valid = False

		if (self.cleaned_data['nova_senha'] != self.cleaned_data['confirmar_senha']):
			self.adiciona_erro('A senha nova é diferenta da senha de confirmação')
			valid = False

		return valid

	def adiciona_erro(self, message):
		errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		errors.append(message)

class RecuperarSenha(forms.Form):
	nome = forms.CharField(required=True)
	telefone = forms.CharField(required=True)
	nome_empresa = forms.CharField(required=True)
	pergunta = forms.CharField(required=True)
	resposta = forms.CharField(required=True)

	def is_valid(self):
		valid = True

		if not super(RecuperarSenha, self).is_valid():
			self.adiciona_erro('Por favor, verifique os dados informados')
			valid = False

		perfil = Perfil.objects.filter(nome =self.cleaned_data['nome'],
									   telefone = self.cleaned_data['telefone'],
									   nome_empresa = self.cleaned_data['nome_empresa'],
									   pergunta=self.cleaned_data['pergunta'],
									   resposta=self.cleaned_data['resposta'])

		if (not perfil):
			self.adiciona_erro('Os dados digitados estão incorretos!')
			valid = False

		return valid

	def adiciona_erro(self, message):
		errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		errors.append(message)

class RecuperarSenhaUsuario(forms.Form):
	nova_senha = forms.CharField(required=True)
	confirmar_senha = forms.CharField(required=True)

	def is_valid(self):
		valid = True

		if not super(RecuperarSenhaUsuario, self).is_valid():
			self.adiciona_erro('Por favor, verifique os dados informados')
			valid = False

		if (self.cleaned_data['nova_senha'] != self.cleaned_data['confirmar_senha']):
			self.adiciona_erro('A senha nova é diferenta da senha de confirmação')
			valid = False

		return valid

	def adiciona_erro(self, message):
		errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		errors.append(message)