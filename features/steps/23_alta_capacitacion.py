from behave import*
from pages.back_end_pages.alta_capacitacion_23_page import alta_capacitacion

@when(u'Click capacitaciones')
def step_impl(context):
    alta_capacitacion.click_capacitaciones(context)


@when(u'Completar todos los campos')
def step_impl(context):
    alta_capacitacion.completar_campos(context)


@then(u'Click guardar como borrador y validar')
def step_impl(context):
    alta_capacitacion.click_guardar_borrador(context)


@when(u'Click boton cargar')
def step_impl(context):
    alta_capacitacion.click_cargar(context)


@when(u'Cargar datos de edicion')
def step_impl(context):
    alta_capacitacion.cargar_datos_edicion(context)


@then(u'Click boton crear y validar')
def step_impl(context):
    alta_capacitacion.click_crear(context)


@when(u'Cambiar estado')
def step_impl(context):
    alta_capacitacion.cambiar_estado(context)