from behave import*
from pages.deshabilitar_inscripcion_capacitacion_26_page import deshabilitar_capacitacion

@when(u'Deshabilitar capacitacion')
def step_impl(context):
    deshabilitar_capacitacion.click_deshabilitar(context)