from django.urls import path

from .views import (
    ProdutoListView,
    ProdutoDetailView
)


urlpatterns = [

    path(
        '',
        ProdutoListView.as_view(),
        name='produtos-list'
    ),

    path(
        '<int:pk>/',
        ProdutoDetailView.as_view(),
        name='produto-detail'
    ),

]