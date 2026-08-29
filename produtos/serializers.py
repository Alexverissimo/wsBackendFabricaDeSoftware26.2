from rest_framework import serializers

from .models import Categoria, Produto


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = [
            'id',
            'nome',
        ]


class ProdutoSerializer(serializers.ModelSerializer):

    categoria = CategoriaSerializer(read_only=True)

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
        ]