import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_configuracion import *

t = 1

class buscar_reparticion(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def escribir_reparticion(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_reparticion, "DG Políticas de Juventud")