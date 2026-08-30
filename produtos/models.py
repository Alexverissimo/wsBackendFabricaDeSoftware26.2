from django.db import models
from django.contrib.auth.models import User


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


class Carrinho(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='carrinho'
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'Carrinho de {self.usuario.username}'


class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(
        Carrinho,
        on_delete=models.CASCADE,
        related_name='itens'
    )

    produto = models.ForeignKey(
        Produto,
        on_delete=models.CASCADE
    )

    quantidade = models.PositiveIntegerField(
        default=1
    )

    def __str__(self):
        return f'{self.produto.nome} - {self.quantidade}'


class Pedido(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='pedidos'
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return f'Pedido #{self.id} - {self.usuario.username}'


class ItemPedido(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name='itens'
    )

    produto = models.ForeignKey(
        Produto,
        on_delete=models.PROTECT
    )

    quantidade = models.PositiveIntegerField()

    preco_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f'{self.produto.nome} - {self.quantidade}'