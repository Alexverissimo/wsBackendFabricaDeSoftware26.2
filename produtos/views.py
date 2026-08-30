from rest_framework import generics, viewsets, filters
from django.shortcuts import render

from .models import Produto
from .serializers import ProdutoSerializer


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