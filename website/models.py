from django.db import models

# Create your models here.
class Contato(models.Model):
    email = models.EmailField()
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    mensagem = models.TextField()

    def __str__(self):
        return self.nome
