Feature: ABM ministerio
  Background:
    Given Ingreso al portal de oportunidades

  Scenario Outline: 02 Verificar la creacion de un ministerio y se pueda editar y borrar
    When Validar logo pagina
    When Completar credenciales de inicio de sesion
    Then Click boton ingresar
    #HASTA ACA INICIO DE SESION EN EL BACK
    When Click configuracion
    When Click ministerios
    When Click boton crear
    When Completar nombre ministerio
    Then Click boton guardar
    When Click icono "editar"
    When Modificar nombre ministerio
    Then Click boton guardar
    When Click icono "tachito"
    Then Click boton eliminar
      Examples:

        | user        | clave    |
        | 27165286796 | Troquel1 |