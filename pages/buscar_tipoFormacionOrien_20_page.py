import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_back import *

t = 1

class buscar_tipoFormacionOrigen(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def escribir_tipoFormacionOrigen(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_formacionOrigen, "Formación origen_Test")

    def click_buscar(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_buscar)
        time.sleep(t)
        nombre = "Formación origen (automatización)"
        formacionOrigen_buscada = self.driver.find_element(self, By.XPATH, "//p[text()='Formación origen (automatización)']")
        if formacionOrigen_buscada == nombre:
            funciones_TyP.screenShot(self, "Se visualiza la formacion origen buscada")
            print("** valido el step: Click boton buscar formacion origen y validar **")
        else:
            print("** hay un fallo en el step: Click boton buscar formacion origen y validar **")
            assert False, "** hay un fallo en el step: Click boton buscar formacion origen y validar **"