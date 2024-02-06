from behave import *
from pages.back_end_pages.ABM_ministerio_02_page import ABM_ministerio

@when(u'Click configuracion')
def step_impl(context):
    ABM_ministerio.click_config(context)


@when(u'Click ministerios')
def step_impl(context):
    ABM_ministerio.click_ministerios(context)


@when(u'Click boton crear')
def step_impl(context):
    ABM_ministerio.click_btn_crear(context)


@when(u'Completar nombre ministerio')
def step_impl(context):
    ABM_ministerio.comp_nom_ministerio(context)


@then(u'Click boton guardar')
def step_impl(context):
    ABM_ministerio.click_guardar(context)


@when(u'Click icono "editar"')
def step_impl(context):
    ABM_ministerio.click_editar(context)


@when(u'Modificar nombre ministerio')
def step_impl(context):
    ABM_ministerio.mod_nom_ministerio(context)


@when(u'Click icono "tachito"')
def step_impl(context):
    ABM_ministerio.click_tachito(context)


@then(u'Click boton eliminar')
def step_impl(context):
    ABM_ministerio.click_eliminar(context)