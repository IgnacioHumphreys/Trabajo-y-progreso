import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_front import *
from selenium.webdriver import ActionChains

t = 2

class deshabilitar_capacitacion(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def click_deshabilitar(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_deshabilitar)