from behave import *
from pages.back_end_pages.ABM_tipoFormacionWeb_17_page import ABM_tipoFormacionWeb


@when(u'Click educacion')
def step_impl(context):
    ABM_tipoFormacionWeb.click_educacion(context)


@when(u'Click tipos de formacion web')
def step_impl(context):
    ABM_tipoFormacionWeb.click_tiposFormacionWeb(context)


@when(u'Completar nombre tipo de formacion web')
def step_impl(context):
    ABM_tipoFormacionWeb.com_nom_formacionWeb(context)


@when(u'Seleccionar color etiqueta')
def step_impl(context):
    ABM_tipoFormacionWeb.select_color(context)


@when(u'Modificar nombre tipo de formacion web')
def step_impl(context):
    ABM_tipoFormacionWeb.mod_nom_formacionWeb(context)


@when(u'Modificar color etiqueta')
def step_impl(context):
    ABM_tipoFormacionWeb.mod_color_etiqueta(context)