import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_front import *
from elements.elementos_back import *
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys

t = 2

class LoginPage_front(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def openBrowser(self):
        funciones_TyP.driver_Chrome(self)
        funciones_TyP.browser(self, URL_front)
        time.sleep(5)

    def validar_logo(self):
        funciones_TyP.validates_visibility(self, By.XPATH, logoBA)
        funciones_TyP.screenShot(self, "Ingreso al front ofertas de educacion")
        self.driver.quit()