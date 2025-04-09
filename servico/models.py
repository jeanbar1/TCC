from django.db import models

class Servico(models.Model):
    nome = models.CharField(max_length=500)
    endereco = models.CharField(max_length=250)
    anaminese = models.BooleanField()
    descricao = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15, blank=True)
    
    def __str__(self):
        return f'{self.nome}'    