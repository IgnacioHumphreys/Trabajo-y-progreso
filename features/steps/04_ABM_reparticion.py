from behave import *
from pages.ABM_reparticion_04_page import ABM_reparticion

@when(u'Click reparticiones')
def step_impl(context):
    ABM_reparticion.click_reparticiones(context)


@when(u'Completar nombre reparticion')
def step_impl(context):
    ABM_reparticion.com_nom_reparticion(context)


@when(u'Asociar ministerio')
def step_impl(context):
    ABM_reparticion.asociar_ministerio(context)


@then(u'Click boton guardar reparticion')
def step_impl(context):
    ABM_reparticion.click_guardar_reparticion(context)


@when(u'Modificar nombre reparticion')
def step_impl(context):
    ABM_reparticion.mod_nom_reparticion(context)

@then(u'Click boton guardar reparticion editada')
def step_impl(context):
    ABM_reparticion.click_guardar_reparticion_editada(context)