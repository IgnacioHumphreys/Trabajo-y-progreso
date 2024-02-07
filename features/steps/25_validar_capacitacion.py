from behave import *
from pages.validar_capacitacion_25_page import validar_capacitacion

@when(u'Click buscar en educacion')
def step_impl(context):
    validar_capacitacion.click_buscar_en_educacion(context)


@when(u'Seleccionar categoria')
def step_impl(context):
    validar_capacitacion.select_cateogoria(context)


@then(u'Click buscar y validar')
def step_impl(context):
    validar_capacitacion.click_buscar(context)


@when(u'Click en la capacitacion')
def step_impl(context):
    validar_capacitacion.click_capacitacion(context)


@then(u'Click inscribirme')
def step_impl(context):
    validar_capacitacion.click_inscribirme(context)