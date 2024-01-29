Feature: ABM tipo de Formacion Web
  Background:
    Given Ingreso al portal de oportunidades

  Scenario Outline: 17 Validar la creacion de un tipo de Formacion Web y que permita editar y eliminar
    When Validar logo pagina
    When Completar credenciales de inicio de sesion
    Then Click boton ingresar
    #HASTA ACA INICIO DE SESION
    When Click educacion
    When Click tipos de formacion origen
    When Click boton crear
    When Completar nombre tipo de formacion origen
    When Seleccionar tipo formacion web
    Then Click boton guardar formacion origen
    When Click icono "editar"
    When Modificar nombre tipo de formacion web
    Then Click boton guardar formacion origen
    When Click icono "tachito"
    Then Click boton eliminar
      Examples:

        | user | clave |
        | test | Gobi  |