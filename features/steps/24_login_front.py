from behave import *
from pages.login_front_24_page import LoginPage_front

@given(u'Ingreso a ofertas de educacion')
def step_impl(context):
    LoginPage_front.openBrowser(context)


@when(u'Validar logo pagina front')
def step_impl(context):
    LoginPage_front.validar_logo(context)


@when(u'Click accede a tu cuenta')
def step_impl(context):
    LoginPage_front.click_tu_cuenta(context)


@when(u'Click ingreso por miBA')
def step_impl(context):
    LoginPage_front.click_ingreso_miBA(context)


@when(u'Ingresa el "noecoppo@yahoo.com.ar"')
def step_impl(context):
    LoginPage_front.ingresar_mail(context)


@when(u'Ingresa la "Troquel1"')
def step_impl(context):
    LoginPage_front.ingresar_clave(context)


@then(u'Click boton ingresar y validar el inicio de sesion')
def step_impl(context):
    LoginPage_front.click_ingresar(context)