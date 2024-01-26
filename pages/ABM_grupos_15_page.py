import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_configuracion import *

t = 1

class ABM_grupos(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def click_grupos(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_grupos)
        title_grupos = self.driver.find_element(self, By.XPATH,"//div[@class='col']//h1[1]")
        if title_grupos is True:
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click grupos **")
        else:
            print("** hay un fallo en el step: Click grupos **")
            assert False, "** hay un fallo en el step: Click grupos **"

    def com_nom_grupo(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_grupo, "Cursos faciles")

    def activar_switch(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_switch)

    def select_capacitaciones(self):
        funciones_TyP.scrollToElement(self, By.ID, select_capacitacion1)
        funciones_TyP.click_Field(self, By.ID, select_capacitacion1)
        funciones_TyP.scrollToElement(self, By.ID, select_capacitacion2)
        funciones_TyP.click_Field(self, By.ID, select_capacitacion2)

    def click_publicar(self):
        funciones_TyP.scrollToElement(self, By.XPATH, btn_publicar)
        funciones_TyP.click_Field(self, By.XPATH, btn_publicar)
        title_grupos_publicado = self.driver.find_element(self, By.XPATH, "(//div[@class='alert alert-success']//div)[2]")
        if title_grupos_publicado is True:
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click boton publicar **")
        else:
            print("** hay un fallo en el step: Click boton publicar **")
            assert False, "** hay un fallo en el step: Click boton publicar **"