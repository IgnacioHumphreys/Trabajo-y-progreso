import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_back import *

t = 1

class ABM_tipoFormacionWeb(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def click_educacion(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_educacion)
        btn_tiposFormacionWeb = self.driver.find_element(self, By.XPATH, "(//div[@id='educacionCollapse']//a)[2]")
        if btn_tiposFormacionWeb is True:
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click educacion **")
        else:
            print("** hay un fallo en el step: Click educacion **")
            assert False, "** hay un fallo en el step: Click educacion **"

    def click_tiposFormacionWeb(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_tiposFormacionWeb)
        title_tiposFormacionWeb = self.driver.find_element(self, By.XPATH, "//div[@class='col']//h1[1]")
        if title_tiposFormacionWeb is True:
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click tipos formacion web **")
        else:
            print("** hay un fallo en el step: Click tipos formacion web **")
            assert False, "** hay un fallo en el step: Click tipos formacion web **"

    def com_nom_formacionWeb(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_formacionWeb, "Cursos 2")

    def select_color(self):
        funciones_TyP.click_Field(self, By.XPATH, box_colorEtiqueta)
        funciones_TyP.scrollToElement(self, By.XPATH, select_verde)
        funciones_TyP.click_Field(self, By.XPATH, select_verde)

    '''def click_guardar_formacionWeb(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_guardar_formacionWeb)
        title_guardar_formacionWeb = self.driver.find_element(self, By.XPATH, "(//div[@class='alert alert-success']//div)[2]")
        if title_guardar_formacionWeb is True:
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click boton guardar formacion web **")
        else:
            print("** hay un fallo en el step: Click boton guardar formacion web **")
            assert False, "** hay un fallo en el step: Click boton guardar formacion web **"'''

    def mod_nom_formacionWeb(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_formacionWeb, "Cursos 3")

    def mod_color_etiqueta(self):
        funciones_TyP.click_Field(self, By.XPATH, box_colorEtiqueta)
        funciones_TyP.scrollToElement(self, By.XPATH, select_rojo)
        funciones_TyP.click_Field(self, By.XPATH, select_rojo)