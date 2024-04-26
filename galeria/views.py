#esse arquivo é o arquivo de configuração do django e mostra como o django está configurado para rodar a aplicação
#ele é um arquivo de configuração do django e é onde se configura o banco de dados, as senhas, as urls, os templates, etc
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'galeria/index.html')

def imagem (request):
    return render(request,'galeria/imagem.html')