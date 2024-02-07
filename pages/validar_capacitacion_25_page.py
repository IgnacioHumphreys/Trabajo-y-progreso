import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_front import *
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys

t = 2

class validar_capacitacion(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def click_buscar_en_educacion(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_buscar_en_educacion)

    def select_cateogoria(self):
        funciones_TyP.click_Field(self, By.XPATH, box_categoria)
        funciones_TyP.scrollToElement(self, By.XPATH, select_categoria)
        funciones_TyP.click_Field(self, By.XPATH, select_categoria)

    def click_buscar(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_buscar)
        title_QAautomation = self.driver.find_element(By.XPATH, "//h4[text()='QA automation']")
        if title_QAautomation.is_displayed():
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click buscar y validar **")
        else:
            print("** hay un fallo en el step: Click buscar y validar **")
            assert False, "** hay un fallo en el step: Click buscar y validar **"

    def click_capacitacion(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_capacitacion)
        title_inscripcionHasta = self.driver.find_element(By.XPATH, "//p[text()='Inscripción hasta:']")
        if title_inscripcionHasta.is_displayed():
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click en la capacitacion **")
        else:
            print("** hay un fallo en el step: Click en la capacitacion **")
            assert False, "** hay un fallo en el step: Click en la capacitacion **"

    def click_inscribirme(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_inscribirme)
        time.sleep(3)
        '''logo_pinterest = self.driver.find_element(By.XPATH, "//h1[text()='Pinterest']")
        texto = logo_pinterest.text
        texto_comparativo = "Pinterest"
        if texto == texto_comparativo:
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click inscribirme **")
        else:
            print("** hay un fallo en el step: Click inscribirme **")
            assert False, "** hay un fallo en el step: Click inscribirme **"'''