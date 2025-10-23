"""
Exercício 4: Page Object Model
Página de Dashboard (após login)
"""
from selenium.webdriver.common.by import By
from .base_page import BasePage


class DashboardPage(BasePage):
    """Page Object para a página de dashboard"""
    
    # Locators
    SUCCESS_MESSAGE = (By.CLASS_NAME, "post-title")
    LOGOUT_BUTTON = (By.LINK_TEXT, "Log out")
    WELCOME_MESSAGE = (By.TAG_NAME, "h1")
    
    def esta_logado(self):
        """Verifica se o usuário está logado com sucesso"""
        try:
            return (self.elemento_visivel(self.SUCCESS_MESSAGE) and 
                    "logged-in-successfully" in self.obter_url_atual())
        except:
            return False
    
    def obter_mensagem_sucesso(self):
        """Obtém a mensagem de sucesso do login"""
        if self.elemento_visivel(self.SUCCESS_MESSAGE):
            return self.obter_texto(self.SUCCESS_MESSAGE)
        return None
    
    def obter_mensagem_boas_vindas(self):
        """Obtém a mensagem de boas-vindas"""
        if self.elemento_visivel(self.WELCOME_MESSAGE):
            return self.obter_texto(self.WELCOME_MESSAGE)
        return None
    
    def fazer_logout(self):
        """Realiza logout"""
        if self.elemento_visivel(self.LOGOUT_BUTTON):
            self.clicar(self.LOGOUT_BUTTON)
    
    def tem_botao_logout(self):
        """Verifica se o botão de logout está visível"""
        return self.elemento_visivel(self.LOGOUT_BUTTON)
