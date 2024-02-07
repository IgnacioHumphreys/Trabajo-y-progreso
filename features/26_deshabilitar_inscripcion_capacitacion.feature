Feature: Deshabilitar la inscripcion en la capacitacion y validar
  Background:
    Given Ingreso al portal de oportunidades

  Scenario Outline: 26 Se deshabilita la inscripcion a la capacitacion y se valida desde el lado del usuario
    When Validar logo pagina
    When Completar credenciales de inicio de sesion
    Then Click boton ingresar
    #HASTA ACA INICIO DE SESION EN EL BACK
    When Click educacion
    When Click capacitaciones
    When Click icono "editar"
    When Deshabilitar capacitacion
    Then Click boton guardar
      Examples:

        | user        | pass     | email | clave |
        | 27165286796 | Troquel1 |       |       |