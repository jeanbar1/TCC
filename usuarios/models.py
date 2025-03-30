from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    TIPOS_CLIENTE_DICT = {
        'CLIENTE ': 'cliente',
        'ALOCADOR': 'alocador',
    }
    TIPOS_CLIENTE = [
        ('CLIENTE', 'cliente'),
        ('ALOCADOR', 'alocador'),
    ]
    
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    tipo_cliente = models.CharField(max_length=20, choices=TIPOS_CLIENTE, default='CLIENTE')
    cpf = models.CharField(max_length=11, unique=True, blank=True, null=True)
    
    def __str__(self):
        return f"{self.id} - {self.username}"