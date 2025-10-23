"""
Exercício 3: Teste CRUD Completo (REST)
Testes CRUD para API JSONPlaceholder
"""
import pytest
import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture
def todo_criado():
    """Fixture para criar um todo para testes"""
    todo_data = {
        "title": "Minha tarefa de teste",
        "completed": False,
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/todos", json=todo_data)
    todo = response.json()
    
    yield todo
    
    # Teardown - tentar deletar (JSONPlaceholder é fake, mas seguimos o padrão)
    requests.delete(f"{BASE_URL}/todos/{todo['id']}")


@pytest.mark.api
def test_create_todo():
    """Teste CREATE - Criar novo todo"""
    todo_data = {
        "title": "Aprender testes automatizados",
        "completed": False,
        "userId": 1
    }
    
    response = requests.post(f"{BASE_URL}/todos", json=todo_data)
    
    assert response.status_code == 201
    todo = response.json()
    
    assert "id" in todo
    assert todo["title"] == todo_data["title"]
    assert todo["completed"] == todo_data["completed"]
    assert todo["userId"] == todo_data["userId"]


@pytest.mark.api
def test_create_todo_sem_titulo():
    """Teste CREATE com dados inválidos - sem título"""
    todo_data = {
        "completed": False,
        "userId": 1
    }
    
    response = requests.post(f"{BASE_URL}/todos", json=todo_data)
    
    # JSONPlaceholder aceita qualquer coisa, mas validamos a resposta
    assert response.status_code == 201


@pytest.mark.api
def test_read_todo():
    """Teste READ - Buscar todo específico"""
    todo_id = 1
    response = requests.get(f"{BASE_URL}/todos/{todo_id}")
    
    assert response.status_code == 200
    todo = response.json()
    
    assert todo["id"] == todo_id
    assert "title" in todo
    assert "completed" in todo
    assert "userId" in todo


@pytest.mark.api
def test_read_todos_lista():
    """Teste READ - Listar todos os todos"""
    response = requests.get(f"{BASE_URL}/todos")
    
    assert response.status_code == 200
    todos = response.json()
    
    assert len(todos) > 0
    assert isinstance(todos, list)


@pytest.mark.api
def test_read_todos_por_usuario():
    """Teste READ - Filtrar todos por usuário"""
    user_id = 1
    response = requests.get(f"{BASE_URL}/todos", params={"userId": user_id})
    
    assert response.status_code == 200
    todos = response.json()
    
    assert len(todos) > 0
    for todo in todos:
        assert todo["userId"] == user_id


@pytest.mark.api
def test_update_todo_completo(todo_criado):
    """Teste UPDATE completo - PUT"""
    todo_id = todo_criado["id"]
    
    todo_atualizado = {
        "id": todo_id,
        "title": "Tarefa atualizada",
        "completed": True,
        "userId": 1
    }
    
    response = requests.put(f"{BASE_URL}/todos/{todo_id}", json=todo_atualizado)
    
    assert response.status_code == 200
    todo = response.json()
    
    assert todo["title"] == todo_atualizado["title"]
    assert todo["completed"] == True


@pytest.mark.api
def test_update_todo_parcial(todo_criado):
    """Teste UPDATE parcial - PATCH"""
    todo_id = todo_criado["id"]
    
    atualizacao = {
        "completed": True
    }
    
    response = requests.patch(f"{BASE_URL}/todos/{todo_id}", json=atualizacao)
    
    assert response.status_code == 200
    todo = response.json()
    
    assert todo["completed"] == True


@pytest.mark.api
def test_delete_todo(todo_criado):
    """Teste DELETE - Deletar todo"""
    todo_id = todo_criado["id"]
    
    response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
    
    assert response.status_code == 200


@pytest.mark.api
def test_crud_fluxo_completo():
    """Teste de fluxo CRUD completo"""
    
    # CREATE
    novo_todo = {
        "title": "Teste CRUD completo",
        "completed": False,
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/todos", json=novo_todo)
    assert response.status_code == 201
    todo_id = response.json()["id"]
    
    # READ
    response = requests.get(f"{BASE_URL}/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json()["title"] == novo_todo["title"]
    
    # UPDATE
    atualizacao = {"completed": True}
    response = requests.patch(f"{BASE_URL}/todos/{todo_id}", json=atualizacao)
    assert response.status_code == 200
    assert response.json()["completed"] == True
    
    # DELETE
    response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
    assert response.status_code == 200


@pytest.mark.api
def test_validar_schema_todo():
    """Teste para validar schema do todo"""
    response = requests.get(f"{BASE_URL}/todos/1")
    
    assert response.status_code == 200
    todo = response.json()
    
    # Validar estrutura
    assert isinstance(todo["id"], int)
    assert isinstance(todo["title"], str)
    assert isinstance(todo["completed"], bool)
    assert isinstance(todo["userId"], int)
