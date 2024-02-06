Feature: Buscar aptitudes
  Background:
    Given Ingreso al portal de oportunidades

  Scenario Outline: 14 Verificar la busqueda de una aptitud
    When Validar logo pagina
    When Completar credenciales de inicio de sesion
    Then Click boton ingresar
    #HASTA ACA INICIO DE SESION EN EL BACK
    When Click configuracion
    When Click aptitudes
    When Escribir aptitud
    Then Click boton buscar aptitud y validar
      Examples:

        | user        | clave    |
        | 27165286796 | Troquel1 |