Feature: Buscar aptitudes
  Background:
    Given Ingreso al portal de oportunidades

  Scenario Outline: 14 Verificar la busqueda de una aptitud
    When Validar logo pagina
    When Completar credenciales de inicio de sesion
    Then Click boton ingresar
    #HASTA ACA INICIO DE SESION
    When Click configuracion
    When Click aptitudes
    When Escribir aptitud
    Then Click boton buscar
      Examples:

        | user | clave |
        | test | Gobi  |