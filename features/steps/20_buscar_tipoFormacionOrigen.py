from behave import*
from pages.back_end_pages.buscar_tipoFormacionOrien_20_page import buscar_tipoFormacionOrigen

@when(u'Escribir formacion origen')
def step_impl(context):
    buscar_tipoFormacionOrigen.escribir_tipoFormacionOrigen(context)


@then(u'Click boton buscar formacion origen y validar')
def step_impl(context):
    buscar_tipoFormacionOrigen.click_buscar(context)