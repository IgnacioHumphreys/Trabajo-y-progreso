import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_front import *
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys

t = 2

class LoginPage_front(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def openBrowser(self):
        funciones_TyP.driver_Chrome(self)
        funciones_TyP.browser(self, URL_front)
        time.sleep(5)

    def validar_logo(self):
        funciones_TyP.validates_visibility(self, By.XPATH, logoBa_front)
        funciones_TyP.screenShot(self, "Ingreso al front ofertas de educacion")

    def click_tu_cuenta(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_tuCuenta)
        title_ingresa_tu_cuenta = self.driver.find_element(By.XPATH, "//h1[text()='Ingresá a tu cuenta de la Ciudad']")
        if title_ingresa_tu_cuenta.is_displayed():
            funciones_TyP.screenShot(self, "Inicio de sesion")
            print("** valido el step: Click accede a tu cuenta **")
        else:
            self.driver.quit()
            print("** hay un fallo: Click accede a tu cuenta **")
            assert False, "** hay un fallo: Click accede a tu cuenta **"

    def click_ingreso_miBA(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_ingreso_miBA)
        title_cuenta_ciudad = self.driver.find_element(By.XPATH, "//h1[text()='Ingresá a tu cuenta de la Ciudad']")
        if title_cuenta_ciudad.is_displayed():
            funciones_TyP.screenShot(self, "Inicio de sesion para ingresar credenciales")
            print("** valido el step: Click ingreso por miBA **")
        else:
            self.driver.quit()
            print("** hay un fallo: Click ingreso por miBA **")
            assert False, "** hay un fallo: Click ingreso por miBA **"

    def ingresar_mail(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_email, email)

    def ingresar_clave(self):
        funciones_TyP.input_Texto(self, By.XPATH, input_clave, clave)

    def click_ingresar(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_ingresar)
        title_mi_perfil = self.driver.find_element(By.XPATH, "//span[text()='Mi perfil']")
        if title_mi_perfil.is_displayed():
            funciones_TyP.screenShot(self, "Sesion iniciada")
            print("** valido el step: Click boton ingresar y validar el inicio de sesion **")
        else:
            self.driver.quit()
            print("** hay un fallo: Click boton ingresar y validar el inicio de sesion **")
            assert False, "** hay un fallo: Click boton ingresar y validar el inicio de sesion **"