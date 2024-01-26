import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_configuracion import *

t = 1

class buscar_ministerio(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def escribir_ministerio(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_nom_ministerio, "MEGC")

    def click_buscar(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_buscar)
        time.sleep(t)
        MEGC = self.driver.find_element(self, By.XPATH, "//table[@class='table table-hover']//p[1]")
        if MEGC is True:
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click boton buscar **")
        else:
            print("** hay un fallo en el step: Click boton buscar **")
            assert False, "** hay un fallo en el step: Click boton buscar **"