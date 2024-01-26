import os
import time
import allure
import warnings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from allure_commons.types import AttachmentType
#import geckodriver_autoinstaller
##############descomentar para VM #######################
'''from pyvirtualdisplay import Display
from webdriver_manager.chrome import ChromeDriverManager'''


class funciones_TyP:
    def __init__(self, driver):
        self.driver = driver
    ################################## RUN LOCAL  ###############################################
    '''def driver_Firefox(self):  # NAVEGADOR FIREFOX RUTA DEL DRIVE
        self.driver = webdriver.Firefox("\\..\\drivers\\geckodriver")
        s = Service(os.path.join("\\..\\drivers\\geckodriver"))
        self.driver = webdriver.Firefox(service=s)
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)'''

    def driver_Chrome(self):
        chrome_options = Options()
        #chrome_options.add_argument('--incognito')
        #chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-extensions')
        self.driver = webdriver.Chrome(options=chrome_options)

#################################### RUN VM  #################################################

    '''def driver_Firefox(self):  # NAVEGADOR FIREFOX RUTA DEL DRIVE
        self.driver = os.path.join("\\..\\drivers\\geckodriver")
        s = Service(os.path.join("\\..\\drivers\\geckodriver"))
        self.driver = webdriver.Firefox(service=s)
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

    def driver_Chrome(self):
        # self.driver = webdriver.Chrome(os.path.join("\\..\\drivers\\chromedriver"))
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        options.add_argument("--headless")
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        display = Display(visible=0, size=(800, 600))
        display.start()'''


    ############################################################################################
    def browser(self, link):
        try:
            self.driver.get(link)
            self.driver.maximize_window()
            print("Página abierta: " + str(link))
        except Exception as ex:
            allure.attach("Error", str(ex))
            assert False, f"Error Desconocido: {ex}"

    def input_Texto(self, tipo, selector, texto):
        try:
            WebDriverWait(self.driver, timeout=40).until(EC.element_to_be_clickable((tipo, selector))).send_keys(texto)
            time.sleep(1)
            print("\n Escribir en el campo {} el texto -> {} ".format(selector, texto))
        except NoSuchElementException as ex:
            assert False, f"No se escribio el texto debido a que no se encontró el elemento " \
                          f"con el selector '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except ElementNotInteractableException as ex:
            assert False, f"No se escribio el texto debido a que no se puede interactuar con " \
                          f"el elemento '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except TimeoutException as ex:
            assert False, f"No se escribio el texto debido a que el Tiempo de espera fue excedido " \
                          f"para encontrar el elemento '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except Exception as ex:
            allure.attach("Error", str(ex))
            assert False, f"Error Desconocido: {ex}"

    def click_Field(self, tipo, selector):
        try:
            WebDriverWait(self.driver, timeout=40).until(EC.presence_of_element_located((tipo, selector))).click()
            time.sleep(2)
            print("\n Click sobre el elemento -> {} ".format(selector))
        except NoSuchElementException as ex:
            assert False, f"El elemento no pudo clickear debido a que no se encontró el elemento " \
                          f"con el selector '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except ElementNotInteractableException as ex:
            assert False, f"El elemento no pudo clickear debido a que no se puede interactuar con " \
                          f"el elemento '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except TimeoutException as ex:
            assert False, f"El elemento no pudo clickear debido a que el Tiempo de espera fue excedido " \
                          f"para encontrar el elemento '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except Exception as ex:
            allure.attach("Error", str(ex))
            print("Error de ejecución:", str(ex))
            raise ex  # Levanta la excepción para que Jenkins pueda detectarla como un error



    def clear_Field(self, tipo, selector):
        try:
            WebDriverWait(self.driver, timeout=40).until(EC.element_to_be_clickable((tipo, selector))).clear()
            print("\n Texto eliminado -> {} ".format(selector))
        except NoSuchElementException as ex:
            assert False, f"El elemento no pudo limpiar el campo debido a que no se encontró el elemento " \
                          f"con el selector '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except ElementNotInteractableException as ex:
            assert False, f"El elemento no pudo limpiar el campo debido a que no se puede interactuar con " \
                          f"el elemento '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except TimeoutException as ex:
            assert False, f"El elemento no pudo limpiar el campo debido a que el Tiempo de espera fue excedido " \
                          f"para encontrar el elemento '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except Exception as ex:
            allure.attach("Error", str(ex))
            assert False, f"Error Desconocido: {ex}"

    def validates(self, tipo, selector):
        try:
            element = WebDriverWait(self.driver, timeout=40).until(EC.presence_of_element_located((tipo, selector))).text
            print(element)
            print("\n Elemento Validado -> {} ".format(selector))
        except NoSuchElementException as ex:
            assert False, f"El elemento no pudo Validar debido a que no se encontró el elemento " \
                          f"con el selector '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except ElementNotInteractableException as ex:
            assert False, f"El elemento no pudo Validar debido a que no se puede interactuar con " \
                          f"el elemento '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except TimeoutException as ex:
            assert False, f"El elemento no pudo Validar  debido a que el Tiempo de espera fue excedido " \
                          f"para encontrar el elemento '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except Exception as ex:
            allure.attach("Error", str(ex))
            assert False, f"Error Desconocido: {ex}"



    def subirArchivo(self, tipo, selector, ruta):
        try:
            val = self.driver.find_element(tipo, selector)
            val.send_keys(ruta)
            print("\n Elemento Cargado -> {} ".format(selector))
        except NoSuchElementException as ex:
            assert False, f"El elemento no pudo Cargar debido a que no se encontró el elemento " \
                          f"con el selector '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except ElementNotInteractableException as ex:
            assert False, f"El elemento no pudo Cargar debido a que no se puede interactuar con " \
                          f"el elemento '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except TimeoutException as ex:
            assert False, f"El elemento no pudo Cargar  debido a que el Tiempo de espera fue excedido " \
                          f"para encontrar el elemento '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except Exception as ex:
            allure.attach("Error", str(ex))
            assert False, f"Error Desconocido: {ex}"

    def scrollToElement(self, tipo, elemento):
        try:
            val = WebDriverWait(self.driver, timeout=40).until(EC.visibility_of_element_located((tipo, elemento)))
            self.driver.execute_script("arguments[0].scrollIntoView();", val)
            print("\n Desplazando al elemento -> {} ".format(elemento))
        except NoSuchElementException as ex:
            assert False, f"No pudo moverse debido a que no se encontró el elemento " \
                          f"con el selector '{elemento}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except ElementNotInteractableException as ex:
            assert False, f"No pudo moverse debido a que no se puede interactuar con " \
                          f"el elemento '{elemento}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except TimeoutException as ex:
            assert False, f"No pudo moverse  debido a que el Tiempo de espera fue excedido " \
                          f"para encontrar el elemento '{elemento}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except Exception as ex:
            assert False, f"Error Desconocido: {ex}"

        ###################################################################################

    ########################## Allure-Report ##########################################
    ###################################################################################

    def screenShot(self, nombre):
        allure.attach(self.driver.get_screenshot_as_png(), name=nombre, attachment_type=AttachmentType.PNG)

    ###################################################################################
    ########################## ACTION CHAINS ##########################################
    ###################################################################################

    def input_Texto_ActionChains(self, tipo, selector, texto):
        action = ActionChains(self.driver)
        try:
            val = self.driver.find_element(tipo, selector, texto)
            action.click(val).perform()
            action.send_keys(texto).perform()
            time.sleep(1)
        except NoSuchElementException as ex:
            assert False, f"No se pudo ingresar el text debido a que no se encontró el elemento " \
                          f"con el selector '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except ElementNotInteractableException as ex:
            assert False, f"No se pudo ingresar el text debido a que no se puede interactuar con " \
                          f"el elemento '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except TimeoutException as ex:
            assert False, f"No se pudo ingresar el text debido a que el Tiempo de espera fue excedido " \
                          f"para encontrar el elemento '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except Exception as ex:
            allure.attach("Error", str(ex))
            assert False, f"Error Desconocido: {ex}"

    def clickAction(self, tipo, selector):
        action = ActionChains(self.driver)
        try:
            val = self.driver.find_element(tipo, selector)
            action.click(val).perform()
            time.sleep(1)
        except NoSuchElementException as ex:
            assert False, f"No se realizo click action debido a que no se encontró el elemento " \
                          f"con el selector '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except ElementNotInteractableException as ex:
            assert False, f"No se realizo click action debido a que no se puede interactuar con " \
                          f"el elemento '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except TimeoutException as ex:
            assert False, f"No se realizo click action debido a que el Tiempo de espera fue excedido " \
                          f"para encontrar el elemento '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except Exception as ex:
            allure.attach("Error", str(ex))
            assert False, f"Error Desconocido: {ex}"

    def key_Up_Key_Down(self, tecla):
        action = ActionChains(self.driver)
        try:
            action.key_down(tecla).perform()
            action.key_up(tecla).perform()
            time.sleep(1)
        except Exception as ex:
            allure.attach("Error", str(ex))
            assert False, f"Error Desconocido: {ex}"

    ############################################################################################
    ############################ visibility_of_element_located #################################
    ############################################################################################

    def input_Texto_visibility(self, tipo, selector, texto):
        try:
            WebDriverWait(self.driver, timeout=20).until(EC.visibility_of_element_located((tipo, selector))).send_keys(
                texto)
            time.sleep(1)
            print("\n Escribir en el campo {} el texto -> {} ".format(selector, texto))
        except NoSuchElementException as ex:
            assert False, f"No pudo moverse debido a que no se encontró el elemento " \
                          f"con el selector '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except ElementNotInteractableException as ex:
            assert False, f"No pudo moverse debido a que no se puede interactuar con " \
                          f"el elemento '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except TimeoutException as ex:
            assert False, f"No pudo moverse  debido a que el Tiempo de espera fue excedido " \
                          f"para encontrar el elemento '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except Exception as ex:
            allure.attach("Error", str(ex))
            assert False, f"Error Desconocido: {ex}"

    def click_Field_visibility(self, tipo, selector):
        try:
            WebDriverWait(self.driver, timeout=20).until(EC.visibility_of_element_located((tipo, selector))).click()
            time.sleep(2)
            print("\n Click sobre el elemento -> {} ".format(selector))
        except NoSuchElementException as ex:
            assert False, f"No se realizo click debido a que no se encontró el elemento " \
                          f"con el selector '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except ElementNotInteractableException as ex:
            assert False, f"No se realizo click debido a que no se puede interactuar con " \
                          f"el elemento '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except TimeoutException as ex:
            assert False, f"No se realizo click  debido a que el Tiempo de espera fue excedido " \
                          f"para encontrar el elemento '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except Exception as ex:
            allure.attach("Error", str(ex))
            assert False, f"Error Desconocido: {ex}"


    def click_Field_optional(self, tipo, selector):
        try:
            WebDriverWait(self.driver, timeout=20).until(EC.visibility_of_element_located((tipo, selector))).click()
            time.sleep(2)
            print("\n Click sobre el elemento -> {} ".format(selector))
        except NoSuchElementException as ex:
            assert False, f"No se realizo click debido a que no se encontró el elemento " \
                          f"con el selector '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except ElementNotInteractableException as ex:
            assert False, f"No se realizo click debido a que no se puede interactuar con " \
                          f"el elemento '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except TimeoutException as ex:
            assert False, f"No se realizo click debido a que el Tiempo de espera fue excedido " \
                          f"para encontrar el elemento '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except Exception as ex:
            allure.attach("Error", str(ex))
            assert False, f"Error Desconocido: {ex}"

    def validates_visibility(self, tipo, selector):
        try:
            element = WebDriverWait(self.driver, timeout=20).until(
                EC.visibility_of_element_located((tipo, selector))).text
            print(element)
            print("\n Elemento Validado -> {} ".format(selector))
        except NoSuchElementException as ex:
            assert False, f"No se Valido debido a que no se encontró el elemento " \
                          f"con el selector '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except ElementNotInteractableException as ex:
            assert False, f"No se Valido click debido a que no se puede interactuar con " \
                          f"el elemento '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except TimeoutException as ex:
            assert False, f"No se Valido click debido a que el Tiempo de espera fue excedido " \
                          f"para encontrar el elemento '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except Exception as ex:
            allure.attach("Error", str(ex))
            assert False, f"Error Desconocido: {ex}"

    def subirArchivo_visibility(self, tipo, selector, ruta):
        try:
            val = self.driver.find_element(tipo, selector)
            val.send_keys(ruta)
            print("\n Elemento Cargado -> {} ".format(selector))
        except NoSuchElementException as ex:
            assert False, f"El elemento no pudo Cargar debido a que no se encontró el elemento " \
                          f"con el selector '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except ElementNotInteractableException as ex:
            assert False, f"El elemento no pudo Cargar debido a que no se puede interactuar con " \
                          f"el elemento '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except TimeoutException as ex:
            assert False, f"El elemento no pudo Cargar debido a que el Tiempo de espera fue excedido " \
                          f"para encontrar el elemento '{selector}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except Exception as ex:
            allure.attach("Error", str(ex))
            assert False, f"Error Desconocido: {ex}"

    def scrollToElement_visibility(self, tipo, elemento):
        try:
            val = WebDriverWait(self.driver, timeout=40).until(EC.visibility_of_element_located((tipo, elemento)))
            self.driver.execute_script("arguments[0].scrollIntoView();", val)
            print("\n Desplazando al elemento -> {} ".format(elemento))
        except NoSuchElementException as ex:
            assert False, f"No se movio debido a que no se encontró el elemento " \
                          f"con el selector '{elemento}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except ElementNotInteractableException as ex:
            assert False, f"No se movio debido a que no se puede interactuar con " \
                          f"el elemento '{elemento}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except TimeoutException as ex:
            assert False, f"No se movio debido a que el Tiempo de espera fue excedido " \
                          f"para encontrar el elemento '{elemento}' de tipo: '{tipo}'\n Error Log: {ex.msg}"
        except Exception as ex:
            allure.attach("Error", str(ex))
            assert False, f"Error Desconocido: {ex}"

    def findListOfElementsBySelector(self, by_tipo, selector):
        """
        Funcion que retorna una lista de localizadores con el mismo tipo de selector y by_typo.
        :param by_tipo: Ingresar el tipo de selector a usar, si es XPATH, CLASS_NAME, ID, etc.
        :param selector: Ruta de los elementos que se desean encontrar.
        :return: Listado de localizadores que contengan el mismo selector y by_tipo.
        """
        try:
            time.sleep(2)
            val = self.driver.find_elements(by_tipo, selector)
            return val
        except TimeoutException as ex:
            assert False, f"Error: Tiempo de espera agotado mientras se buscaban los " \
                          f"elementos: {selector} de tipo: {by_tipo}\n Log: {ex}"
        except NoSuchElementException as ex:
            assert False, f"Error: No se encontraron los elementos: {selector} de tipo: {by_tipo}\n Log: {ex}"
        except ElementNotInteractableException as ex:
            assert False, f"Error: No se puede interactuar con los elementos: {selector} de tipo: {by_tipo}\n Log: {ex}"
        except Exception as ex:
            assert False, f"Error desconocido: {ex}"


    def scrollToElement_panel_botton(self):
        try:
            self.driver.execute_script("window.scrollTo(0,500)")
        except Exception as ex:
            allure.attach("Error", str(ex))
            assert False, f"Error desconocido al moverse: {ex}"

    def scrollToElement_panel_up(self):
        try:
            self.driver.execute_script("window.scrollTo(600,0)")
        except Exception as ex:
            allure.attach("Error", str(ex))
            assert False, f"Error desconocido al moverse: {ex}"