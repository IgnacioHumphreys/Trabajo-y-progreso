import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_back import *

t = 1

class buscar_ministerio(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def escribir_ministerio(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_ministerio, "Automatizacion")

    def click_buscar_ministerio(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_buscar)
        time.sleep(t)
        texto_comparativo = "Automatizacion"
        min_buscado = self.driver.find_element(By.XPATH, "//p[text()='Automatizacion']")
        texto = min_buscado.text
        if texto == texto_comparativo:
            funciones_TyP.screenShot(self, "Se visualiza el ministerio buscado")
            print("** valido el step: Click boton buscar ministerio y validar **")
        else:
            self.driver.quit()
            print("** hay un fallo en el step: Click boton buscar ministerio y validar **")
            assert False, "** hay un fallo en el step: Click boton buscar ministerio y validar **"