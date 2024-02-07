from behave import *
from pages.ABM_grupos_15_page import ABM_grupos

@when(u'Click grupos')
def step_impl(context):
    ABM_grupos.click_grupos(context)


@when(u'Completar nombre grupo')
def step_impl(context):
    ABM_grupos.com_nom_grupo(context)


@when(u'Cambiar switch activo/inactivo')
def step_impl(context):
    ABM_grupos.click_switch(context)


@when(u'Seleccionar capacitaciones')
def step_impl(context):
    ABM_grupos.select_capacitaciones(context)


@then(u'Click boton publicar')
def step_impl(context):
    ABM_grupos.click_publicar(context)


@when(u'Modificar nombre grupo')
def step_impl(context):
    ABM_grupos.mod_nom_grupo(context)


@when(u'Click icono "editar" grupos')
def step_impl(context):
    ABM_grupos.click_editar(context)


@when(u'Click icono "tachito" grupo')
def step_impl(context):
    ABM_grupos.click_tachito(context)