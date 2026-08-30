from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    ProdutoListView,
    ProdutoDetailView,
    ProdutoViewSet,
    produtos_page,
    carrinho_page,
    CarrinhoView,
    AdicionarCarrinhoView,
    RemoverItemCarrinhoView,
    AlterarQuantidadeCarrinhoView,
    FinalizarCompraView
)


router = DefaultRouter()

router.register(
    'crud',
    ProdutoViewSet,
    basename='produto'
)


urlpatterns = [
    path(
        '',
        ProdutoListView.as_view(),
        name='produtos-list'
    ),

    path(
        'pagina/',
        produtos_page,
        name='produtos-page'
    ),

    path(
        'carrinho/',
        CarrinhoView.as_view(),
        name='carrinho'
    ),

    path(
        'carrinho/adicionar/',
        AdicionarCarrinhoView.as_view(),
        name='carrinho-adicionar'
    ),

    path(
        'carrinho/pagina/',
        carrinho_page,
        name='carrinho-page'
    ),

    path(
        'carrinho/item/<int:item_id>/remover/',
        RemoverItemCarrinhoView.as_view(),
        name='carrinho-remover'
    ),

    path(
        'carrinho/item/<int:item_id>/quantidade/',
        AlterarQuantidadeCarrinhoView.as_view(),
        name='carrinho-quantidade'
    ),

    path(
        'checkout/',
        FinalizarCompraView.as_view(),
        name='checkout'
    ),

    path(
        '<int:pk>/',
        ProdutoDetailView.as_view(),
        name='produto-detail'
    ),

    path(
        '',
        include(router.urls)
    ),
]