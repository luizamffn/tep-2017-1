from django import forms

class DesativarPerfil(forms.Form):
	justificativa = forms.CharField(required=True)

	def is_valid(self):
		valid = True

		if not super(DesativarPerfil, self).is_valid():
			self.adiciona_erro('Por favor, informe a justificativa')
			valid = False

		return valid

	def adiciona_erro(self, message):
		errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		errors.append(message)

class BuscarUsuario(forms.Form):
	nome = forms.CharField(required=True)

	def is_valid(self):
		valid = True

		if not super(BuscarUsuario, self).is_valid():
			self.adiciona_erro('Por favor, informe o nome do usuário')
			valid = False

		return valid

	def adiciona_erro(self, message):
		errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		errors.append(message)

class AlterarImagemPerfil(forms.Form):
	imagem = forms.ImageField(required=True)

	def is_valid(self, request):
		valid = True

		if not super(AlterarImagemPerfil, self).is_valid():
			self.adiciona_erro('Por favor, carregue a imagem')
			valid = False

		if 'imagem' in request.FILES and (request.FILES['imagem'] is not None or request.FILES['imagem'] is not ''):
			imagem = request.FILES['imagem']

			main, sub = imagem.content_type.split('/')
			if not (main == 'image' and sub in ['jpeg', 'jpg', 'png']):
				self.adiciona_erro('Formato de imagem inválido')
				valid = False

		return valid

	def adiciona_erro(self, message):
		errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		errors.append(message)