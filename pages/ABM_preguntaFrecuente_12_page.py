import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_back import *

t = 1

class ABM_pregunta_frecuente(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def click_preguntas_frecuentes(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_preguntasFrecuentes)
        title_preguntasFrecuentes = self.driver.find_element(self, By.XPATH,
                                    "//div[contains(@class,'d-flex align-items-center')]//h2[1]")
        if title_preguntasFrecuentes is True:
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click preguntas frecuentes **")
        else:
            print("** hay un fallo en el step: Click preguntas frecuentes **")
            assert False, "** hay un fallo en el step: Click preguntas frecuentes **"

    def select_ministerio_en_preguntaFrecuente(self):
        funciones_TyP.click_Field(self, By.XPATH, box4_ministerio)
        funciones_TyP.scrollToElement(self, By.XPATH, select_automatizacion)
        funciones_TyP.click_Field(self, By.XPATH, select_automatizacion)

    def select_programa(self):
        funciones_TyP.click_Field(self, By.XPATH, box_programa)
        funciones_TyP.scrollToElement(self, By.XPATH, select_programa)
        funciones_TyP.click_Field(self, By.XPATH, select_programa)

    def select_capacitacion(self):
        funciones_TyP.click_Field(self, By.XPATH, box_capacitacion)
        funciones_TyP.scrollToElement(self, By.XPATH, select_python)
        funciones_TyP.click_Field(self, By.XPATH, select_python)

    def com_pregunta(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_pregunta, "Cuales son los requerimientos?")

    def com_respuesta(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_respuesta, "Ninguno")

    '''def click_guardar_preguntaFrecuente(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_guardar)
        title_guardar_preguntasFrecuentes = self.driver.find_element(self, By.XPATH,
                                                            "(//div[@class='alert alert-success']//div)[2]")
        if title_guardar_preguntasFrecuentes is True:
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click boton guardar preguntas frecuentes **")
            funciones_TyP.validates_visibility(self, By.XPATH, "//h5[text()='Cuales son los requerimientos?']")
        else:
            print("** hay un fallo en el step: Click boton guardar preguntas frecuentes **")
            assert False, "** hay un fallo en el step: Click boton guardar preguntas frecuentes **"'''


    def click_editar_preguntasFrecuentes(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_editar_preguntasFrecuentes)
        title_editar_preguntasFrecuentes = self.driver.find_element(self, By.XPATH,
                                                             "//div[contains(@class,'d-flex align-items-center')]//h2[1]")
        if title_editar_preguntasFrecuentes is True:
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click icono editar preguntas frecuentes **")
        else:
            print("** hay un fallo en el step: Click icono editar preguntas frecuentes **")
            assert False, "** hay un fallo en el step: Click icono editar preguntas frecuentes **"

    def mod_pregunta(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_pregunta, "Cuales son los requisitos")

    def mod_respuesta(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_respuesta, "Tener una computadora con internet")

    def click_tachito_preguntasFreuentes(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_tachito_preguntaFrecuente)
        title_eliminar_preguntaFrecuente = self.driver.find_element(self, By.XPATH,
                                                                    "//div[@class='modal-header']//h5[1]")
        if title_eliminar_preguntaFrecuente is True:
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click icono tachito pregunta frecuente **")
        else:
            print("** hay un fallo en el step: Click icono tachito pregunta frecuente **")
            assert False, "** hay un fallo en el step: Click icono tachito pregunta frecuente **"

    def click_eliminar_preguntaFrecuente(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_eliminar_preguntaFrecuente)
        title_preguntaFrecuente_eliminada = self.driver.find_element(self, By.XPATH,
                                                            "(//div[@class='alert alert-success']//div)[2]")
        if title_preguntaFrecuente_eliminada is True:
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click boton eliminar pregunta frecuente **")
        else:
            print("** hay un fallo en el step: Click boton eliminar pregunta frecuente **")
            assert False, "** hay un fallo en el step: Click icono tacboton eliminar frecuente **"