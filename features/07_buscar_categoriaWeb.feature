Feature: Buscar categoriaWeb
  Background:
    Given Ingreso al portal de oportunidades

  Scenario Outline: 07 Verificar la busqueda de una categoriaWeb
    When Validar logo pagina
    When Completar credenciales de inicio de sesion
    Then Click boton ingresar
    #HASTA ACA INICIO DE SESION EN EL BACK
    When Click configuracion
    When Click categoriasWeb
    When Escribir categoriaWeb
    Then Click boton buscar categoriaWeb y validar
      Examples:

        | user        | clave    |
        | 27165286796 | Troquel1 |