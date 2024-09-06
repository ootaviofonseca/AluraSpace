#esse arquivo é o arquivo de configuração do django e mostra como o django está configurado para rodar a aplicação
#ele é um arquivo de configuração do django e é onde se configura o banco de dados, as senhas, as urls, os templates, etc
from django.shortcuts import get_object_or_404, render, redirect
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForm

from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar essa página')
        return redirect('login')
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True) #pega todas as fotografias que estão publicadas (publicada = True
    return render(request,'galeria/index.html', {"cards": fotografias})

def imagem (request,foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id) #pega a fotografia com o id passado na url
    return render(request,'galeria/imagem.html',{"fotografia":fotografia}) #retorna a página imagem.html com a fotografia passada como contexto

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado buscar')
        return redirect('login')
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if 'buscar' in request.GET:
        nome_buscar = request.GET['buscar']
        if nome_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_buscar)

    return render(request,'galeria/index.html',{"cards":fotografias}) #retorna a página buscar.html

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar essa página')
        return redirect('login')
    
    form =  FotografiaForm(request.POST or None, request.FILES or None) 
    if request.method == 'POST':
        form = FotografiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem cadastrada com sucesso')
            return redirect('index')
    return render(request,'galeria/nova_imagem.html', {'form': form}) #retorna a página nova_imagem.html

def editar_imagem(request,foto_id):
    
    fotografia = Fotografia.objects.get(id=foto_id) #pega a fotografia com o id passado na url
    form = FotografiaForm( instance=fotografia) #passa a fotografia como instância do form
    if request.method == 'POST':
        form = FotografiaForm(request.POST, request.FILES, instance=fotografia) #passa a fotografia como instância do form
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem editada com sucesso')
            return redirect('index')
    return render(request,'galeria/editar_imagem.html',{"form":form, 'foto_id':foto_id}) #retorna a página editar_imagem.html com a fotografia passada como contexto

def deletar_imagem(request,foto_id):
    
    fotografia =Fotografia.objects.get(id=foto_id) 
    fotografia.delete() #deleta a fotografia
    messages.success(request, 'Imagem deletada com sucesso')
    return redirect('index') #redireciona para a página inicial

def filtro(request,categoria):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True, categoria = categoria) #pega todas as fotografias que estão publicadas (publicada = True)
    return render(request,'galeria/index.html',{"cards":fotografias})