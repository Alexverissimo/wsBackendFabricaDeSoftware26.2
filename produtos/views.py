from rest_framework import generics

from .models import Produto
from .serializers import ProdutoSerializer


class ProdutoListView(generics.ListAPIView):

    queryset = Produto.objects.select_related(
        'categoria'
    ).all()

    serializer_class = ProdutoSerializer


class ProdutoDetailView(generics.RetrieveAPIView):

    queryset = Produto.objects.select_related(
        'categoria'
    ).all()

    serializer_class = ProdutoSerializer