Feature: Buscar grupos
  Background:
    Given Ingreso al portal de oportunidades

  Scenario Outline: 16 Verificar la busqueda de un grupo
    When Validar logo pagina
    When Completar credenciales de inicio de sesion
    Then Click boton ingresar
    #HASTA ACA INICIO DE SESION
    When Click educacion
    When Click tipos de formacion web
    When Escribir formacion web
    Then Click boton buscar formacion web
      Examples:

        | user | clave |
        | test | Gobi  |