from behave import*
from pages.buscar_grupo_16_page import buscar_grupo

@when(u'Escribir grupo')
def step_impl(context):
    buscar_grupo.escribir_grupo(context)


@then(u'Click boton buscar grupo')
def step_impl(context):
    buscar_grupo.click_buscar(context)