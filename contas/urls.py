from django.urls import path

from .views import (
login_page,
cadastro_page,
RegisterView
)

urlpatterns = [

path(
    '',
    login_page,
    name='login'
),

path(
    'cadastro/',
    cadastro_page,
    name='cadastro'
),

path(
    'api/auth/register/',
    RegisterView.as_view(),
    name='register'
),

]
