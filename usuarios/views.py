from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group
from django.urls import reverse
from .forms import AutonomoSignUpForm, ClienteSignUpForm, PasswordChangeForm, PhoneLoginForm, UsuarioForm
from .models import Usuario

def home(request):
    """View para a página inicial"""
    context = {
        'titulo': 'Bem-vindo ao FlowAgenda',
        'mensagem': 'Sistema de agendamento inteligente'
    }
    return render(request, 'usuarios/home.html', context)


def user_login(request):
    """View personalizada para login com telefone"""
    
    # Se usuário já estiver autenticado, redireciona
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = PhoneLoginForm(request, data=request.POST)
        
        if form.is_valid():
            telefone = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Autentica usando o telefone como username
            user = authenticate(request, username=telefone, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f"Bem-vindo(a), {user.nome}!")
                return redirect('home')
            else:
                messages.error(request, "Telefone ou senha incorretos.")
        else:
            messages.error(request, "Por favor, corrija os erros abaixo.")
    else:
        form = PhoneLoginForm()
    
    return render(request, 'user/login.html', {'form': form})

def user_logout(request):
    """View para logout de usuários"""
    logout(request)
    messages.success(request, "Você foi desconectado com sucesso.")
    return redirect('home')


def escolher_tipo(request):
    """View para escolha inicial do tipo de cadastro"""
    return render(request, 'user/escolher_tipo.html')




def addUser(request):
    # Se já tiver escolhido o tipo (veio pela URL)
    user_type = request.GET.get('tipo', None)
    
    # Processar formulário enviado
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        
        if user_type == 'autonomo':
            form = AutonomoSignUpForm(request.POST)
        else:
            form = ClienteSignUpForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            if user_type == 'autonomo':
                messages.success(request, "Cadastro de autônomo realizado!")
                return redirect('home')
            else:
                messages.success(request, "Cadastro de cliente realizado!")
                return redirect('home')
    
    # Mostrar formulário de cadastro específico
    elif user_type in ['autonomo', 'cliente']:
        if user_type == 'autonomo':
            form = AutonomoSignUpForm()
        else:
            form = ClienteSignUpForm()
        
        return render(request, 'user/add.html', {
            'form': form,
            'user_type': user_type
        })
    
    # Mostrar tela de escolha inicial
    return render(request, 'user/escolher_tipo.html')







@login_required
def editUser(request, id):
    """View para edição de perfil de usuário"""
    usuario = get_object_or_404(Usuario, id=id)
    
    # Verifica permissões
    if not request.user.is_superuser and request.user.id != usuario.id:
        messages.error(request, "Você não tem permissão para editar este perfil.")
        return redirect('profile', id=request.user.id)
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect('profile', id=id)
    else:
        form = UsuarioForm(instance=usuario)
    
    return render(request, 'usuarios/edit.html', {'form': form, 'usuario': usuario})

@login_required
def deleteUser(request, id):
    """View para deletar usuário"""
    if not request.user.is_superuser:
        messages.error(request, "Você não tem permissão para esta ação.")
        return redirect('home')
    
    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    messages.success(request, "Usuário removido com sucesso.")
    return redirect('listUser')

@login_required
def profile(request, id=None):
    """View para visualização de perfil"""
    if id is None:
        return redirect('profile', id=request.user.id)
    
    usuario = get_object_or_404(Usuario, id=id)
    
    # Verifica se o usuário tem permissão para ver o perfil
    if not request.user.is_superuser and request.user.id != usuario.id:
        messages.warning(request, "Você só pode ver seu próprio perfil.")
        return redirect('profile', id=request.user.id)
    
    return render(request, 'usuarios/profile.html', {'usuario': usuario})

@login_required
def listUser(request):
    """View para listagem de usuários"""
    if not request.user.is_superuser:
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('home')
    
    usuarios = Usuario.objects.all().order_by('nome')
    return render(request, 'usuarios/list.html', {'usuarios': usuarios})

@login_required
def change_password(request):
    """View para alteração de senha"""
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Sua senha foi alterada com sucesso!')
            return redirect('profile')
        else:
            messages.error(request, 'Por favor corrija os erros abaixo.')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'usuarios/change_password.html', {
        'form': form,
        'titulo': 'Alterar senha'
    })