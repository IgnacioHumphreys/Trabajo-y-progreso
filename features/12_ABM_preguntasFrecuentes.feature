Feature: ABM preguntasFrecuentes
  Background:
    Given Ingreso al portal de oportunidades

  Scenario Outline: 12 Validar la creacion de una preguntaFrecuente y que permita editar y eliminar
    When Validar logo pagina
    When Completar credenciales de inicio de sesion
    Then Click boton ingresar
    #HASTA ACA INICIO DE SESION
    When Click configuracion
    When Click preguntasFrecuentes
    When Click boton crear
    When Seleccionar ministerio en pregunta frecuente
    When Seleccionar reparticion
    When Seleccionar programa
    When Seleccionar capacitacion
    When Completar pregunta
    When Completar respuesta
    Then Click boton guardar preguntas frecuentes
    When Click icono "editar" preguntas frecuentes
    When Modificar pregunta
    When Modificar respuesta
    Then Click boton guardar preguntas frecuentes
    When Click icono "tachito" preguntas frecuentes
    Then Click boton eliminar preguntas frecuentes
      Examples:

        | user | clave |
        | test | Gobi  |