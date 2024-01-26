from behave import *
from pages.buscar_programa_11_page import buscar_programa

@when(u'Escribir codigo programa')
def step_impl(context):
    buscar_programa.escribir_codigo(context)


@when(u'Escribir nombre programa')
def step_impl(context):
    buscar_programa.escribir_nom_programa(context)


@when(u'Seleccionar ministerio en programa')
def step_impl(context):
    buscar_programa.seleccionar_ministerio_en_programa(context)