from behave import*
from pages.alta_capacitacion_23_page import alta_capacitacion

@when(u'Click capacitaciones')
def step_impl(context):
    alta_capacitacion.click_capacitaciones(context)


@when(u'Completar todos los campos')
def step_impl(context):
    alta_capacitacion.completar_campos(context)


@then(u'Click guardar como borrador y validar')
def step_impl(context):
    alta_capacitacion.click_guardar_borrador(context)


@then(u'Click boton cargar')
def step_impl(context):
    alta_capacitacion.click_cargar(context)
