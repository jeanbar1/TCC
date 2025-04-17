from django.db import models

class Servico(models.Model):
    nome = models.CharField(max_length=500)
    endereco = models.CharField(max_length=250)
    anamnese_obrigatoria = models.BooleanField(default=False)
    descricao = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15, blank=True)
    duracao_minutos = models.PositiveIntegerField(default=60)
    
    def __str__(self): 
        return self.nome

