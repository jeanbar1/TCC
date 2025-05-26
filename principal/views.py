from django.shortcuts import render

def home(request):
    """
    View simples para a página inicial
    """
    return render(request, 'principal/home.html')