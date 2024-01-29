from behave import *
from pages.ABM_tipoFormacionOrigen_19_page import ABM_tipoFormacionOrigen

@when(u'Click tipos de formacion origen')
def step_impl(context):
    ABM_tipoFormacionOrigen.click_tiposFormacionOrigen(context)


@when(u'Completar nombre tipo de formacion origen')
def step_impl(context):
    ABM_tipoFormacionOrigen.com_nom_formacionOrigen(context)


@when(u'Seleccionar tipo formacion web')
def step_impl(context):
    ABM_tipoFormacionOrigen.select_formacionWeb(context)


@then(u'Click boton guardar formacion origen')
def step_impl(context):
    ABM_tipoFormacionOrigen.click_guardar_formacionOrigen(context)


@when(u'Modificar nombre tipo de formacion web')
def step_impl(context):
    ABM_tipoFormacionOrigen.mod_nom_formacionOrigen(context)