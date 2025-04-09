from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User


from .models import *
from .forms import *


def addServico(request):
    if request.method == "POST":
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/servico/")
        else:
            return render(request, "addServico.html", {"form" : form, 'titulo' : "Criar serviço"})
    else:
        form = ServicoForm()
        return render(request, "addServico.html", {"form": form, 'titulo': "Criar serviço"})


def editServico(request, id):
    servico = Servico.objects.get(id=id)
    print(servico)
    
    if request.method == "POST":
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            return redirect('/servico/')
    
    else:       
        form = ServicoForm(instance=servico)
    return render(request, 'editServico.html', {'form': form, 'titulo': 'Editar serviço'})


def deleteServico(request, id):
    servico = Servico.objectss.filter(id=id).first()
    
    if not servico:
        messages.error(request, 'serviço não encontrado')
        return redirect("listServico")
    
    servico.delete()
    return redirect("listServico")

def listServico(request, id=None):
    if id:
        if not request.user.is_superuser and id != request.user.id:
            return redirect('listServico', request.user.id)
            
        user = get_object_or_404(User, id=id)
        servico = Servico.objectss.filter(cliente=user)
    
    elif request.user.is_superuser:
        servico = Servico.objectss.all()
        
    else:
        redirect('listServico', request.user.id)
    return render(request, 'servico/listServico.html', {'servico': servico})
