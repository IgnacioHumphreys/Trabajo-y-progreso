import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_back import *
from selenium.webdriver import ActionChains

t = 1

class ABM_grupos(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def click_grupos(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_grupos)
        title_grupos = self.driver.find_element(By.XPATH,"//div[@class='col']//h1[1]")
        if title_grupos.is_displayed():
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click grupos **")
        else:
            self.driver.quit()
            print("** hay un fallo en el step: Click grupos **")
            assert False, "** hay un fallo en el step: Click grupos **"

    def com_nom_grupo(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_grupo, "Cursos faciles")

    def click_switch(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_switch)

    def select_capacitaciones(self):
        act = ActionChains(self.driver)
        #Scrool hasta una capacitacion
        '''funciones_TyP.scrollToElement(self, By.XPATH, "//p[text()='10000000002']")
        time.sleep(t)'''
        #Click a capacitacion
        check1 = self.driver.find_element(By.ID, "customCheck2")
        check1.click()
        '''funciones_TyP.click_Field(self, By.XPATH, select_capacitacion1)
        elemento = self.driver.find_element(By.ID, "customCheck2")
        act.click(elemento).perform()
        time.sleep(t)'''
        #Scrool hasta otra capacitacion
        '''funciones_TyP.scrollToElement(self, By.ID, select_capacitacion2)'''
        # Click a capacitacion
        check2 = self.driver.find_element(By.ID, "customCheck1")
        check2.click()

    def click_publicar(self):
        funciones_TyP.scrollToElement(self, By.XPATH, btn_publicar)
        funciones_TyP.click_Field(self, By.XPATH, btn_publicar)
        title_grupos_publicado = self.driver.find_element(By.XPATH, "(//div[@class='alert alert-success']//div)[2]")
        if title_grupos_publicado.is_displayed():
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click boton publicar **")
        else:
            self.driver.quit()
            print("** hay un fallo en el step: Click boton publicar **")
            assert False, "** hay un fallo en el step: Click boton publicar **"

    def click_editar(self):
        funciones_TyP.scrollToElement(self, By.XPATH, btn_editar_grupo)
        funciones_TyP.click_Field(self, By.XPATH, btn_editar_grupo)
        editar_grupo = self.driver.find_element(By.XPATH, "//h2[@class='d-inline m-0']")
        if editar_grupo.is_displayed():
            funciones_TyP.screenShot(self, "Editar grupo")
            print("** valido el step: Click icono editar grupo **")
        else:
            self.driver.quit()
            print("** hay un fallo en el step: Click icono editar grupo **")
            assert False, "** hay un fallo en el step: Click icono editar grupo **"

    def mod_nom_grupo(self):
        act = ActionChains(self.driver)
        elemento = self.driver.find_element(By.XPATH, input_grupo)
        act.double_click(elemento).double_click(elemento).perform()
        funciones_TyP.input_Texto(self, By.XPATH, input_grupo, "Cursos promedio")

    def click_tachito(self):
        funciones_TyP.scrollToElement(self, By.XPATH, btn_tachito_grupo)
        funciones_TyP.click_Field(self, By.XPATH, btn_tachito_grupo)
        editar_grupo = self.driver.find_element(By.XPATH, "//div[@class='modal-header']//h5[1]")
        if editar_grupo.is_displayed():
            funciones_TyP.screenShot(self, "Eliminar grupo")
            print("** valido el step: Click icono tachito grupo **")
        else:
            self.driver.quit()
            print("** hay un fallo en el step: Click icono tachito grupo **")
            assert False, "** hay un fallo en el step: Click icono tachito grupo **"

    '''def click_guardar_grupo(self):
        funciones_TyP.scrollToElement(self, By.XPATH, btn_guardar)
        funciones_TyP.click_Field(self, By.XPATH, btn_guardar)
        title_grupo_editado = self.driver.find_element(By.XPATH, "(//div[@class='container-fluid content']//div)[1]")
        if title_grupo_editado.is_displayed():
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click boton guardar grupo **")
        else:
            self.driver.quit()
            print("** hay un fallo en el step: Click boton guardar grupo **")
            assert False, "** hay un fallo en el step: Click boton guardar grupo **"'''