from django import forms


class Publicar(forms.Form):
	postagem = forms.CharField(required=True)
	imagem = forms.ImageField(required=False)
	def is_valid(self,request):
		valid = True

		if not super(Publicar, self).is_valid():
			self.adiciona_erro('Escreva alguma coisa')
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

class AlterarPubicacao(forms.Form):
	postagem_id = forms.IntegerField(required=True)
	postagem = forms.CharField(required=True)
	def is_valid(self,request):
		valid = True

		if not super(AlterarPubicacao, self).is_valid():
			self.adiciona_erro('Escreva alguma coisa')
			valid = False

		return valid

	def adiciona_erro(self, message):
		errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		errors.append(message)