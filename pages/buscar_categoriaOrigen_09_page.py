import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_configuracion import *

t = 1

class buscar_categoriaOrigen(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def escribir_categoriaOrigen(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_categoriaOrigen, "CategoríaOrigen (automatizacion)")
        time.sleep(t)

    def escribir_categoriaWeb_en_origen(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_categoriaWeb_en_origen, "CategoríaWeb (automatización)")

    def click_buscar(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_buscar)
        categoriaOrigen_automatizacion = self.driver.find_element(self, By.XPATH,
                                                               "(//table[@class='table table-hover']//p)[1]")
        if categoriaOrigen_automatizacion is True:
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click boton buscar categoriaOrigen **")
        else:
            print("** hay un fallo en el step: Click boton buscar categoriaOrigen **")
            assert False, "** hay un fallo en el step: Click boton buscar categoriaOrigen **"