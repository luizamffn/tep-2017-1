from django.shortcuts import render
from perfis.models import *
from perfis.views import *
from postagens.forms import *


# Create your views here.

class Publicar(View):
	form_class = Publicar
	def get(self, request):
		pass

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST, request.FILES)

		if (form.is_valid(request)):
			dados = form.cleaned_data
			p = Postagem(descricao = dados['postagem'], perfil = get_perfil_logado(request), data = datetime.now())
			p.save()

			# if dados['imagem'] is not None:
			p.imagem = dados['imagem']
			p.save()
			return redirect('index')

		return render(request, 'funcionarios.html', {'perfil_logado':get_perfil_logado(request),'form': form})

@login_required
def ExcluirPublicacao(request, publicacao_id):
	p = Postagem.objects.get(id = publicacao_id)
	p.excluirPublicacao()
	return redirect('index')

def EditarPublicacao(request, publicacao_id):
	postagem = Postagem.objects.get(id = publicacao_id)
	descricao = postagem.descricao
	return render(request, 'editarPostagem.html', {'perfil_logado':get_perfil_logado(request),
												   'descricao': descricao,
												   'postagem_id':publicacao_id})

class SalvarAlteracao(View):
	form_class = AlterarPubicacao

	def get(self, request):
		pass

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)

		if (form.is_valid(request)):
			dados = form.cleaned_data
			p = Postagem.objects.get(id=dados['postagem_id'])
			print(p)
			p.descricao = dados['postagem']
			p.save()

			return redirect('index')

		return render(request, 'funcionarios.html', {'perfil_logado': get_perfil_logado(request), 'form': form})
