from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

class Usuario(AbstractUser):
    TIPOS_USUARIO = [
        ('AUTONOMO', 'autônomo'),
        ('CLIENTE', 'cliente'),
    ]
    
    # Mantenha todos os campos existentes
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15, unique=True)  # Agora será usado para login
    cpf = models.CharField(max_length=11, unique=True, blank=True, null=True)
    tipo_usuario = models.CharField(max_length=20, choices=TIPOS_USUARIO, default='CLIENTE')
    
    # Configuração para autenticação por telefone
    USERNAME_FIELD = 'telefone'  # Define que o telefone será usado para login
    REQUIRED_FIELDS = []  # Remove username dos campos obrigatórios
    
    # Remove campos não utilizados
    first_name = None
    last_name = None
    
    def save(self, *args, **kwargs):
        """Gera username automaticamente baseado no telefone"""
        if not self.username:
            # Cria um username baseado no telefone (remove caracteres não numéricos)
            telefone_limpo = ''.join(filter(str.isdigit, self.telefone))
            self.username = f"user_{telefone_limpo}"
            
            # Garante que o username é único
            counter = 1
            while Usuario.objects.filter(username=self.username).exists():
                self.username = f"user_{telefone_limpo}_{counter}"
                counter += 1
                
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.nome} ({self.telefone})"