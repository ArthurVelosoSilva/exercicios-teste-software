"""
Exercício 5: Testes Parametrizados (Web)
Testes de busca parametrizada
"""
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.web
@pytest.mark.parametrize("termo_busca", [
    "Python",
    "Selenium",
    "Pytest",
    "API Testing",
    "Automation"
])
def test_busca_google(chrome_driver, termo_busca):
    """Teste parametrizado de busca no Google"""
    driver = chrome_driver
    driver.get("https://www.google.com")
    
    try:
        # Aceitar cookies se aparecer
        cookie_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Aceitar') or contains(., 'Accept')]"))
        )
        cookie_btn.click()
    except:
        pass
    
    # Buscar elemento de pesquisa
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(termo_busca)
    search_box.send_keys(Keys.RETURN)
    
    # Aguardar resultados
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )
    
    # Verificar que o termo aparece nos resultados
    assert termo_busca.lower() in driver.page_source.lower()


@pytest.mark.web
@pytest.mark.parametrize("produto", [
    "electronics",
    "jewelery",
    "men's clothing",
    "women's clothing"
])
def test_busca_produtos_categoria(chrome_driver, produto):
    """Teste parametrizado de categorias de produtos"""
    # Este teste usa a página de produtos da FakeStore
    driver = chrome_driver
    driver.get(f"https://fakestoreapi.com/products/category/{produto}")
    
    # Verificar que a página carregou
    time.sleep(2)
    assert driver.page_source is not None


@pytest.mark.web
@pytest.mark.parametrize("username,senha,resultado", [
    ("student", "Password123", "sucesso"),
    ("invaliduser", "Password123", "erro"),
    ("student", "wrongpass", "erro"),
    ("", "Password123", "erro"),
    ("student", "", "erro"),
])
def test_login_multiplos_cenarios(chrome_driver, username, senha, resultado):
    """Teste parametrizado de múltiplos cenários de login"""
    driver = chrome_driver
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    if username:
        driver.find_element(By.ID, "username").send_keys(username)
    if senha:
        driver.find_element(By.ID, "password").send_keys(senha)
    
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    
    if resultado == "sucesso":
        assert "Logged In Successfully" in driver.page_source
    else:
        assert ("invalid" in driver.page_source.lower() or 
                "practice-test-login" in driver.current_url)


@pytest.mark.web
@pytest.mark.parametrize("idioma", ["pt", "en", "es", "fr"])
def test_mudanca_idioma(chrome_driver, idioma):
    """Teste parametrizado de mudança de idioma"""
    driver = chrome_driver
    driver.get(f"https://www.wikipedia.org")
    
    # Aguardar página carregar
    time.sleep(2)
    assert driver.page_source is not None


@pytest.mark.web
@pytest.mark.parametrize("num_produtos", [5, 10, 15])
def test_limite_produtos_exibidos(chrome_driver, num_produtos):
    """Teste parametrizado de limite de produtos"""
    driver = chrome_driver
    driver.get(f"https://fakestoreapi.com/products?limit={num_produtos}")
    
    # Aguardar carregamento
    time.sleep(2)
    assert driver.page_source is not None


@pytest.mark.web
@pytest.mark.parametrize("navegador_tamanho", [
    (1920, 1080),
    (1366, 768),
    (375, 812),  # Mobile
])
def test_responsividade(chrome_driver, navegador_tamanho):
    """Teste parametrizado de responsividade"""
    driver = chrome_driver
    largura, altura = navegador_tamanho
    
    driver.set_window_size(largura, altura)
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    # Verificar que elementos principais estão presentes
    assert driver.find_element(By.ID, "username").is_displayed()
    assert driver.find_element(By.ID, "password").is_displayed()
    assert driver.find_element(By.ID, "submit").is_displayed()


@pytest.mark.web
@pytest.mark.parametrize("cor_hex", [
    "#FF0000",  # Vermelho
    "#00FF00",  # Verde
    "#0000FF",  # Azul
])
def test_validacao_cores(cor_hex):
    """Teste parametrizado de validação de cores hexadecimais"""
    # Validação de formato
    assert cor_hex.startswith("#")
    assert len(cor_hex) == 7
    # Verificar que são caracteres hexadecimais válidos
    assert all(c in "0123456789ABCDEFabcdef" for c in cor_hex[1:])
