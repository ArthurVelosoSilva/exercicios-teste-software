"""
Exercício 4: Page Object Model
Testes de login usando POM
"""
import pytest
import sys
sys.path.insert(0, '../exercicio04/pages')

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@pytest.mark.web
def test_login_sucesso_pom(chrome_driver):
    """Teste de login com sucesso usando POM"""
    login_page = LoginPage(chrome_driver)
    dashboard_page = DashboardPage(chrome_driver)
    
    # Abrir página e fazer login
    login_page.abrir_pagina()
    login_page.fazer_login("student", "Password123")
    
    # Verificar que está logado
    assert dashboard_page.esta_logado()
    assert "Logged In Successfully" in dashboard_page.obter_mensagem_sucesso()


@pytest.mark.web
def test_login_username_invalido_pom(chrome_driver):
    """Teste de login com username inválido usando POM"""
    login_page = LoginPage(chrome_driver)
    
    login_page.abrir_pagina()
    login_page.fazer_login("invaliduser", "Password123")
    
    # Verificar mensagem de erro
    assert login_page.tem_mensagem_erro()
    assert "Your username is invalid!" in login_page.obter_mensagem_erro()


@pytest.mark.web
def test_login_senha_invalida_pom(chrome_driver):
    """Teste de login com senha inválida usando POM"""
    login_page = LoginPage(chrome_driver)
    
    login_page.abrir_pagina()
    login_page.fazer_login("student", "wrongpassword")
    
    # Verificar mensagem de erro
    assert login_page.tem_mensagem_erro()
    assert "Your password is invalid!" in login_page.obter_mensagem_erro()


@pytest.mark.web
def test_login_campos_vazios_pom(chrome_driver):
    """Teste de login com campos vazios usando POM"""
    login_page = LoginPage(chrome_driver)
    
    login_page.abrir_pagina()
    login_page.clicar_submit()
    
    # Verificar que permanece na página de login
    assert "practice-test-login" in login_page.obter_url_atual()


@pytest.mark.web
def test_login_apenas_username_pom(chrome_driver):
    """Teste de login apenas com username usando POM"""
    login_page = LoginPage(chrome_driver)
    
    login_page.abrir_pagina()
    login_page.preencher_username("student")
    login_page.clicar_submit()
    
    # Verificar mensagem de erro
    assert login_page.tem_mensagem_erro()


@pytest.mark.web
def test_login_apenas_password_pom(chrome_driver):
    """Teste de login apenas com password usando POM"""
    login_page = LoginPage(chrome_driver)
    
    login_page.abrir_pagina()
    login_page.preencher_password("Password123")
    login_page.clicar_submit()
    
    # Verificar mensagem de erro
    assert login_page.tem_mensagem_erro()


@pytest.mark.web
def test_dashboard_possui_logout_pom(chrome_driver):
    """Teste para verificar botão de logout no dashboard"""
    login_page = LoginPage(chrome_driver)
    dashboard_page = DashboardPage(chrome_driver)
    
    login_page.abrir_pagina()
    login_page.fazer_login("student", "Password123")
    
    # Verificar que botão de logout existe
    assert dashboard_page.tem_botao_logout()


@pytest.mark.web
@pytest.mark.parametrize("username,password,esperado", [
    ("student", "Password123", "sucesso"),
    ("invaliduser", "Password123", "erro_username"),
    ("student", "wrongpass", "erro_password"),
])
def test_login_multiplos_casos_pom(chrome_driver, username, password, esperado):
    """Teste parametrizado de múltiplos casos de login"""
    login_page = LoginPage(chrome_driver)
    dashboard_page = DashboardPage(chrome_driver)
    
    login_page.abrir_pagina()
    login_page.fazer_login(username, password)
    
    if esperado == "sucesso":
        assert dashboard_page.esta_logado()
    elif esperado == "erro_username":
        assert login_page.tem_mensagem_erro()
        assert "username" in login_page.obter_mensagem_erro().lower()
    elif esperado == "erro_password":
        assert login_page.tem_mensagem_erro()
        assert "password" in login_page.obter_mensagem_erro().lower()