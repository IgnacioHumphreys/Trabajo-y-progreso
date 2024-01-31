import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_back import *

t = 1

class buscar_aptitud(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def escribir_aptitud(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_aptitud, "Creatividad (Automatizacion)")

    def click_buscar(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_buscar)
        aptitud_automatizacion = self.driver.find_element(self, By.XPATH,
                                                           "(//table[@class='table table-hover']//p)[1]")
        if aptitud_automatizacion is True:
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click boton buscar aptitud **")
        else:
            print("** hay un fallo en el step: Click boton buscar aptitud **")
            assert False, "** hay un fallo en el step: Click boton buscar aptitud **"