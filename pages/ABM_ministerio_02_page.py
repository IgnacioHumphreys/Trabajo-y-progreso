import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_configuracion import *

t = 1

class ABM_ministerio(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def click_config(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_configuracion)
        time.sleep(t)
        if btn_ministerios is True:
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click configuracion **")
        else:
            print("** hay un fallo en el step: Click configuracion **")
            assert False, "** hay un fallo en el step: Click configuracion **"

    def click_ministerios(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_ministerios)
        time.sleep(t)
        title_ministerios = self.driver.find_element(self, By.XPATH, "//div[@class='col']//h1[1]")
        if title_ministerios is True:
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click ministerios **")
        else:
            print("** hay un fallo en el step: Click ministerios **")
            assert False, "** hay un fallo en el step: Click ministerios **"

    def click_btn_crear(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_crear)
        time.sleep(t)
        title_crear_ministerio = self.driver.find_element(self, By.XPATH,
                                "//div[contains(@class,'d-flex align-items-center')]//h2[1]")
        if title_crear_ministerio is True:
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click boton crear **")
        else:
            print("** hay un fallo en el step: Click boton crear **")
            assert False, "** hay un fallo en el step: Click boton crear **"

    def comp_nom_ministerio(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_nom_ministerio, "MDT2")
        time.sleep(t)

    def click_guardar(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_guardar)
        ministerio_creado = self.driver.find_element(self, By.XPATH,"(//div[@class='alert alert-success']//div)[2]")
        if ministerio_creado is True:
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click boton guardar **")
        else:
            print("** hay un fallo en el step: Click boton guardar **")
            assert False, "** hay un fallo en el step: Click boton guardar **"

    def click_editar(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_editar)
        editar_ministerio = self.driver.find_element(self, By.XPATH, "(//div[@class='alert alert-success']//div)[2]")
        if editar_ministerio is True:
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click icono editar **")
        else:
            print("** hay un fallo en el step: Click icono editar **")
            assert False, "** hay un fallo en el step: Click icono editar **"

    def mod_nom_ministerio(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_nom_ministerio, "MDT2 (automatizacion)")

    def click_guardar_min(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_guardar)
        ministerio_editado = self.driver.find_element(self, By.XPATH, "((//div[@class='alert alert-success']//div)[2]")
        if ministerio_editado is True:
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click boton guardar ministerio **")
        else:
            print("** hay un fallo en el step: Click boton guardar ministerio **")
            assert False, "** hay un fallo en el step: Click boton guardar ministerio **"

    def click_tachito(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_tachito)
        title_eliminar_min = self.driver.find_element(self, By.XPATH, "//div[@class='modal-header']//h5[1]")
        if title_eliminar_min is True:
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click icono tachito **")
        else:
            print("** hay un fallo en el step: Click icono tachito **")
            assert False, "** hay un fallo en el step: Click icono tachito **"

    def click_eliminar(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_eliminar)
        funciones_TyP.click_Field(self, By.XPATH, btn_tachito)
        title_min_eliminado = self.driver.find_element(self, By.XPATH, "(//div[@class='alert alert-success']//div)[2]")
        if title_min_eliminado is True:
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click boton eliminar **")
        else:
            print("** hay un fallo en el step: Click boton eliminar **")
            assert False, "** hay un fallo en el step: Click boton eliminar **"