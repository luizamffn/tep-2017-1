from django.shortcuts import render, redirect
from projeto.forms import *
from projeto.models import *
from django.views.generic.base import View
from django.utils import timezone
from django.contrib.auth.decorators import login_required



# Create your views here.
# def index(request):
#     return render(request, 'index.html')

# def login(request):
#     return render(request, 'login.html')

@login_required
def projeto(request):
    projetos = Projeto.objects.filter(user = get_perfil_logado(request))
    return render(request, 'projeto.html', {'projetos':projetos,
                                            'user': get_perfil_logado(request)})

@login_required
def pessoa(request):
    responsaveis = Responsavel.objects.all()
    return render(request, 'pessoa.html', {'responsaveis':responsaveis,
                                           'user': get_perfil_logado(request)})

@login_required
def atividade(request):
    projetos = Projeto.objects.filter(user=get_perfil_logado(request))
    responsaveis = Responsavel.objects.all()
    atividades = Atividade.objects.filter(projeto__in = projetos)
    return render(request, 'atividade.html', {'projetos':projetos,
                                              'responsaveis' : responsaveis,
                                              'atividades': atividades,
                                              'user': get_perfil_logado(request)})

class CadastrarProjeto(View):
    form_class = CadastrarProjeto

    def get(self, request):
        return render(request, 'projeto.html')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        # perfil = get_perfil_logado(request)

        if (form.is_valid()):
            dados = form.cleaned_data

            projeto = Projeto(nome=dados['nome'],
                             descricao=dados['descricao'],
                             dataCadastro = timezone.localdate(),
                             user = get_perfil_logado(request))

            projeto.save()
            return redirect('projeto')

        return redirect('index')

class CadastrarPessoa(View):
    form_class = CadastrarPessoa

    def get(self, request):
        return render(request, 'pessoa.html')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if (form.is_valid()):
            dados = form.cleaned_data

            pessoa = Responsavel(nome=dados['nome'],
                             salario=dados['salario'],
                             funcao = dados['funcao'])

            pessoa.save()
            return redirect('pessoa')

        return redirect('index')

class CadastrarAtividade(View):
    form_class = CadastrarAtividade

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if (form.is_valid()):
            dados = form.cleaned_data

            projeto = Projeto.objects.get(id=dados['projeto'])
            responsavel = Responsavel.objects.get(id=dados['responsavel'])
            atividade = Atividade(nome=dados['nome'],
                               descricao=dados['descricao'],
                             dataInicio = dados['dataInicio'],
                             dataFim = dados['dataFim'],
                             projeto = projeto,
                            responsavel = responsavel)

            atividade.save()
            return redirect('atividade')

        return redirect('projeto')

@login_required
def get_perfil_logado(request):
    return request.user
