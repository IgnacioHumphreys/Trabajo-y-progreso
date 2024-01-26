Feature: ABM reparticion
  Background:
    Given Ingreso al portal de oportunidades

  Scenario Outline: 04 Validar la creacion de una reparticion y que permita editar y eliminar
    When Validar logo pagina
    When Completar credenciales de inicio de sesion
    Then Click boton ingresar
    #HASTA ACA INICIO DE SESION
    When Click configuracion
    When Click reparticiones
    When Click boton crear
    When Completar nombre reparticion
    When Asociar ministerio
    Then Click boton guardar reparticion
    When Click icono "editar"
    When Modificar nombre reparticion
    Then Click boton guardar reparticion editada
    When Click icono "tachito"
    Then Click boton eliminar
      Examples:

        | user | clave |
        | test | Gobi  |