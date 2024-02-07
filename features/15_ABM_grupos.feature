Feature: ABM grupos
  Background:
    Given Ingreso al portal de oportunidades

  Scenario Outline: 15 Validar la creacion de un grupo (si esta activo o no) y que permita editar y eliminar
    When Validar logo pagina
    When Completar credenciales de inicio de sesion
    Then Click boton ingresar
    #HASTA ACA INICIO DE SESION EN EL BACK
    When Click configuracion
    When Click grupos
    When Click boton crear
    When Completar nombre grupo
    When Cambiar switch activo/inactivo
    When Seleccionar capacitaciones
    Then Click boton publicar
    When Click icono "editar" grupos
    When Modificar nombre grupo
    When Cambiar switch activo/inactivo
    Then Click boton guardar
    When Click icono "tachito" grupo
    Then Click boton eliminar
      Examples:

        | user        | clave    |
        | 27165286796 | Troquel1 |