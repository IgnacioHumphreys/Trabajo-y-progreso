import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_configuracion import *

t = 1

class LoginPage(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def openBrowser(self):
        funciones_TyP.driver_Chrome(self)
        funciones_TyP.browser(self, URL)
        time.sleep(5)

    def validarLogo(self):
        funciones_TyP.validates_visibility(self, By.XPATH, logoBA)
        funciones_TyP.screenShot(self, "Ingreso a la pagina Portal de Oportunidades (backend)")

    def completar_credenciales (self):
        funciones_TyP.input_Texto(self, By.XPATH, input_usuario, "27165286796")
        funciones_TyP.input_Texto(self, By.XPATH, input_password, "Troquel1")
        time.sleep(t)

    def click_ingresar(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_ingresar)
        title = self.driver.find_element(By.XPATH, "//div[@class='title-container']//h4[1]")
        if title is True:
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click boton ingresar **")
        else:
            self.driver.quit()
            print("** hay un fallo: Click boton ingresar **")
            assert False, "** hay un fallo: Click boton ingresar **"