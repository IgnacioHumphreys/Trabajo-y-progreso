import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_back import *
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys

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
        funciones_TyP.input_Texto(self, By.XPATH, input_usuario, usuario)
        funciones_TyP.input_Texto(self, By.XPATH, input_password, password)
        time.sleep(t)

    def click_ingresar(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_ingresar)
        act = ActionChains(self.driver)
        act.send_keys(Keys.ENTER).perform()
        title_BA = self.driver.find_element(By.XPATH, "//div[@class='title-container']//h4[1]")
        if title_BA.is_displayed():
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click boton ingresar **")
        else:
            self.driver.quit()
            print("** hay un fallo: Click boton ingresar **")
            assert False, "** hay un fallo: Click boton ingresar **"