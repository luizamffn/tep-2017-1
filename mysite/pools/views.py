from django.shortcuts import render, redirect

from .models import *

# Create your views here.
def index(request):
    questoes = Question.objects.order_by('pub_date')
    return render(request, 'index.html', {"questions": questoes})

def question(request, question_id):
    question= Question.objects.get(id = question_id)
    return render(request, 'question.html', {'question': question})

def resultados(request, question_id):
    question= Question.objects.get(id = question_id)
    choices = Choice.objects.filter(question = question)
    count = 0
    for c in choices:
        count = count + c.votes

    return render(request, 'resultado.html', {'question': question, 'total': count})

def votar(request, choice_id):
    choice = Choice.objects.get(id = choice_id)
    choice.votar()
    return redirect('index')

def manage(request, question_id):
    question= Question.objects.get(id = question_id)
    return render(request, 'manage.html', {'question': question})

def remover(request, choice_id):
    choice = Choice.objects.get(id = choice_id)
    choice.remover()
    return redirect('manage', question_id=choice.question.id)

def abirStatus(request, question_id):
    question= Question.objects.get(id = question_id)
    question.alterarStatus(False)
    return redirect('manage', question_id=question.id)

def fecharStatus(request, question_id):
    question= Question.objects.get(id = question_id)
    question.alterarStatus(True)
    return redirect('manage', question_id=question.id)