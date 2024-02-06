from behave import *
from pages.back_end_pages.ABM_reparticion_04_page import ABM_reparticion

@when(u'Click reparticiones')
def step_impl(context):
    ABM_reparticion.click_reparticiones(context)


@when(u'Completar nombre reparticion')
def step_impl(context):
    ABM_reparticion.com_nom_reparticion(context)


@when(u'Asociar ministerio')
def step_impl(context):
    ABM_reparticion.asociar_ministerio(context)


@when(u'Modificar nombre reparticion')
def step_impl(context):
    ABM_reparticion.mod_nom_reparticion(context)