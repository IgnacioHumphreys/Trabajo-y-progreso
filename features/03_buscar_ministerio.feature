Feature: Buscar ministerio
  Background:
    Given Ingreso al portal de oportunidades

  Scenario Outline: 03 Verificar la busqueda de un ministerio
    When Validar logo pagina
    When Completar credenciales de inicio de sesion
    Then Click boton ingresar
    #HASTA ACA INICIO DE SESION EN EL BACK
    When Click configuracion
    When Click ministerios
    When Escribir ministerio
    Then Click boton buscar ministerio y validar
      Examples:

        | user        | clave    |
        | 27165286796 | Troquel1 |