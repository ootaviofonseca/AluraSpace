#esse arquivo é o arquivo de configuração do django e mostra como o django está configurado para rodar a aplicação
#ele é um arquivo de configuração do django e é onde se configura o banco de dados, as senhas, as urls, os templates, etc
from django.shortcuts import get_object_or_404, render
from galeria.models import Fotografia



def index(request):
    fotografias = Fotografia.objects.all() #pega todas as fotografias do banco de dados e coloca na variável fotografias
    return render(request,'galeria/index.html', {"cards": fotografias})

def imagem (request,foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id) #pega a fotografia com o id passado na url
    return render(request,'galeria/imagem.html',{"fotografia":fotografia}) #retorna a página imagem.html com a fotografia passada como contexto