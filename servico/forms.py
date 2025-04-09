from django import forms
from django.forms import ModelForm
from .models import Servico


class ServicoForm(ModelForm):
    class Meta:
        model = Servico
        fields = ['nome', 'endereco', 'anaminese', 'descricao', 'telefone']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'digite o nome do servico aqui'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'digite o endereco do servico aqui'}),
            'anaminese': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'descricao': forms.Textarea(attrs={'class': 'form-check-text'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'digite o telefone do servico aqui'}),
        }