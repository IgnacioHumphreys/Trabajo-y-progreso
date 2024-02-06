from behave import*
from pages.back_end_pages.buscar_tipoFormacionWeb_18_page import buscar_formacionWeb

@when(u'Escribir formacion web')
def step_impl(context):
    buscar_formacionWeb.escribir_formacionWeb(context)


@then(u'Click boton buscar formacion web y validar')
def step_impl(context):
    buscar_formacionWeb.click_buscar(context)