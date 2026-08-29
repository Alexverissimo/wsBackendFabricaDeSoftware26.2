from django.db import models


class Categoria(models.Model):

    nome = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.nome


class Produto(models.Model):

    id_externo = models.IntegerField(
        unique=True
    )

    nome = models.CharField(
        max_length=200
    )

    descricao = models.TextField()

    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    estoque = models.IntegerField(
        default=0
    )

    imagem = models.URLField()

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='produtos'
    )

    def __str__(self):
        return self.nome