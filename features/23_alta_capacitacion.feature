Feature: Alta capacitacion
  Background:
    Given Ingreso al portal de oportunidades

  Scenario Outline: 23 Verificar la creacion (en borrador) de la capacitacion
    When Validar logo pagina
    When Completar credenciales de inicio de sesion
    Then Click boton ingresar
    #HASTA ACA INICIO DE SESION EN EL BACK
    When Click educacion
    When Click capacitaciones
    When Click boton crear
    When Completar todos los campos
    Then Click guardar como borrador y validar
    When Click icono "editar"
    When Click boton cargar
    When Cargar datos de edicion
    Then Click boton crear y validar
    When Cambiar estado
    Then Click boton guardar
      Examples:

        | user        | clave    |
        | 27165286796 | Troquel1 |