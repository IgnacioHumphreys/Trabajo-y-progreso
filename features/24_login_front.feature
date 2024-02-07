Feature: Iniciar sesion en el Front ofertas de educacion
  Background:
    Given Ingreso a ofertas de educacion

  Scenario Outline: 24 Verificar el ingreso a ofertas de educacion con credenciales validas
    When Validar logo pagina front
    When Click accede a tu cuenta
    When Click ingreso por miBA
    When Ingresa el "<email>"
    When Ingresa la "<clave>"
    Then Click boton ingresar y validar el inicio de sesion
      Examples:

        | email                 | clave    |
        | noecoppo@yahoo.com.ar | Troquel1 |