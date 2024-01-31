Feature: ABM programa
  Background:
    Given Ingreso al portal de oportunidades

  Scenario Outline: 10 Validar la creacion de una reparticion y que permita editar y eliminar
    When Validar logo pagina
    When Completar credenciales de inicio de sesion
    Then Click boton ingresar
    #HASTA ACA INICIO DE SESION
    When Click configuracion
    When Click programas
    When Click boton crear
    When Completar codigo programa
    When Completar nombre programa
    When Seleccionar ministerio
    When Seleccionar reparticion
    When Completar duracion estimada
    When Completar fecha de inscripcion estimada
    Then Click boton guardar
    When Click icono "editar"
    When Modificar codigo programa
    When Modificar nombre programa
    When Modificar fecha de inscripcion
    Then Click boton guardar
    When Click icono "tachito"
    Then Click boton eliminar
      Examples:

        | user        | clave    |
        | 27165286796 | Troquel1 |