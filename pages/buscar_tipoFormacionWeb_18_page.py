import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_back import *

t = 1

class buscar_formacionWeb(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def escribir_formacionWeb(self):
        funciones_TyP.input_Texto(self, By.ID, "SearchTipoFormacionWebType_nombre", "Automatizacion")

    def click_buscar(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_buscar)
        time.sleep(t)
        texto_comparativo = "Automatizacion"
        formacionweb_buscada = self.driver.find_element(By.XPATH, "//p[text()='Automatizacion']")
        texto = formacionweb_buscada.text
        if texto == texto_comparativo:
            funciones_TyP.screenShot(self, "Se visualiza la formacion web buscada")
            print("** valido el step: Click boton buscar formacion web y validar **")
        else:
            print("** hay un fallo en el step: Click boton buscar formacion web y validar **")
            assert False, "** hay un fallo en el step: Click boton buscar formacion web y validar **"