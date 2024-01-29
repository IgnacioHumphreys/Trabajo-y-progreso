from behave import *
from pages.buscar_aptitudes_14_page import buscar_aptitud

@when(u'Escribir aptitud')
def step_impl(context):
    buscar_aptitud.escribir_aptitud(context)


@then(u'Click boton buscar aptitud')
def step_impl(context):
    buscar_aptitud.click_buscar(context)