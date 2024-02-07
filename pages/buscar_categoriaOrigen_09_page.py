import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_back import *

t = 1

class buscar_categoriaOrigen(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def escribir_categoriaOrigen(self):
        funciones_TyP.input_Texto(self, By.ID, "SearchCategoriaType_nombre", "CategoríaOrigen (automatizacion)")
        time.sleep(t)

    def escribir_categoriaWeb_en_origen(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_categoriaWeb_en_origen, "CategoríaWeb (automatización)")

    def click_buscar(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_buscar)
        time.sleep(t)
        texto_comparativo = "CategoríaOrigen (automatizacion)"
        categoriaOrigen_buscada = self.driver.find_element(By.XPATH,
                                                               "//p[text()='CategoríaOrigen (automatizacion)']")
        texto = categoriaOrigen_buscada.text
        if texto == texto_comparativo:
            funciones_TyP.screenShot(self, "Se visualiza la categoria origen buscada")
            print("** valido el step: Click boton buscar categoriaOrigen y validar **")
        else:
            self.driver.quit()
            print("** hay un fallo en el step: Click boton buscar categoriaOrigen y validar **")
            assert False, "** hay un fallo en el step: Click boton buscar categoriaOrigen y validar **"