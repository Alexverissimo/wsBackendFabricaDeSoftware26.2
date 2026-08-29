from django.contrib.auth.models import User
from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


def login_page(request):
    return render(request, 'contas/login.html')

def cadastro_page(request):
    return render(
        request,
        'contas/cadastro.html'
    )


class RegisterView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response(
                {'detail': 'Usuário e senha são obrigatórios.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(username=username).exists():
            return Response(
                {'detail': 'Usuário já existe.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        User.objects.create_user(
            username=username,
            password=password
        )

        return Response(
            {'detail': 'Usuário criado com sucesso.'},
            status=status.HTTP_201_CREATED
        )