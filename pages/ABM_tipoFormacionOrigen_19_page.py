import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_back import *

t = 1

class ABM_tipoFormacionOrigen(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def click_tiposFormacionOrigen(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_tiposFormacionOrigen)
        title_tiposFormacionOrigen = self.driver.find_element(self, By.XPATH, "//div[@class='col']//h1[1]")
        if title_tiposFormacionOrigen.is_displayed():
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click tipos formacion origen **")
        else:
            print("** hay un fallo en el step: Click tipos formacion origen **")
            assert False, "** hay un fallo en el step: Click tipos formacion origen **"

    def com_nom_formacionOrigen(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_formacionOrigen, "Origen")

    def select_formacionWeb(self):
        funciones_TyP.click_Field(self, By.XPATH, box_formacionWeb)
        funciones_TyP.scrollToElement(self, By.XPATH, select_automatizacion_formacionWeb)
        funciones_TyP.click_Field(self, By.XPATH, select_automatizacion_formacionWeb)

    '''def click_guardar_formacionOrigen(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_guardar_formacionOrigen)
        title_guardar_formacionOrigen = self.driver.find_element(self, By.XPATH, "(//div[@class='alert alert-success']//div)[2]")
        if title_guardar_formacionOrigen.is_displayed():
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click boton guardar formacion origen **")
        else:
            print("** hay un fallo en el step: Click boton guardar formacion origen **")
            assert False, "** hay un fallo en el step: Click boton guardar formacion origen **"'''

    def mod_nom_formacionOrigen(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_formacionOrigen, "Formacion Origen")