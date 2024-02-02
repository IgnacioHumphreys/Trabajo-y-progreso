from behave import *
from pages.buscar_ministerio_03_page import buscar_ministerio

@when(u'Escribir ministerio')
def step_impl(context):
    buscar_ministerio.escribir_ministerio(context)


@then(u'Click boton buscar ministerio y validar')
def step_impl(context):
    buscar_ministerio.click_buscar_ministerio(context)