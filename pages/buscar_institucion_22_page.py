import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_back import *

t = 1

class buscar_institucion(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def escribir_cod_institucion(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_cod_institucion, "2525")

    def escribir_nom_institucion(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_nom_institucion, "Automatizacion")

    def click_buscar_instituion(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_buscar)
        codigo = "2525"
        institucion_automatizacion = self.driver.find_element(self, By.XPATH, "//p[text()='2525']")
        if institucion_automatizacion == codigo:
            funciones_TyP.screenShot(self, "Se visualiza la institucion buscada")
            print("** valido el step: Click boton buscar institucion **")
        else:
            print("** hay un fallo en el step: Click boton buscar institucion **")
            assert False, "** hay un fallo en el step: Click boton buscar institucion **"