from behave import *
from pages.login_back_01_page import LoginPage

@given(u'Ingreso al portal de oportunidades')
def step_impl(context):
    LoginPage.openBrowser(context)


@when(u'Validar logo pagina')
def step_impl(context):
    LoginPage.validarLogo(context)


@when(u'Completar credenciales de inicio de sesion')
def step_impl(context):
    LoginPage.completar_credenciales(context)


@then(u'Click boton ingresar')
def step_impl(context):
    LoginPage.click_ingresar(context)