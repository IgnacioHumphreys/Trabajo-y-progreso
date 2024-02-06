from behave import*
from pages.back_end_pages.buscar_institucion_22_page import buscar_institucion

@when(u'Escribir codigo institucion')
def step_impl(context):
    buscar_institucion.escribir_cod_institucion(context)


@when(u'Escribir nombre institucion')
def step_impl(context):
    buscar_institucion.escribir_nom_institucion(context)


@then(u'Click boton buscar institucion y validar')
def step_impl(context):
    buscar_institucion.click_buscar_instituion(context)