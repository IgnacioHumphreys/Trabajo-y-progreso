from behave import *
from pages.buscar_reparticion_05_page import buscar_reparticion

@when(u'Escribir reparticion')
def step_impl(context):
    buscar_reparticion.escribir_reparticion(context)


@then(u'Click boton buscar reparticion y validar')
def step_impl(context):
    buscar_reparticion.click_buscar(context)