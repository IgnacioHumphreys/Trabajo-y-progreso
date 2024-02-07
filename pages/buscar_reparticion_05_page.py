import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_back import *

t = 1

class buscar_reparticion(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def escribir_reparticion(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_reparticion, "Repartición (automatización)")

    def click_buscar(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_buscar)
        time.sleep(t)
        texto_comparativo = "Repartición (automatización)"
        reparticion_buscada = self.driver.find_element(By.XPATH, "//p[text()='Repartición (automatización)']")
        texto = reparticion_buscada.text
        if texto == texto_comparativo:
            funciones_TyP.screenShot(self, "Se visualiza la reparticion buscada")
            print("** valido el step: Click boton buscar reparticion y validar **")
        else:
            self.driver.quit()
            print("** hay un fallo en el step: Click boton buscar reparticion y validar **")
            assert False, "** hay un fallo en el step: Click boton buscar reparticion y validar **"