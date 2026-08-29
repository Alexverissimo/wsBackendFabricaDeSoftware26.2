import requests
from django.db import transaction

from .models import Categoria, Produto

API_URL = 'https://dummyjson.com/products'


def buscar_produtos_api():
    try:
        response = requests.get(
            API_URL,
            timeout=10
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.Timeout as err:
        raise Exception(
            'A API externa demorou muito para responder.'
        ) from err

    except requests.exceptions.ConnectionError as err:
        raise Exception(
            'Não foi possível conectar com a API externa.'
        ) from err

    except requests.exceptions.HTTPError as err:
        status = (
            err.response.status_code
            if err.response is not None
            else 'Desconhecido'
        )
        raise Exception(
            f'Erro HTTP na API externa: {status}'
        ) from err

    except requests.exceptions.RequestException as err:
        raise Exception(
            'Erro ao consumir a API externa.'
        ) from err


def sincronizar_produtos():
    data = buscar_produtos_api()
    produtos = data.get('products', [])

    with transaction.atomic():
        for item in produtos:
            categoria, _ = Categoria.objects.get_or_create(
                nome=item['category']
            )

            Produto.objects.update_or_create(
                id_externo=item['id'],
                defaults={
                    'nome': item['title'],
                    'descricao': item['description'],
                    'preco': item['price'],
                    'estoque': item['stock'],
                    'imagem': item['thumbnail'],
                    'categoria': categoria,
                }
            )

    return len(produtos)