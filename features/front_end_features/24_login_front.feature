Feature: Iniciar sesion en el Front ofertas de educacion
  Background:
    Given Ingreso a ofertas de educacion

  Scenario Outline: 24 Verificar el ingreso a ofertas de educacion
    Then Validar logo pagina front
      Examples:

        | user        | clave    |
        | 27165286796 | Troquel1 |