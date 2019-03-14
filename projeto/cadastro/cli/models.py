from django.db import models


#Admin superuser: admin: Deus / senha: superuser
# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=16)
    cep = models.CharField(max_length=11,null=False)
    endereco = models.CharField(max_length=100,null=False)
    numero = models.IntegerField(null=False)
    cidade = models.CharField(max_length=40,null=False)
    estado = models.CharField(max_length=30,null=False)
    pais = models.CharField(max_length=30,null=False)


    def __str__(self):
        return self.nome