from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group

from django.shortcuts import render, get_object_or_404, redirect

from principal.decorators import group_required
from .models import *
from .forms import *


def addUser(request):
    if request.method == "POST":
        form = UsuarioFormSing(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.set_password(request.POST.get('password1'))
            user.save()
            
            login(request, user)
            group, created = Group.objects.get_or_create(name= 'Clientes')
            
            user.groups.add(group)
            return redirect('home')
        else:
            return render(request, "user/add.html", {"form" : form, 'titulo': "Criar Usuario"})
    else:
        form = UsuarioFormSing()
        return render(request, "user/add.html", {"form" : form, 'titulo': "Criar Usuario"})
    
@login_required
def editUser(request, id):
    if not request.user.is_superuser and  id != request.user.id:
        return redirect ('perfilUser')
    
    usuario = Usuario.objects.filter(id = id).first()
    
    if request.method == 'POST':
         form = UsuarioForm(request.POST, request.FILES, instance=usuario)
         
         if form.is_valid():
            user = form.save()
             
            if request.user.id == usuario.id:
                login(request, user)
            return redirect('perfilUser', id=id)
    else:
        form = UsuarioForm(instance=usuario)
    context = {'form' : form, 'titulo': 'Editar Usuario'}
    return render(request, 'edit.html', context)

@login_required
def deleteUser(request, id):
    usuario = Usuario.objects.filter(id = id).first()
    if usuario: usuario.delete()
    return redirect('listUser')

@login_required
def profile(request, id=None):
    if not request.user.is_superuser and id  is not None and id != request.user.id:
        return redirect('profileUser')
    
    
    user=None
    if id:
      user = get_object_or_404(Usuario, id=id)
    else:
        user = request.user
    form = UsuarioForm(instance=user)

    return render(request, 'user/profile.html', {'form': form, 'user':user, 'titulo': 'Perfil do Usuario'})


@login_required
def muda_tipo(request, id):
    if request.method =='POST':
        tipo = request.POST.get('tipo', "Clientes")
        user = get_object_or_404(Usuario, id=id)
        
        if tipo == "CLIENTE":
            user.groups.clear()
            user.is_superuser = False
            user.tipo_cliente = tipo
            group, created = Group.objects.get_or_create(name='Clientes')
            user.groups.add(group)
            
        elif tipo == "ALOCADOR":
            user.groups.clear()
            user.is_superuser = True
            user.tipo_cliente = tipo
            group, created = Group.objects.get_or_create(name='ALOCADOR')
            user.groups.add(group)
        
        user.save()
        messages.success(request, f"Tipo de usuário alterado com sucesso para {Usuario.TIPOS_CLIENTE_DICT[tipo]}.")
        
    return redirect('profileUser', id=id)

@login_required
def listUser(request):
    usuarios = Usuario.objects,all()
    return render(request, 'user/listUser.html', {'usuarios': usuarios})