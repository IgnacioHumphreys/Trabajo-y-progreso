Feature: Iniciar sesion en Back de portal de oportunidades
  Background:
    Given Ingreso al portal de oportunidades

  Scenario Outline: 01 Verificar el inicio de secion con credenciales validas
    When Validar logo pagina
    When Completar credenciales de inicio de sesion
    Then Click boton ingresar
      Examples:

        | user | clave |
        | test | Gobi  |