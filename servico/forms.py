# servico/forms.py
from django import forms
from .models import Servico, Anamnese, Pergunta, OpcaoPergunta

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['nome', 'endereco', 'anamnese_obrigatoria', 'descricao', 'telefone', 'duracao_minutos']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'duracao_minutos': forms.NumberInput(attrs={'class': 'form-control'}),
        }