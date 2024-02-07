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
        time.sleep(t)
        texto_comparativo = "Creatividad (Automatizacion)"
        aptitud_buscada = self.driver.find_element(By.XPATH, "//p[text()='Creatividad (Automatizacion)']")
        texto = aptitud_buscada.text
        if texto == texto_comparativo:
            funciones_TyP.screenShot(self, "Se visualiza la aptitud buscada")
            print("** valido el step: Click boton buscar aptitud y validar **")
        else:
            self.driver.quit()
            print("** hay un fallo en el step: Click boton buscar aptitud y validar **")
            assert False, "** hay un fallo en el step: Click boton buscar aptitud y validar **"