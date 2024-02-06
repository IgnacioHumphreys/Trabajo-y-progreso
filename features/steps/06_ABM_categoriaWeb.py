from behave import *
from pages.back_end_pages.ABM_categoriaWeb_06_page import ABM_categoriaWeb

@when(u'Click categoriasWeb')
def step_impl(context):
    ABM_categoriaWeb.click_categoriasWeb(context)


@when(u'Completar nombre categoriaWeb')
def step_impl(context):
    ABM_categoriaWeb.input_categoriaWeb(context)


@when(u'Subir archivo (imagen)')
def step_impl(context):
    ABM_categoriaWeb.subir_imagen(context)


@when(u'Modificar nombre categoriaWeb')
def step_impl(context):
    ABM_categoriaWeb.mod_nom_categoriaWeb(context)