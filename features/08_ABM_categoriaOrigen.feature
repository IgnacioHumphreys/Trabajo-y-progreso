Feature: ABM categoriasOrigen
  Background:
    Given Ingreso al portal de oportunidades

  Scenario Outline: 08 Validar la creacion de una categoriaOrigen y que permita editar y eliminar
    When Validar logo pagina
    When Completar credenciales de inicio de sesion
    Then Click boton ingresar
    #HASTA ACA INICIO DE SESION
    When Click configuracion
    When Click categoriasOrigen
    When Click boton crear
    When Completar nombre categoriaOrigen
    When Seleccionar tipo
    When Asociar categoriaWeb
    Then Click boton guardar categoriaOrigen
    When Click icono "editar"
    When Modificar nombre cateogriaOrigen
    When Modificar tipo
    Then Click boton guardar categoriaOrigen
    When Click icono "tachito"
    Then Click boton eliminar
      Examples:

        | user | clave |
        | test | Gobi  |