import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_back import *

t = 1

class buscar_programa(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def escribir_codigo(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_cod_programa_buscar, "2310")

    def escribir_nom_programa(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_nom_programa_buscar, "Programa (Automatización)")

    def seleccionar_ministerio_en_programa(self):
        funciones_TyP.click_Field(self, By.XPATH, box3_ministerio)
        funciones_TyP.scrollToElement(self, By.XPATH, select_automatizaion_en_programa)
        funciones_TyP.click_Field(self, By.XPATH, select_automatizaion_en_programa)

    def click_buscar(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_buscar)
        time.sleep(t)
        texto_comparativo = "2310"
        programa_buscado = self.driver.find_element(By.XPATH, "//p[text()='2310']")
        texto = programa_buscado.text
        if texto == texto_comparativo:
            funciones_TyP.screenShot(self, "Se visualiza el programa buscado")
            print("** valido el step: Click boton buscar programa y validar **")
        else:
            self.driver.quit()
            print("** hay un fallo en el step: Click boton buscar programa y validar **")
            assert False, "** hay un fallo en el step: Click boton buscar programa y validar **"