from rest_framework import serializers

from .models import (
    Categoria,
    Produto,
    Carrinho,
    ItemCarrinho
)


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = [
            'id',
            'nome'
        ]


class ProdutoSerializer(serializers.ModelSerializer):

    categoria = serializers.PrimaryKeyRelatedField(
        queryset=Categoria.objects.all(),
        write_only=True
    )

    categoria_detalhes = CategoriaSerializer(
        source='categoria',
        read_only=True
    )

    class Meta:
        model = Produto
        fields = [
            'id',
            'id_externo',
            'nome',
            'descricao',
            'preco',
            'estoque',
            'imagem',
            'categoria',
            'categoria_detalhes'
        ]


class ItemCarrinhoSerializer(serializers.ModelSerializer):

    produto_detalhes = ProdutoSerializer(
        source='produto',
        read_only=True
    )

    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = ItemCarrinho
        fields = [
            'id',
            'produto',
            'produto_detalhes',
            'quantidade',
            'subtotal'
        ]

    def get_subtotal(
        self,
        obj
    ):
        return obj.produto.preco * obj.quantidade


class CarrinhoSerializer(serializers.ModelSerializer):

    itens = ItemCarrinhoSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Carrinho
        fields = [
            'id',
            'usuario',
            'criado_em',
            'itens'
        ]

        read_only_fields = [
            'usuario'
        ]