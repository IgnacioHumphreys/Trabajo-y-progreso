from behave import *
from pages.buscar_categoriaWeb_07_page import buscar_categoriaWeb

@when(u'Escribir categoriaWeb')
def step_impl(context):
    buscar_categoriaWeb.escribir_categoriaWeb(context)


@then(u'Click boton buscar categoriaWeb')
def step_impl(context):
    buscar_categoriaWeb.click_buscar(context)