"""
Exercício 1: Teste de Login (Web)
Testes automatizados para formulário de login
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.web
def test_login_sucesso(chrome_driver):
    """Teste de login com credenciais válidas"""
    driver = chrome_driver
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    # Preencher formulário
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    
    # Aguardar página carregar
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "post-title"))
    )
    
    # Verificar sucesso
    assert "Logged In Successfully" in driver.page_source
    assert "practicetestautomation.com/logged-in-successfully/" in driver.current_url


@pytest.mark.web
def test_login_username_invalido(chrome_driver):
    """Teste de login com username inválido"""
    driver = chrome_driver
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    driver.find_element(By.ID, "username").send_keys("invaliduser")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    
    # Verificar mensagem de erro
    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "error"))
    )
    assert "Your username is invalid!" in error_message.text


@pytest.mark.web
def test_login_senha_incorreta(chrome_driver):
    """Teste de login com senha incorreta"""
    driver = chrome_driver
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("senhaerrada")
    driver.find_element(By.ID, "submit").click()
    
    # Verificar mensagem de erro
    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "error"))
    )
    assert "Your password is invalid!" in error_message.text


@pytest.mark.web
def test_login_campos_vazios(chrome_driver):
    """Teste de tentativa de login sem preencher campos"""
    driver = chrome_driver
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    # Tentar fazer login sem preencher nada
    driver.find_element(By.ID, "submit").click()
    
    # Verificar que permanece na mesma página
    assert "practice-test-login" in driver.current_url


@pytest.mark.web
def test_login_username_vazio(chrome_driver):
    """Teste de login apenas com senha preenchida"""
    driver = chrome_driver
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    
    # Verificar mensagem de erro
    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "error"))
    )
    assert "Your username is invalid!" in error_message.text
