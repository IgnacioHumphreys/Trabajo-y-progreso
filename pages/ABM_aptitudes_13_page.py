import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_back import *
from selenium.webdriver import ActionChains

t = 1

class ABM_aptitudes(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def click_aptitudes(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_aptitudes)
        title_aptitudes = self.driver.find_element(By.XPATH, "//div[@class='col']//h1[1]")
        if title_aptitudes.is_displayed():
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click aptitudes **")
        else:
            self.driver.quit()
            print("** hay un fallo en el step: Click aptitudes **")
            assert False, "** hay un fallo en el step: Click aptitudes **"

    def com_nom_aptutud(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_aptitud, "Ingenio")

    '''def click_guardar_aptitud(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_guardar)
        title_guardar_aptitud = self.driver.find_element(By.XPATH, "(//div[@class='alert alert-success']//div)[2]")
        if title_guardar_aptitud.is_displayed():
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click boton guardar aptitud **")
            funciones_TyP.validates_visibility(self, By.XPATH, "(//table[@class='table table-hover']//p)[1]")
        else:
            self.driver.quit()
            print("** hay un fallo en el step: Click boton guardar aptitud **")
            assert False, "** hay un fallo en el step: Click boton guardar aptitud **"'''

    def mod_nom_aptitud(self):
        act = ActionChains(self.driver)
        elemento = self.driver.find_element(By.XPATH, input_aptitud)
        act.double_click(elemento).perform()
        funciones_TyP.input_Texto(self, By.XPATH, input_aptitud, "Ingenio 2")