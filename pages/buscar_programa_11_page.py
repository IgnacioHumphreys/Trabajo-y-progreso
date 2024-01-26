import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_configuracion import *

t = 1

class buscar_programa(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def escribir_codigo(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_cod_programa_buscar, "2310")

    def escribir_nom_programa(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_nom_programa_buscar, "Programa (Automatización)")

    def seleccionar_ministerio_en_programa(self):
        funciones_TyP.click_Field(self, By.XPATH, box3_ministerio)
        funciones_TyP.scrollToElement(self, By.XPATH, select_automatizaion_en_programa)
        funciones_TyP.click_Field(self, By.XPATH, select_automatizaion_en_programa)