from behave import *
from pages.buscar_categoriaOrigen_09_page import buscar_categoriaOrigen

@when(u'Escribir categoriaOrigen')
def step_impl(context):
    buscar_categoriaOrigen.escribir_categoriaOrigen(context)


@when(u'Escribir categoriaWeb en CategoriasOrigen')
def step_impl(context):
    buscar_categoriaOrigen.escribir_categoriaWeb_en_origen(context)


@then(u'Click boton buscar categoriaOrigen')
def step_impl(context):
    buscar_categoriaOrigen.click_buscar(context)