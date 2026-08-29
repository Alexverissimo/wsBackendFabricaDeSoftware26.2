from django.urls import path

from .views import login_page, RegisterView

urlpatterns = [


path(
    '',
    login_page,
    name='login'
),

path(
    'api/auth/register/',
    RegisterView.as_view(),
    name='register'
),


]
