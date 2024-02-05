import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_back import *

t = 1

class buscar_grupo(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def escribir_grupo(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_grupo, "Cursos cortos")

    def click_buscar(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_buscar)
        time.sleep(t)
        texto_comparativo = "Cursos cortos"
        curso_buscado = self.driver.find_element(By.XPATH, "//p[text()='Cursos cortos']")
        texto = curso_buscado.text
        if texto == texto_comparativo:
            funciones_TyP.screenShot(self, "Se visualiza el grupo buscado")
            print("** valido el step: Click boton buscar grupo y visualizar **")
        else:
            print("** hay un fallo en el step: Click boton buscar grupo y visualizar **")
            assert False, "** hay un fallo en el step: Click boton buscar grupo y visualizar **"