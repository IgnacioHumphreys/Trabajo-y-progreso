import time
from selenium.webdriver.common.by import By
from Funciones.funciones_TyP import funciones_TyP
from elements.elementos_back import *
from selenium.webdriver import ActionChains

t = 1

class alta_capacitacion(funciones_TyP):

    def __init__(self, driver):
        super().__init__(driver)

    def click_capacitaciones(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_capacitaciones)
        time.sleep(t)
        title_capacitaciones = self.driver.find_element(By.XPATH, "//div[@class='col']//h1[1]")
        if title_capacitaciones.is_displayed():
            funciones_TyP.screenShot(self, "pantalla esperada")
            print("** valido el step: Click capacitaciones **")
        else:
            print("** hay un fallo en el step: Click capacitaciones **")
            assert False, "** hay un fallo en el step: Click capacitaciones **"

    def completar_campos(self):
        #Selecciona un programa
        funciones_TyP.click_Field(self, By.XPATH, box3_programa)
        funciones_TyP.scrollToElement(self, By.XPATH, select_programa)
        funciones_TyP.click_Field(self, By.XPATH, select_programa)
        #Ingresa codigo de la capacitacion
        funciones_TyP.input_Texto(self, By.XPATH, input_cod_capacitacion, "25889")
        #Ingresa nombre del curso
        funciones_TyP.input_Texto(self, By.XPATH, input_nom_curso, "QA automation")
        #Ingresa el detalle
        funciones_TyP.input_Texto(self, By.XPATH, input_detalle,
                            "En este curso se aprenderan los primeros pasos para ser un QA utilizando selenium")
        #Carga imagen
        funciones_TyP.subirArchivo(self, By.XPATH, up_imagen,
                "'C:\\Users\\ignac\\Documents\\Automatizaciones_ASI\\trabajo_y_progreso\\IMG\\python.jpg'")
        #Selecciona tipo de formacion
        funciones_TyP.scrollToElement(self, By.XPATH, box_tipoFormacion)
        self.driver.execute_script("window.scrollTo(0,100)")
        funciones_TyP.click_Field(self, By.XPATH, box_tipoFormacion)
        funciones_TyP.scrollToElement(self, By.XPATH, select_formacionOrigen)
        funciones_TyP.click_Field(self, By.XPATH, select_formacionOrigen)
        #time.sleep(3)
        #Selecciona la modalidad
        funciones_TyP.click_Field(self, By.XPATH, box_modalidad)
        funciones_TyP.click_Field(self, By.XPATH, select_virtual)
        #Selecciona el nivel
        funciones_TyP.click_Field(self, By.XPATH, box_nivel)
        funciones_TyP.click_Field(self, By.XPATH, select_basico)
        #Selecciona la aptitud
        funciones_TyP.click_Field(self, By.XPATH, box_aptutud)
        #funciones_TyP.scrollToElement(self, By.XPATH, select_creatividad)
        #self.driver.execute_script("window.scrollTo(0,10)")
        funciones_TyP.click_Field(self, By.XPATH, select_creatividad)
        #Selecciona el sector productivo
        '''funciones_TyP.click_Field(self, By.XPATH, box_sectorProductivo)
        funciones_TyP.scrollToElement(self, By.XPATH, select_origenTest)
        funciones_TyP.click_Field(self, By.XPATH, select_origenTest)'''
        #Selecciona la habilidad
        funciones_TyP.click_Field(self, By.XPATH, box_habilidad)
        funciones_TyP.scrollToElement(self, By.XPATH, select_categoriaOrigen)
        funciones_TyP.click_Field(self, By.XPATH, select_categoriaOrigen)
        #Selecciona categoria web
        funciones_TyP.click_Field(self, By.XPATH, box2_categoriaWeb)
        funciones_TyP.click_Field(self, By.XPATH, select_categoriaWeb)
        #Selecciona seccion
        funciones_TyP.click_Field(self, By.XPATH, box_seccion)
        funciones_TyP.click_Field(self, By.XPATH, select_ambas)
        #Selecciona etiqueta
        funciones_TyP.click_Field(self, By.XPATH, box_etiqueta)
        funciones_TyP.click_Field(self, By.XPATH, select_curso)
        #Completa el contenido del curso
        act = ActionChains(self.driver)
        elemento = self.driver.find_element(By.XPATH, input_contenido)
        act.click(elemento).send_keys(
            "En este curso se vera el idioma de programacion python, junto con otras tecnologias").perform()
        #Completa requerimientos
        funciones_TyP.scrollToElement(self, By.XPATH, input_requisitos)
        act = ActionChains(self.driver)
        elemento = self.driver.find_element(By.XPATH, input_requisitos)
        act.click(elemento).send_keys("Conexion a internet y no se requieren conocimientos previos").perform()
        #Completa materiales
        funciones_TyP.scrollToElement(self, By.ID, input_materiales)
        act = ActionChains(self.driver)
        elemento = self.driver.find_element(By.ID, input_materiales)
        act.click(elemento).send_keys("Una computadora").perform()
        #Completa duracion cantidad
        funciones_TyP.input_Texto(self, By.XPATH, input_duracionCantidad, "4")
        #Selecciona duracion estimada
        funciones_TyP.click_Field(self, By.XPATH, box_duracionEstimada)
        funciones_TyP.scrollToElement(self, By.XPATH, select_meses)
        funciones_TyP.click_Field(self, By.XPATH, select_meses)
        #Ingresa el precio
        funciones_TyP.input_Texto(self, By.XPATH, input_precio, "25000")
        #Ingresa link
        funciones_TyP.input_Texto(self, By.XPATH, input_link, "https://ar.pinterest.com/")
        time.sleep(30)

    def click_guardar_borrador(self):
        funciones_TyP.click_Field(self, By.XPATH, btn_guardar_borrador)
        title_curso_creado = self.driver.find_element(By.XPATH, "(//div[@class='alert alert-success']//div)[2]")
        QA_automation = self.driver.find_element(By.XPATH, "//p[text()='QA automation']")
        texto = QA_automation.text
        texto_comparativo = "QA automation"
        if title_curso_creado.is_displayed() and texto_comparativo == texto:
            funciones_TyP.screenShot(self, "Se valida la creacion de la capacitacion")
            print("** valido el step: Click guardar como borrador y validar **")
        else:
            print("** hay un fallo en el step: Click guardar como borrador y validar **")
            assert False, "** hay un fallo en el step: Click guardar como borrador y validar **"

    def click_cargar(self):
        funciones_TyP.scrollToElement(self, By.XPATH, btn_cargar)
        funciones_TyP.click_Field(self, By.XPATH, btn_cargar)