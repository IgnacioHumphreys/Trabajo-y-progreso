import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_back import *

t = 1

class ABM_instituciones(funciones_TyP):

    def __init__(self, driver):
            super().__init__(driver)

    def click_instituciones(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_instituciones)
        title_instituciones = self.driver.find_element(self, By.XPATH, "//h1[text()='Instituciones']")
        if title_instituciones.is_displayed():
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click instituciones **")
        else:
            print("** hay un fallo en el step: Click instituciones **")
            assert False, "** hay un fallo en el step: Click instituciones **"

    def com_cod_institucion(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_cod_institucion, "2320")

    def com_nom_institucion(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_nom_institucion, "Instituciones (automatizacion)")

    def select_programa_enInstitucion(self):
        funciones_TyP.click_Field(self, By.XPATH, box2_programa)
        funciones_TyP.scrollToElement(self, By.XPATH, select_programa)
        funciones_TyP.click_Field(self, By.XPATH, select_programa)

    def mod_codigo_institucion(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_cod_institucion, "2323")