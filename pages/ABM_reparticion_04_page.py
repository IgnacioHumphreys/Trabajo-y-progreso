import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_back import *
from selenium.webdriver import ActionChains

t = 1

class ABM_reparticion(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def click_reparticiones(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_reparticiones)
        time.sleep(t)
        title_reparticiones = self.driver.find_element(By.XPATH, "//div[@class='col']//h1[1]")
        if title_reparticiones.is_displayed():
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click reparticiones **")
        else:
            self.driver.quit()
            print("** hay un fallo en el step: Click reparticiones **")
            assert False, "** hay un fallo en el step: Click reparticiones **"

    def com_nom_reparticion(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_reparticion, "Sistemas")

    def asociar_ministerio(self):
        funciones_TyP.click_Field(self, By.XPATH, box_ministerio)
        funciones_TyP.scrollToElement(self, By.XPATH, select_automatizacion)
        funciones_TyP.click_Field(self, By.XPATH, select_automatizacion)
        time.sleep(t)

    '''def click_guardar_reparticion(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_guardar_reparticion)
        time.sleep(t)
        title_reparticion_guardada = self.driver.find_element(By.XPATH, "(//div[@class='alert alert-success']//div)[2]")
        if title_reparticion_guardada.is_displayed():
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click boton guardar reparticion **")
            funciones_TyP.validates_visibility(self, By.XPATH, "(//table[@class='table table-hover']//p)[1]")
        else:
            self.driver.quit()
            print("** hay un fallo en el step: Click boton guardar reparticion **")
            assert False, "** hay un fallo en el step: Click boton guardar reparticion **"'''

    def mod_nom_reparticion(self):
        act = ActionChains(self.driver)
        elemento = self.driver.find_element(By.XPATH, input_reparticion)
        act.double_click(elemento).perform()
        funciones_TyP.input_Texto(self, By.XPATH, input_reparticion, "Sistemas 2")