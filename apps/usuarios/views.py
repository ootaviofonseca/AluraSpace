from django.shortcuts import render, redirect

from apps.usuarios.forms import LoginForms, CadastroForms

from django.contrib.auth.models import User

from django.contrib import auth

from django.contrib import messages

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form['username'].value()
            senha = form['senha'].value()

            usuario = auth.authenticate(username=nome, password=senha) 
            #verifica se o usuario existe e se a senha está correta

            if usuario is not None:
                auth.login(request, usuario)
                mensagem = messages.success(request, f'{nome} Seja Bem Vindo!')
                return redirect('index')
                
            else:
                mensagem = messages.error(request, 'Usuário ou senha inválidos')
                return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            
            nome=form['nomeCadastro'].value()
            email=form['emailCadastro'].value()
            senha=form['senhaCadastro'].value()

            if User.objects.filter(username=nome).exists():
                mensagem = messages.error(request, 'Esse usuário já existe!')
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            mensagem = messages.success(request, f'{nome} cadastrado com sucesso!')
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Deslogado com sucesso!')
    return redirect('login')