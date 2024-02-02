Feature: ABM categoriaWeb
  Background:
    Given Ingreso al portal de oportunidades

  Scenario Outline: 06 Validar la creacion de una categoriaWeb y que permita editar y eliminar
    When Validar logo pagina
    When Completar credenciales de inicio de sesion
    Then Click boton ingresar
    #HASTA ACA INICIO DE SESION EN EL BACK
    When Click configuracion
    When Click categoriasWeb
    When Click boton crear
    When Completar nombre categoriaWeb
    #When Subir archivo (imagen)
    Then Click boton guardar
    When Click icono "editar"
    When Modificar nombre categoriaWeb
    Then Click boton guardar
    When Click icono "tachito"
    Then Click boton eliminar
      Examples:

        | user        | clave    |
        | 27165286796 | Troquel1 |