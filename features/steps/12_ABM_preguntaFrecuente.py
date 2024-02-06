from behave import *
from pages.back_end_pages.ABM_preguntaFrecuente_12_page import ABM_pregunta_frecuente

@when(u'Click preguntasFrecuentes')
def step_impl(context):
    ABM_pregunta_frecuente.click_preguntas_frecuentes(context)


@when(u'Seleccionar ministerio en pregunta frecuente')
def step_impl(context):
    ABM_pregunta_frecuente.select_ministerio_en_preguntaFrecuente(context)


@when(u'Seleccionar programa')
def step_impl(context):
    ABM_pregunta_frecuente.select_programa(context)


@when(u'Seleccionar capacitacion')
def step_impl(context):
    ABM_pregunta_frecuente.select_capacitacion(context)


@when(u'Completar pregunta')
def step_impl(context):
    ABM_pregunta_frecuente.com_pregunta(context)


@when(u'Completar respuesta')
def step_impl(context):
    ABM_pregunta_frecuente.com_respuesta(context)


@when(u'Click icono "editar" preguntas frecuentes')
def step_impl(context):
    ABM_pregunta_frecuente.click_editar_preguntasFrecuentes(context)


@when(u'Modificar pregunta')
def step_impl(context):
    ABM_pregunta_frecuente.mod_pregunta(context)


@when(u'Modificar respuesta')
def step_impl(context):
    ABM_pregunta_frecuente.mod_respuesta(context)


@when(u'Click icono "tachito" preguntas frecuentes')
def step_impl(context):
    ABM_pregunta_frecuente.click_tachito_preguntasFreuentes(context)


@then(u'Click boton eliminar preguntas frecuentes')
def step_impl(context):
    ABM_pregunta_frecuente.click_eliminar_preguntaFrecuente(context)


@then(u'Click boton guardar preguntas frecuentes')
def step_impl(context):
    ABM_pregunta_frecuente.click_guardar_preguntaFrecuente(context)