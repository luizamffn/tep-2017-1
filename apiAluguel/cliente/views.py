from django.shortcuts import render, redirect

# Create your views here.
def base(request):
    return render(request, 'base_not_auth.html')

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def generos(request):
    return render(request, 'generos.html')

def filmes(request):
    return render(request, 'filmes.html')

def filmes_not_auth(request):
    return render(request, 'filmes_not_auth.html')

def clientes(request):
    return render(request, 'clientes.html')

def alugueis(request):
    return render(request, 'alugueis.html')

def permission(request):
    return render(request, 'permission.html')