Feature: ABM tipo de Formacion Origen
  Background:
    Given Ingreso al portal de oportunidades

  Scenario Outline: 19 Validar la creacion de un tipo de Formacion Origen y que permita editar y eliminar
    When Validar logo pagina
    When Completar credenciales de inicio de sesion
    Then Click boton ingresar
    #HASTA ACA INICIO DE SESION EN EL BACK
    When Click educacion
    When Click tipos de formacion origen
    When Click boton crear
    When Completar nombre tipo de formacion origen
    When Seleccionar tipo formacion web
    Then Click boton guardar
    When Click icono "editar"
    When Modificar nombre tipo de formacion origen
    Then Click boton guardar
    When Click icono "tachito"
    Then Click boton eliminar
      Examples:

        | user        | clave    |
        | 27165286796 | Troquel1 |