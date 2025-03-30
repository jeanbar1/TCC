from django import forms
from django.contrib.auth.forms import SetPasswordMixin
from .models import Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'telefone', 'cpf', 'endereco']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'digite seu usuario aqui'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'digite seu email aqui'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'digite seu telefone aqui'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'digite seu cpf aqui'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'digite seu endereco aqui'}),
        }
        
class UsuarioFormSing(forms.ModelForm):
    password1, password2 = SetPasswordMixin.create_password_fields()
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'telefone', 'cpf', 'endereco']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'digite seu usuario aqui'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'digite seu email aqui'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'digite seu telefone aqui'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'digite seu cpf aqui'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'digite seu endereco aqui'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'digite sua senha aqui'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'comfirme sua senha aqui'}),
        }