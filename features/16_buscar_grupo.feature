Feature: Buscar grupos
  Background:
    Given Ingreso al portal de oportunidades

  Scenario Outline: 16 Verificar la busqueda de un grupo
    When Validar logo pagina
    When Completar credenciales de inicio de sesion
    Then Click boton ingresar
    #HASTA ACA INICIO DE SESION EN EL BACK
    When Click configuracion
    When Click grupos
    When Escribir grupo
    Then Click boton buscar grupo y validar
      Examples:

        | user        | clave    |
        | 27165286796 | Troquel1 |