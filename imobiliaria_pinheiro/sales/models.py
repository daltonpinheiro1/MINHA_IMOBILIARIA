
from django.db import models


class Imovel(models.Model):
    titulo = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='imoveis/')

    def __str__(self):
        return self.titulo
