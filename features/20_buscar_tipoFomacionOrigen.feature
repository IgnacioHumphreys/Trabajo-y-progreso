Feature: Buscar tipo Formacion Origen
  Background:
    Given Ingreso al portal de oportunidades

  Scenario Outline: 20 Verificar la busqueda de un tipo de Formacion Origen
    When Validar logo pagina
    When Completar credenciales de inicio de sesion
    Then Click boton ingresar
    #HASTA ACA INICIO DE SESION
    When Click educacion
    When Click tipos de formacion origen
    When Escribir formacion origen
    Then Click boton buscar formacion origen
      Examples:

        | user        | clave    |
        | 27165286796 | Troquel1 |