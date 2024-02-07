import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_back import *
from selenium.webdriver import ActionChains

t = 1

class ABM_programa(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def click_programas(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_programas)
        time.sleep(t)
        title_programas = self.driver.find_element(By.XPATH, "//div[@class='col']//h1[1]")
        if title_programas.is_displayed():
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click programas **")
        else:
            self.driver.quit()
            print("** hay un fallo en el step: Click programas **")
            assert False, "** hay un fallo en el step: Click programas **"

    def com_cod_programa(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_cod_programa, "2311")

    def com_nom_programa(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_nom_programa, "Programa")

    def select_ministerio(self):
        funciones_TyP.click_Field(self, By.XPATH, box2_ministerio)
        funciones_TyP.scrollToElement(self, By.XPATH, select_automatizacion)
        funciones_TyP.click_Field(self, By.XPATH, select_automatizacion)

    def select_reparticion(self):
        funciones_TyP.click_Field(self, By.XPATH, box_reparticion)
        funciones_TyP.scrollToElement(self, By.XPATH, select_reparticion_auto)
        time.sleep(t)
        funciones_TyP.click_Field(self, By.XPATH, select_reparticion_auto)

    def com_duracion_estimada(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_duracion_estimada, "4 semanas")

    def com_fecha_inscripcion(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_fecha_inscripcion, "18/06")

    '''def click_guardar_programa(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_guardar_programa)
        time.sleep(t)
        title_guardar_programa = self.driver.find_element(By.XPATH, "(//div[@class='alert alert-success']//div)[2]")
        if title_guardar_programa.is_displayed():
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click boton guardar programa **")
            funciones_TyP.validates_visibility(self, By.XPATH, "(//table[@class='table table-hover']//p)[2]")
        else:
            self.driver.quit()
            print("** hay un fallo en el step: Click boton guardar programa **")
            assert False, "** hay un fallo en el step: Click boton guardar programa **"'''

    def mod_cod_programa(self):
        act = ActionChains(self.driver)
        elemento = self.driver.find_element(By.XPATH, input_cod_programa)
        act.double_click(elemento).perform()
        funciones_TyP.input_Texto(self, By.XPATH, input_cod_programa, "2312")

    def mod_nom_programa(self):
        act = ActionChains(self.driver)
        elemento = self.driver.find_element(By.XPATH, input_nom_programa)
        act.double_click(elemento).perform()
        funciones_TyP.input_Texto(self, By.XPATH, input_nom_programa, "Programa 2")

    def mod_fecha_inscripcion(self):
        act = ActionChains(self.driver)
        elemento = self.driver.find_element(By.XPATH, input_fecha_inscripcion)
        act.double_click(elemento).click(elemento).perform()
        funciones_TyP.input_Texto(self, By.XPATH, input_fecha_inscripcion, "18/07")