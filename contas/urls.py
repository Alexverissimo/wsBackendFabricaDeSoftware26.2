from django.urls import path

from .views import (
login_page,
cadastro_page,
home_page,
RegisterView,
MeView
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

path(
    'home/',
    home_page,
    name='home'
),
path(
'api/auth/me/',
MeView.as_view(),
name='me'
),


]
