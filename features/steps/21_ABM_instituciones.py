from behave import *
from pages.ABM_instituciones_21_page import ABM_instituciones

@when(u'Click institucines')
def step_impl(context):
    ABM_instituciones.click_instituciones(context)


@when(u'Completar codigo de institucion')
def step_impl(context):
    ABM_instituciones.com_cod_institucion(context)


@when(u'Completar nombre de institucion')
def step_impl(context):
    ABM_instituciones.com_nom_institucion(context)


@when(u'Seleccionar programa en institucion')
def step_impl(context):
    ABM_instituciones.select_programa_enInstitucion(context)


@when(u'Modificar codigo de institucion')
def step_impl(context):
    ABM_instituciones.mod_codigo_institucion(context)