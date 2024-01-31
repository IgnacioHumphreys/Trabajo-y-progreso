Feature: ABM tipo de Instituciones
  Background:
    Given Ingreso al portal de oportunidades

  Scenario Outline: 21 Validar la creacion de una institucion y que permita editar y eliminar
    When Validar logo pagina
    When Completar credenciales de inicio de sesion
    Then Click boton ingresar
    #HASTA ACA INICIO DE SESION
    When Click educacion
    When Click institucines
    When Click boton crear
    When Completar codigo de institucion
    When Completar nombre de institucion
    When Seleccionar programa en institucion
    Then Click boton guardar
    When Click icono "editar"
    When Modificar codigo de institucion
    Then Click boton guardar
    When Click icono "tachito"
    Then Click boton eliminar
      Examples:

        | user        | clave    |
        | 27165286796 | Troquel1 |