from behave import *
from pages.ABM_aptitudes_13_page import ABM_aptitudes

@when(u'Click aptitudes')
def step_impl(context):
    ABM_aptitudes.click_aptitudes(context)


@when(u'Completar nombre aptitud')
def step_impl(context):
    ABM_aptitudes.com_nom_aptutud(context)


@then(u'Click boton guardar aptitud')
def step_impl(context):
    ABM_aptitudes.click_guardar_aptitud(context)


@when(u'Modificar nombre aptitud')
def step_impl(context):
    ABM_aptitudes.mod_nom_aptitud(context)