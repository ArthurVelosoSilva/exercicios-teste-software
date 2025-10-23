"""
Exercício 4: Page Object Model
Página de Login
"""
from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    """Page Object para a página de login"""
    
    # Locators
    URL = "https://practicetestautomation.com/practice-test-login/"
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON = (By.ID, "submit")
    ERROR_MESSAGE = (By.ID, "error")
    
    def abrir_pagina(self):
        """Abre a página de login"""
        self.abrir(self.URL)
    
    def preencher_username(self, username):
        """Preenche o campo de username"""
        self.digitar(self.USERNAME_INPUT, username)
    
    def preencher_password(self, password):
        """Preenche o campo de password"""
        self.digitar(self.PASSWORD_INPUT, password)
    
    def clicar_submit(self):
        """Clica no botão de submit"""
        self.clicar(self.SUBMIT_BUTTON)
    
    def fazer_login(self, username, password):
        """Realiza o processo completo de login"""
        self.preencher_username(username)
        self.preencher_password(password)
        self.clicar_submit()
    
    def obter_mensagem_erro(self):
        """Obtém a mensagem de erro se existir"""
        if self.elemento_visivel(self.ERROR_MESSAGE):
            return self.obter_texto(self.ERROR_MESSAGE)
        return None
    
    def tem_mensagem_erro(self):
        """Verifica se há mensagem de erro visível"""
        return self.elemento_visivel(self.ERROR_MESSAGE)
