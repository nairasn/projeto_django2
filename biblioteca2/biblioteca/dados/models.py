from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    idade = models.IntegerField(blank=True, null=True)
    rg = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
        
    def __str__(self):
        return self.nome