from behave import *
from pages.front_end_pages.login_front_24_page import LoginPage_front

@given(u'Ingreso a ofertas de educacion')
def step_impl(context):
    LoginPage_front.openBrowser(context)


@then(u'Validar logo pagina front')
def step_impl(context):
    LoginPage_front.validar_logo(context)
