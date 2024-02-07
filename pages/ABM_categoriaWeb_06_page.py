import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_back import *
from selenium.webdriver import ActionChains

t = 1

class ABM_categoriaWeb(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def click_categoriasWeb(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_categoriasWeb)
        time.sleep(t)
        title_categoriasWeb = self.driver.find_element(By.XPATH, "//div[@class='col']//h1[1]")
        if title_categoriasWeb.is_displayed():
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click categoriasWeb **")
        else:
            self.driver.quit()
            print("** hay un fallo en el step: Click categoriasWeb **")
            assert False, "** hay un fallo en el step: Click categoriasWeb **"

    def input_categoriaWeb(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_categoriaWeb, "Computacion")
        time.sleep(t)

    def subir_imagen(self):
        funciones_TyP.subirArchivo(self, By.XPATH, up_imagen,
                'C:\\Users\\ignac\\Documents\\Automatizaciones_ASI\\trabajo_y_progreso\\IMG\\ceros_y_unos.jpg')
        time.sleep(2)

    '''def click_guardar_categoriaWeb(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_guardar)
        time.sleep(t)
        title_guardar_categoriaWeb = self.driver.find_element(By.XPATH, "(//div[@class='alert alert-success']//div)[2]")
        if title_guardar_categoriaWeb.is_displayed():
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click boton guardar categoriasWeb **")
            funciones_TyP.validates_visibility(self, By.XPATH, "(//table[@class='table table-hover']//p)[1]")
        else:
            self.driver.quit()
            print("** hay un fallo en el step: Click boton guardar categoriasWeb **")
            assert False, "** hay un fallo en el step: Click boton guardar categoriasWeb **"'''

    def mod_nom_categoriaWeb(self):
        act = ActionChains(self.driver)
        elemento = self.driver.find_element(By.XPATH, input_categoriaWeb)
        act.double_click(elemento).perform()
        funciones_TyP.input_Texto(self, By.XPATH, input_categoriaWeb, "Computacion 2")