# wsBackendFabricaDeSoftware26.2

Projeto desenvolvido em Django com Django REST Framework para gerenciamento de produtos, autenticação de usuários, carrinho de compras e finalização de pedidos.

## Tecnologias utilizadas

- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite
- Bootstrap
- JavaScript
- DummyJSON API

## Funcionalidades

- Cadastro de usuário
- Login com JWT
- Rota protegida para usuário autenticado
- Listagem de produtos
- Busca de produtos
- CRUD de produtos
- Consumo de API externa
- Sincronização de produtos com a API externa
- Categorias relacionadas aos produtos
- Carrinho por usuário
- Adicionar produtos ao carrinho
- Alterar quantidade dos produtos
- Remover produtos do carrinho
- Cálculo de subtotal e total
- Finalização de compra
- Criação de pedidos
- Página Home
- Página de produtos
- Página do carrinho

## API externa

O projeto utiliza a API DummyJSON para obter produtos.

Endpoint utilizado:

```text
https://dummyjson.com/products
```

A aplicação possui tratamento de erros para situações como:

- Timeout
- Erro de conexão
- Erros HTTP
- Outros erros de requisição

## Relacionamentos

O projeto possui relacionamentos entre diferentes entidades.

Exemplo entre categoria e produto:

```text
Categoria
    |
    | 1:N
    |
Produto
```

Relacionamento do carrinho:

```text
Usuário
    |
    | 1:1
    |
Carrinho
    |
    | 1:N
    |
ItemCarrinho
```

Relacionamento dos pedidos:

```text
Usuário
    |
    | 1:N
    |
Pedido
    |
    | 1:N
    |
ItemPedido
```

## Instalação

Clone o repositório:https://github.com/Alexverissimo/wsBackendFabricaDeSoftware26.2

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd wsBackendFabricaDeSoftware26.2
```

Crie o ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual no Windows:

```bash
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute as migrations:

```bash
python manage.py migrate
```

Inicie o servidor:

```bash
python manage.py runserver
```

A aplicação ficará disponível em:

```text
http://127.0.0.1:8000/
```

## Principais páginas

### Login

```text
http://127.0.0.1:8000/
```

### Cadastro

```text
http://127.0.0.1:8000/cadastro/
```

### Home

```text
http://127.0.0.1:8000/home/
```

### Produtos

```text
http://127.0.0.1:8000/api/produtos/pagina/
```

### Carrinho

```text
http://127.0.0.1:8000/api/produtos/carrinho/pagina/
```

## Principais endpoints

### Autenticação

Obter token:

```text
POST /api/auth/token/
```

Atualizar token:

```text
POST /api/auth/token/refresh/
```

Consultar usuário autenticado:

```text
GET /api/auth/me/
```

Cadastrar usuário:

```text
POST /api/auth/register/
```

### Produtos

Listar produtos:

```text
GET /api/produtos/
```

Buscar produtos:

```text
GET /api/produtos/?search=produto
```

Detalhes de um produto:

```text
GET /api/produtos/<id>/
```

CRUD de produtos:

```text
GET /api/produtos/crud/
POST /api/produtos/crud/
GET /api/produtos/crud/<id>/
PUT /api/produtos/crud/<id>/
PATCH /api/produtos/crud/<id>/
DELETE /api/produtos/crud/<id>/
```

### Carrinho

Visualizar carrinho:

```text
GET /api/produtos/carrinho/
```

Adicionar produto ao carrinho:

```text
POST /api/produtos/carrinho/adicionar/
```

Alterar quantidade:

```text
PATCH /api/produtos/carrinho/item/<id>/quantidade/
```

Remover item:

```text
DELETE /api/produtos/carrinho/item/<id>/remover/
```

### Checkout

Finalizar compra:

```text
POST /api/produtos/checkout/
```

## Autenticação

As rotas protegidas utilizam autenticação JWT.

O token de acesso deve ser enviado no header da requisição:

```text
Authorization: Bearer SEU_TOKEN
```

## Banco de dados

O projeto utiliza SQLite como banco de dados.

Arquivo:

```text
db.sqlite3
```

## Estrutura principal

```text
wsBackendFabricaDeSoftware26.2/
│
├── configs/
├── contas/
├── produtos/
├── templates/
│   ├── contas/
│   └── itens/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Autor

Projeto desenvolvido por Alex para a de Fábrica de Software.