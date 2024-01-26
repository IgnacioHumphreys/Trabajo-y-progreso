import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_configuracion import *

t = 1

class buscar_categoriaOrigen(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def escribir_categoriaOrigen(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_categoriaOrigen, "CategoríaOrigen (automatizacion)")
        time.sleep(t)

    def escribir_categoriaWeb_en_origen(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_categoriaWeb_en_origen, "CategoríaWeb (automatización)")