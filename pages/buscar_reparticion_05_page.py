import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_configuracion import *

t = 1

class buscar_reparticion(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def escribir_reparticion(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_reparticion, "DG Políticas de Juventud")

    def click_buscar(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_buscar)
        time.sleep(t)
        DG_Políticas_Juventud = self.driver.find_element(self, By.XPATH, "(//table[@class='table table-hover']//p)[1]")
        if DG_Políticas_Juventud is True:
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click boton buscar reparticion **")
        else:
            print("** hay un fallo en el step: Click boton buscar reparticion **")
            assert False, "** hay un fallo en el step: Click boton buscar reparticion **"