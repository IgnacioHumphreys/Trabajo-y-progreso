Feature: Buscar categoriaWeb
  Background:
    Given Ingreso al portal de oportunidades

  Scenario Outline: 07 Verificar la busqueda de una categoriaWeb
    When Validar logo pagina
    When Completar credenciales de inicio de sesion
    Then Click boton ingresar
    #HASTA ACA INICIO DE SESION
    When Click configuracion
    When Click categoriasWeb
    When Escribir categoriaWeb
    Then Click boton buscar
      Examples:

        | user | clave |
        | test | Gobi  |