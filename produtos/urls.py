from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    ProdutoListView,
    ProdutoDetailView,
    ProdutoViewSet
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
        '<int:pk>/',
        ProdutoDetailView.as_view(),
        name='produto-detail'
    ),

    path(
        '',
        include(router.urls)
    ),

]