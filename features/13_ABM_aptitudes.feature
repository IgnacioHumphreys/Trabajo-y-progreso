Feature: ABM aptitudes
  Background:
    Given Ingreso al portal de oportunidades

  Scenario Outline: 13 Validar la creacion de una aptitud y que permita editar y eliminar
    When Validar logo pagina
    When Completar credenciales de inicio de sesion
    Then Click boton ingresar
    #HASTA ACA INICIO DE SESION
    When Click configuracion
    When Click aptitudes
    When Click boton crear
    When Completar nombre aptitud
    Then Click boton guardar aptitud
    When Click icono "editar"
    When Modificar nombre aptitud
    Then Click boton guardar aptitud
    When Click icono "tachito"
    Then Click boton eliminar
      Examples:

        | user | clave |
        | test | Gobi  |