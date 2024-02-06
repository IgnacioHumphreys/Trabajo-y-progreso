Feature: Buscar Institucion
  Background:
    Given Ingreso al portal de oportunidades

  Scenario Outline: 22 Verificar la busqueda de una institucion
    When Validar logo pagina
    When Completar credenciales de inicio de sesion
    Then Click boton ingresar
    #HASTA ACA INICIO DE SESION EN EL BACK
    When Click educacion
    When Click institucines
    When Escribir codigo institucion
    When Escribir nombre institucion
    When Seleccionar programa en institucion
    Then Click boton buscar institucion y validar
      Examples:

        | user        | clave    |
        | 27165286796 | Troquel1 |