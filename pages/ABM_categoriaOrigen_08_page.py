import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_configuracion import *

t = 1

class ABM_categoriaOrigen(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def click_categoriasOrigen(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_categoriasOrigen)
        time.sleep(t)
        title_categoriasOrigen = self.driver.find_element(self, By.XPATH, "//a[@id='categoriasWeb']/following-sibling::a[1]")
        if title_categoriasOrigen is True:
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click categoriasOrigen **")
        else:
            print("** hay un fallo en el step: Click categoriasOrigen **")
            assert False, "** hay un fallo en el step: Click categoriasOrigen **"

    def com_nom_categoriaOrigen(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_categoriaOrigen, "Categoria")

    def seleccionar_tipo(self):
        funciones_TyP.click_Field(self, By.XPATH, box_tipo)
        funciones_TyP.click_Field(self, By.XPATH, select_empleo)

    def asociar_categoriaWeb(self):
        funciones_TyP.click_Field(self, By.XPATH, box_categoriaWeb)
        funciones_TyP.scrollToElement(self, By.XPATH, select_categoriaWebAuto)
        time.sleep(t)
        funciones_TyP.click_Field(self, By.XPATH, select_categoriaWebAuto)

    def click_guardar_categoriaOrigen(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_guardar_categoriaOrigen)
        title_guardar_categoriaOrigen = self.driver.find_element(self, By.XPATH,
                                                          "(//div[@class='alert alert-success']//div)[2]")
        if title_guardar_categoriaOrigen is True:
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click boton guardar categoriaOrigen **")
        else:
            print("** hay un fallo en el step: Click boton guardar categoriaOrigen **")
            assert False, "** hay un fallo en el step: Click boton guardar categoriaOrigen **"

    def mod_nom_categoriaOrigen(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_categoriaOrigen, "Categoria 2")

    def mod_tipo(self):
        funciones_TyP.click_Field(self, By.XPATH, box_tipo)
        funciones_TyP.click_Field(self, By.XPATH, select_habilidad)