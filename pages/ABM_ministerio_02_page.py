import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_back import *
from selenium.webdriver import ActionChains

t = 1

class ABM_ministerio(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def click_config(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_configuracion)
        ministerios = self.driver.find_element(By.XPATH, "//div[@id='configuracionCollapse']//a[1]")
        if ministerios.is_displayed():
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click configuracion **")
        else:
            self.driver.quit()
            print("** hay un fallo en el step: Click configuracion **")
            assert False, "** hay un fallo en el step: Click configuracion **"

    def click_ministerios(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_ministerios)
        time.sleep(t)
        title_ministerios = self.driver.find_element(By.XPATH, "//h1[@class='m-0']")
        if title_ministerios.is_displayed():
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click ministerios **")
        else:
            self.driver.quit()
            print("** hay un fallo en el step: Click ministerios **")
            assert False, "** hay un fallo en el step: Click ministerios **"

    def click_btn_crear(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_crear)
        time.sleep(t)
        title_crear_ministerio = self.driver.find_element(By.XPATH,
                                "//div[contains(@class,'d-flex align-items-center')]//h2[1]")
        if title_crear_ministerio.is_displayed():
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click boton crear **")
        else:
            self.driver.quit()
            print("** hay un fallo en el step: Click boton crear **")
            assert False, "** hay un fallo en el step: Click boton crear **"

    def comp_nom_ministerio(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_ministerio, "MDT2")
        time.sleep(t)

    def click_guardar(self):
        funciones_TyP.scrollToElement(self, By.XPATH, btn_guardar)
        funciones_TyP.click_Field(self, By.XPATH, btn_guardar)
        time.sleep(t)
        title_guardado = self.driver.find_element(By.XPATH,"(//div[@class='alert alert-success']//div)[2]")
        if title_guardado.is_displayed():
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click boton guardar ministerio **")
            funciones_TyP.validates_visibility(self, By.XPATH, "(//table[@class='table table-hover']//p)[1]")
        else:
            self.driver.quit()
            print("** hay un fallo en el step: Click boton guardar**")
            assert False, "** hay un fallo en el step: Click boton guardar**"

    def click_editar(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_editar)
        editar_ministerio = self.driver.find_element(By.XPATH, "//h2[@class='d-inline m-0']")
        if editar_ministerio.is_displayed():
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click icono editar **")
        else:
            self.driver.quit()
            print("** hay un fallo en el step: Click icono editar **")
            assert False, "** hay un fallo en el step: Click icono editar **"

    def mod_nom_ministerio(self):
        act = ActionChains(self.driver)
        elemento = self.driver.find_element(By.XPATH, input_ministerio)
        act.double_click(elemento).perform()
        funciones_TyP.input_Texto(self, By.XPATH, input_ministerio, "MDT2 (automatizacion)")

    def click_tachito(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_tachito)
        title_eliminar_min = self.driver.find_element(By.XPATH, "//div[@class='modal-header']//h5[1]")
        if title_eliminar_min.is_displayed():
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click icono tachito **")
        else:
            self.driver.quit()
            print("** hay un fallo en el step: Click icono tachito **")
            assert False, "** hay un fallo en el step: Click icono tachito **"

    def click_eliminar(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_eliminar)
        title_min_eliminado = self.driver.find_element(By.XPATH, "(//div[@class='alert alert-success']//div)[2]")
        if title_min_eliminado.is_displayed():
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click boton eliminar **")
        else:
            self.driver.quit()
            print("** hay un fallo en el step: Click boton eliminar **")
            assert False, "** hay un fallo en el step: Click boton eliminar **"