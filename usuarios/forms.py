from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.password_validation import validate_password
from .models import Usuario


class PhoneLoginForm(AuthenticationForm):
    """Formulário personalizado para login com telefone"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Personaliza os campos
        self.fields['username'].label = 'Telefone'
        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '(99) 99999-9999'
        })
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Digite sua senha'
        })
class AutonomoSignUpForm(UserCreationForm):
    nome      = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}))
    telefone  = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(99) 99999-9999'}))
    email     = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'seu@email.com'}))
    cpf       = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.000.000-00'}))
    password1 = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Crie uma senha forte'}), help_text="Mínimo de 8 caracteres com letras e números.")
    password2 = forms.CharField(label="Confirmação de senha", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repita a mesma senha'}))

    class Meta:
        model  = Usuario
        fields = ['username', 'nome', 'telefone', 'email', 'cpf']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['username'].widget   = forms.HiddenInput()

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        return cpf.replace('.', '').replace('-', '')

class ClienteSignUpForm(UserCreationForm):
    nome      = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}))
    telefone  = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(99) 99999-9999'}))
    password1 = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Crie uma senha forte'}), help_text="Mínimo de 8 caracteres com letras e números.")
    password2 = forms.CharField(label="Confirmação de senha", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repita a mesma senha'}))

    class Meta:
        model  = Usuario
        fields = ['username', 'email', 'nome', 'telefone']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['username'].widget   = forms.HiddenInput()
        self.fields['email'].required    = False
        self.fields['email'].widget      = forms.HiddenInput()

class UsuarioForm(forms.ModelForm):
    nome     = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email    = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    cpf      = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model  = Usuario
        fields = ['nome', 'telefone', 'email', 'cpf']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.is_cliente():
            self.fields.pop('email', None)
            self.fields.pop('cpf', None)

class PasswordChangeForm(PasswordChangeForm):
    old_password  = forms.CharField(label="Senha atual", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label="Nova senha", widget=forms.PasswordInput(attrs={'class': 'form-control'}), help_text="Mínimo de 8 caracteres com letras e números.")
    new_password2 = forms.CharField(label="Confirmação da nova senha", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
