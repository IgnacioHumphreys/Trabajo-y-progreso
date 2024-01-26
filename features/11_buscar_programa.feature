Feature: Buscar programa
  Background:
    Given Ingreso al portal de oportunidades

  Scenario Outline: 11 Verificar la busqueda de un programa
    When Validar logo pagina
    When Completar credenciales de inicio de sesion
    Then Click boton ingresar
    #HASTA ACA INICIO DE SESION
    When Click configuracion
    When Click programas
    When Escribir codigo programa
    When Escribir nombre programa
    When Seleccionar ministerio en programa
    When Seleccionar reparticion
    Then Click boton buscar
      Examples:

        | user | clave |
        | test | Gobi  |