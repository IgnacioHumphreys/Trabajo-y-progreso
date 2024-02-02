Feature: Buscar reparticion
  Background:
    Given Ingreso al portal de oportunidades

  Scenario Outline: 05 Verificar la busqueda de una reparticion
    When Validar logo pagina
    When Completar credenciales de inicio de sesion
    Then Click boton ingresar
    #HASTA ACA INICIO DE SESION EN EL BACK
    When Click configuracion
    When Click reparticiones
    When Escribir reparticion
    Then Click boton buscar reparticion y validar
      Examples:

        | user        | clave    |
        | 27165286796 | Troquel1 |