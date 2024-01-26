from behave import *
from pages.ABM_programa_10_page import ABM_programa

@when(u'Click programas')
def step_impl(context):
    ABM_programa.click_programas(context)


@when(u'Completar codigo programa')
def step_impl(context):
    ABM_programa.com_cod_programa(context)


@when(u'Completar nombre programa')
def step_impl(context):
    ABM_programa.com_nom_programa(context)


@when(u'Seleccionar ministerio')
def step_impl(context):
    ABM_programa.select_ministerio(context)


@when(u'Seleccionar reparticion')
def step_impl(context):
    ABM_programa.select_reparticion(context)


@when(u'Completar duracion estimada')
def step_impl(context):
    ABM_programa.com_duracion_estimada(context)


@when(u'Completar fecha de inscripcion estimada')
def step_impl(context):
    ABM_programa.com_fecha_inscripcion(context)


@then(u'Click boton guardar programa')
def step_impl(context):
    ABM_programa.click_guardar_programa(context)


@when(u'Modificar codigo programa')
def step_impl(context):
    ABM_programa.mod_cod_programa(context)


@when(u'Modificar nombre programa')
def step_impl(context):
    ABM_programa.mod_nom_programa(context)


@when(u'Modificar fecha de inscripcion')
def step_impl(context):
    ABM_programa.mod_fecha_inscripcion(context)