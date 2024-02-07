Feature: Buscar la capacitacion creada anteriormente e inscribirse
  Background:
    Given Ingreso a ofertas de educacion

  Scenario Outline: 25 Verificar la busqueda de la capacitacion y el poder inscribirse
    When Validar logo pagina front
    When Click accede a tu cuenta
    When Click ingreso por miBA
    When Ingresa el "<email>"
    When Ingresa la "<clave>"
    Then Click boton ingresar y validar el inicio de sesion
    #HASTA ACA EL INICIO DE SECION (FRONT)
    When Click buscar en educacion
    When Seleccionar categoria
    Then Click buscar y validar
    When Click en la capacitacion
    Then Click inscribirme
      Examples:

        | email                 | clave    |
        | noecoppo@yahoo.com.ar | Troquel1 |