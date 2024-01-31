import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_back import *

t = 1

class buscar_formacionWeb(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def escribir_formacionWeb(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_formacionWeb, "Curso Prueba")

    def click_buscar(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_buscar)
        curso_prueba = self.driver.find_element(self, By.XPATH, "//p[text()='Curso Prueba']")
        if curso_prueba is True:
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click boton buscar formacion web **")
        else:
            print("** hay un fallo en el step: Click boton buscar formacion web **")
            assert False, "** hay un fallo en el step: Click boton buscar formacion web **"