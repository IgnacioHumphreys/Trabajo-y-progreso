from behave import *
from pages.ABM_grupos_15_page import ABM_grupos

@when(u'Click grupos')
def step_impl(context):
    ABM_grupos.click_grupos(context)


@when(u'Completar nombre grupo')
def step_impl(context):
    ABM_grupos.com_nom_grupo(context)


@when(u'Switch "mostrar en el home"')
def step_impl(context):
    ABM_grupos.activar_switch(context)


@when(u'Seleccionar capacitaciones')
def step_impl(context):
    ABM_grupos.select_capacitaciones(context)


@then(u'Click boton publicar')
def step_impl(context):
    ABM_grupos.click_publicar(context)


#@when(u'Click icono "editar" grupo')
#def step_impl(context):



#@when(u'Modificar nombre grupo')
#def step_impl(context):



#@when(u'Switch inactivo')
#def step_impl(context):
