"""
Exercício 2: API de Produtos (REST)
Testes para API https://fakestoreapi.com/
"""
import pytest
import requests


BASE_URL = "https://fakestoreapi.com"
CATEGORIAS_VALIDAS = ["electronics", "jewelery", "men's clothing", "women's clothing"]


@pytest.mark.api
def test_listar_todos_produtos():
    """Teste para listar todos os produtos"""
    response = requests.get(f"{BASE_URL}/products")
    
    assert response.status_code == 200
    produtos = response.json()
    assert len(produtos) > 0
    assert isinstance(produtos, list)
    
    # Verificar estrutura do primeiro produto
    produto = produtos[0]
    assert "id" in produto
    assert "title" in produto
    assert "price" in produto
    assert "category" in produto
    assert "description" in produto
    assert "image" in produto


@pytest.mark.api
def test_buscar_produto_por_id():
    """Teste para buscar produto específico por ID"""
    produto_id = 1
    response = requests.get(f"{BASE_URL}/products/{produto_id}")
    
    assert response.status_code == 200
    produto = response.json()
    assert produto["id"] == produto_id
    assert "title" in produto
    assert "price" in produto


@pytest.mark.api
@pytest.mark.parametrize("categoria", CATEGORIAS_VALIDAS)
def test_filtrar_produtos_por_categoria(categoria):
    """Teste para filtrar produtos por categoria"""
    response = requests.get(f"{BASE_URL}/products/category/{categoria}")
    
    assert response.status_code == 200
    produtos = response.json()
    assert len(produtos) > 0
    
    # Verificar que todos os produtos pertencem à categoria
    for produto in produtos:
        assert produto["category"] == categoria


@pytest.mark.api
def test_validar_schema_produto():
    """Teste para validar schema completo do produto"""
    response = requests.get(f"{BASE_URL}/products/1")
    
    assert response.status_code == 200
    produto = response.json()
    
    # Validar tipos de dados
    assert isinstance(produto["id"], int)
    assert isinstance(produto["title"], str)
    assert isinstance(produto["price"], (int, float))
    assert isinstance(produto["description"], str)
    assert isinstance(produto["category"], str)
    assert isinstance(produto["image"], str)
    assert isinstance(produto["rating"], dict)
    
    # Validar rating
    assert "rate" in produto["rating"]
    assert "count" in produto["rating"]
    assert isinstance(produto["rating"]["rate"], (int, float))
    assert isinstance(produto["rating"]["count"], int)


@pytest.mark.api
def test_limite_produtos_retornados():
    """Teste para verificar limite de produtos"""
    limite = 5
    response = requests.get(f"{BASE_URL}/products?limit={limite}")
    
    assert response.status_code == 200
    produtos = response.json()
    assert len(produtos) == limite


@pytest.mark.api
def test_ordenacao_produtos():
    """Teste para verificar ordenação de produtos"""
    response = requests.get(f"{BASE_URL}/products?sort=desc")
    
    assert response.status_code == 200
    produtos = response.json()
    
    # Verificar que IDs estão em ordem decrescente
    ids = [p["id"] for p in produtos]
    assert ids == sorted(ids, reverse=True)


@pytest.mark.api
def test_produto_inexistente():
    """Teste para buscar produto que não existe"""
    produto_id = 99999
    response = requests.get(f"{BASE_URL}/products/{produto_id}")
    
    # API retorna 200 com null ou objeto vazio
    assert response.status_code == 200


@pytest.mark.api
def test_listar_categorias():
    """Teste para listar todas as categorias disponíveis"""
    response = requests.get(f"{BASE_URL}/products/categories")
    
    assert response.status_code == 200
    categorias = response.json()
    assert isinstance(categorias, list)
    
    # Verificar que todas as categorias esperadas estão presentes
    for categoria in CATEGORIAS_VALIDAS:
        assert categoria in categorias
