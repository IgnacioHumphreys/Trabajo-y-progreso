import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_configuracion import *

t = 1

class buscar_grupo(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def escribir_grupo(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_grupo, "Cursos cortos")

    def click_buscar(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_buscar)
        cursos_cortos = self.driver.find_element(self, By.XPATH, "(//tr[@data-id='2']//p)[1]")
        if cursos_cortos is True:
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click boton buscar grupo **")
        else:
            print("** hay un fallo en el step: Click boton buscar grupo **")
            assert False, "** hay un fallo en el step: Click boton buscar grupo **"