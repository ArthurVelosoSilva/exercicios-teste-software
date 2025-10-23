"""
Exercício 5: Testes Parametrizados (REST)
Validações parametrizadas de email e senha
"""
import pytest
import requests


BASE_URL_REQRES = "https://reqres.in/api"


# Cenários de emails inválidos
emails_invalidos = [
    "sem-arroba.com",
    "@sem-usuario.com",
    "sem-dominio@",
    "espacos no meio@teste.com",
    "caracteres!especiais@teste.com",
    "..pontos@teste.com",
    "teste@",
    "@teste.com",
    "teste..duplo@email.com",
    "teste@dominio",
]


# Cenários de senhas inválidas
senhas_invalidas = [
    ("123", "muito curta"),
    ("semNumero", "sem número"),
    ("semmaiuscula123", "sem maiúscula"),
    ("12345678", "só números"),
    ("ab", "muito curta"),
    ("SOMENTEMAIUSCULA", "sem minúscula"),
    ("", "vazia"),
]


@pytest.mark.api
@pytest.mark.parametrize("email_invalido", emails_invalidos)
def test_validacao_email_api(email_invalido):
    """Teste de validação de emails inválidos na API"""
    response = requests.post(f"{BASE_URL_REQRES}/register", json={
        "email": email_invalido,
        "password": "senha123"
    })
    
    # API deve rejeitar emails inválidos
    assert response.status_code == 400
    assert "error" in response.json()


@pytest.mark.api
@pytest.mark.parametrize("senha,motivo", senhas_invalidas)
def test_validacao_senha(senha, motivo):
    """Teste de validação de senhas inválidas"""
    response = requests.post(f"{BASE_URL_REQRES}/register", json={
        "email": "test@test.com",
        "password": senha
    })
    
    # API deve rejeitar senhas inválidas
    assert response.status_code == 400


@pytest.mark.api
def test_registro_email_valido():
    """Teste de registro com email válido"""
    response = requests.post(f"{BASE_URL_REQRES}/register", json={
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    })
    
    # Este email é válido na API de teste
    assert response.status_code == 200
    assert "token" in response.json()


@pytest.mark.api
@pytest.mark.parametrize("email", [
    "usuario@dominio.com",
    "nome.sobrenome@empresa.com.br",
    "email+tag@teste.com",
    "123@numerico.com",
])
def test_emails_validos_formato(email):
    """Teste para verificar formato de emails válidos"""
    # Validação básica de formato
    assert "@" in email
    assert "." in email.split("@")[1]
    assert len(email.split("@")) == 2


@pytest.mark.api
@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
def test_buscar_usuario_por_id(user_id):
    """Teste parametrizado para buscar múltiplos usuários"""
    response = requests.get(f"{BASE_URL_REQRES}/users/{user_id}")
    
    assert response.status_code == 200
    data = response.json()["data"]
    assert data["id"] == user_id
    assert "email" in data
    assert "first_name" in data
    assert "last_name" in data


@pytest.mark.api
@pytest.mark.parametrize("pagina", [1, 2])
def test_listar_usuarios_paginacao(pagina):
    """Teste de paginação de usuários"""
    response = requests.get(f"{BASE_URL_REQRES}/users", params={"page": pagina})
    
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["page"] == pagina
    assert len(json_data["data"]) > 0


@pytest.mark.api
@pytest.mark.parametrize("nome,cargo", [
    ("morpheus", "leader"),
    ("neo", "developer"),
    ("trinity", "hacker"),
])
def test_criar_usuario_parametrizado(nome, cargo):
    """Teste parametrizado para criar usuários"""
    response = requests.post(f"{BASE_URL_REQRES}/users", json={
        "name": nome,
        "job": cargo
    })
    
    assert response.status_code == 201
    user = response.json()
    assert user["name"] == nome
    assert user["job"] == cargo
    assert "id" in user
    assert "createdAt" in user


@pytest.mark.api
@pytest.mark.parametrize("delay", [1, 2, 3])
def test_requisicao_com_delay(delay):
    """Teste de requisições com delay"""
    response = requests.get(f"{BASE_URL_REQRES}/users", params={"delay": delay})
    
    assert response.status_code == 200
    assert "data" in response.json()
