from behave import *
from pages.back_end_pages.ABM_categoriaOrigen_08_page import ABM_categoriaOrigen

@when(u'Click categoriasOrigen')
def step_impl(context):
    ABM_categoriaOrigen.click_categoriasOrigen(context)


@when(u'Completar nombre categoriaOrigen')
def step_impl(context):
    ABM_categoriaOrigen.com_nom_categoriaOrigen(context)


@when(u'Seleccionar tipo')
def step_impl(context):
    ABM_categoriaOrigen.seleccionar_tipo(context)


@when(u'Asociar categoriaWeb')
def step_impl(context):
    ABM_categoriaOrigen.asociar_categoriaWeb(context)


@when(u'Modificar nombre cateogriaOrigen')
def step_impl(context):
    ABM_categoriaOrigen.mod_nom_categoriaOrigen(context)


@when(u'Modificar tipo')
def step_impl(context):
    ABM_categoriaOrigen.mod_tipo(context)