from django import forms
from projeto.models import *

class CadastrarProjeto(forms.Form):
    nome = forms.CharField(required=True)
    descricao = forms.CharField(required=True)

    def is_valid(self):
        valid = True

        if not super(CadastrarProjeto, self).is_valid():
            self.adiciona_erro('Preencha todos os campos')
            valid = False

        return valid

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)

class CadastrarPessoa(forms.Form):
    nome = forms.CharField(required=True)
    salario = forms.FloatField(required=True)
    funcao = forms.CharField(required=True)

    def is_valid(self):
        valid = True

        if not super(CadastrarPessoa, self).is_valid():
            self.adiciona_erro('Preencha todos os campos')
            valid = False

        return valid

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)

class CadastrarAtividade(forms.Form):
    nome = forms.CharField(required=True)
    descricao = forms.CharField(required=True)
    dataInicio = forms.DateField(required=False)
    dataFim = forms.DateField(required=False)
    projeto = forms.IntegerField()
    responsavel = forms.IntegerField()

    def is_valid(self):
        valid = True

        if not super(CadastrarAtividade, self).is_valid():
            self.adiciona_erro('Preencha todos os campos')
            valid = False

        return valid

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)


