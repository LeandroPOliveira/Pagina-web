from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForm, PerfilForm, NovaSenhaForm, UserInfoForm
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile


def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

            usuario = auth.authenticate(request, username=nome, password=senha)
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f'{nome} logado com sucesso!')
                return redirect('index')
            else:
                messages.error(request, 'Erro ao efetuar o login')
                return redirect('login')

    return render(request, 'usuarios/login.html', {"form": form})


def cadastro(request):
    form = CadastroForm()
    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            form.save()

            usuario = form.cleaned_data['username']
            password = form.cleaned_data['password1']


            if User.objects.filter(username=usuario).exists():
                messages.error(request, 'Usuário já cadastrado')
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )

            usuario.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form': form})


def perfil(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        current_profile = Profile.objects.get(usuario__id=request.user.id)
        user_form = PerfilForm(request.POST or None, instance=current_user)
        perfil_form = UserInfoForm(request.POST or None, instance=current_profile)

        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()

            login(request)
            messages.success(request, "User Has Been Updated!!")
            return redirect('index')
        return render(request, "usuarios/perfil.html", {'user_form': user_form, 'perfil_form': perfil_form})
    else:
        messages.success(request, "You Must Be Logged In To Access That Page!!")
        return redirect('index')


def nova_senha(request):
    if request.user.is_authenticated:
        current_user = request.user
        # Did they fill out the form
        if request.method == 'POST':
            form = NovaSenhaForm(current_user, request.POST)
            # Is the form valid
            if form.is_valid():
                form.save()
                messages.success(request, "Your Password Has Been Updated...")
                login(request)
                return redirect('nova_senha')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect('nova_senha')
        else:
            form = NovaSenhaForm(current_user)
            return render(request, "usuarios/nova-senha.html", {'form':form})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('index')


def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')
