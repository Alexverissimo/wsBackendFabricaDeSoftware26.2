from django.shortcuts import render

from rest_framework import (
    generics,
    viewsets,
    filters,
    status
)

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import (
    Produto,
    Carrinho,
    ItemCarrinho
)

from .serializers import (
    ProdutoSerializer,
    CarrinhoSerializer
)



class ProdutoListView(generics.ListAPIView):

    queryset = Produto.objects.select_related(
        'categoria'
    ).all()

    serializer_class = ProdutoSerializer

    filter_backends = [
        filters.SearchFilter
    ]

    search_fields = [
        'nome',
        'descricao',
    ]


class ProdutoDetailView(generics.RetrieveAPIView):

    queryset = Produto.objects.select_related(
        'categoria'
    ).all()

    serializer_class = ProdutoSerializer


class ProdutoViewSet(viewsets.ModelViewSet):

    queryset = Produto.objects.select_related(
        'categoria'
    ).all()

    serializer_class = ProdutoSerializer


def produtos_page(request):

    return render(
        request,
        'itens/produtos.html'
    )


def carrinho_page(request):

    return render(
        request,
        'itens/carrinho.html'
    )


class CarrinhoView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        carrinho, _ = Carrinho.objects.get_or_create(
            usuario=request.user
        )

        serializer = CarrinhoSerializer(
            carrinho
        )

        return Response(
            serializer.data
        )
    
class AdicionarCarrinhoView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):

        produto_id = request.data.get(
            'produto_id'
        )

        if not produto_id:

            return Response(
                {
                    'detail':
                    'produto_id é obrigatório.'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:

            produto = Produto.objects.get(
                id=produto_id
            )

        except Produto.DoesNotExist:

            return Response(
                {
                    'detail':
                    'Produto não encontrado.'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        carrinho, _ = Carrinho.objects.get_or_create(
            usuario=request.user
        )

        item, criado = ItemCarrinho.objects.get_or_create(
            carrinho=carrinho,
            produto=produto,
            defaults={
                'quantidade': 1
            }
        )

        if not criado:

            item.quantidade += 1

            item.save()

        serializer = CarrinhoSerializer(
            carrinho
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class RemoverItemCarrinhoView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def delete(
        self,
        request,
        item_id
    ):

        try:

            item = ItemCarrinho.objects.get(
                id=item_id,
                carrinho__usuario=request.user
            )

        except ItemCarrinho.DoesNotExist:

            return Response(
                {
                    'detail':
                    'Item não encontrado no carrinho.'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        item.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


class AlterarQuantidadeCarrinhoView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def patch(
        self,
        request,
        item_id
    ):

        quantidade = request.data.get(
            'quantidade'
        )

        try:

            quantidade = int(
                quantidade
            )

        except (
            TypeError,
            ValueError
        ):

            return Response(
                {
                    'detail':
                    'Quantidade inválida.'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if quantidade < 1:

            return Response(
                {
                    'detail':
                    'A quantidade deve ser maior que zero.'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:

            item = ItemCarrinho.objects.get(
                id=item_id,
                carrinho__usuario=request.user
            )

        except ItemCarrinho.DoesNotExist:

            return Response(
                {
                    'detail':
                    'Item não encontrado no carrinho.'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        item.quantidade = quantidade

        item.save()

        serializer = CarrinhoSerializer(
            item.carrinho
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )