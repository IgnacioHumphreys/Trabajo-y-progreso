Feature: Buscar categoriaOrigen
  Background:
    Given Ingreso al portal de oportunidades

  Scenario Outline: 09 Verificar la busqueda de una categoriaOrigen
    When Validar logo pagina
    When Completar credenciales de inicio de sesion
    Then Click boton ingresar
    #HASTA ACA INICIO DE SESION
    When Click configuracion
    When Click categoriasOrigen
    When Escribir categoriaOrigen
    When Escribir categoriaWeb en CategoriasOrigen
    Then Click boton buscar categoriaOrigen
      Examples:

        | user | clave |
        | test | Gobi  |