############################ TEST 1 LOGIN ############################
URL = "https://trabajo-y-progreso-backend-qa.gcba.gob.ar/"
logoBA = "//div[@class='navbar-brand']//img[1]"
input_usuario = "(//div[@class='mb-3']//input)[1]"
input_password = "(//div[@class='mb-3']//input)[2]"
btn_ingresar = "//div[contains(@class,'d-flex justify-content-between')]//button[1]"
############################ TEST 2 ABM MINISTERIO ############################
btn_configuracion = "(//div[@class='d-flex']//span)[1]"
btn_ministerios = "//a[contains(text(),'Ministerios')]"
btn_crear = "//button[@class='btn btn-primary']"
input_nom_ministerio = "//div[contains(@class,'col-md-6 col-xl-4')]//input[1]"
btn_guardar = "//form[@name='MinisterioType']//button[1]"
btn_editar = "(//div[@class='actions']//button)[1]"
btn_tachito = "(//div[@class='actions']//button)[2]"
btn_eliminar = "(//div[@class='modal-footer']//button)[2]"
############################ TEST 3 BUSCAR MINISTERIO ############################
btn_buscar = "(//div[@class='col-auto mb-3']//button)[1]"
############################ TEST 4 ABM REPARTICION ############################
btn_reparticiones = "(//div[@id='configuracionCollapse']//a)[2]"
input_reparticion = "(//div[contains(@class,'col-md-6 col-xl-4')]//input)[1]"
box_ministerio = "//div[@class='filter-option-inner']//div[1]"
select_automatizacion = "//a[@id='bs-select-1-5']/span[1]"
btn_guardar_reparticion = "(//form[@name='ReparticionType']//button)[2]"
############################ TEST 5 BUSCAR REPARTICION ############################
############################ TEST 6 ABM CATEGORIA WEB ############################
btn_categoriasWeb = "(//div[@id='configuracionCollapse']//a)[3]"
input_categoriaWeb = "//div[contains(@class,'col-md-6 col-xl-4')]//input[1]"
up_imagen = "//div[contains(@class,'dashedUploaderImg mb-2')]//input[1]"
btn_guardar_categoriaWeb = "//form[@name='CategoriaFrontType']//button[1]"
############################ TEST 7 BUSCAR CATEGORIA WEB ############################
############################ TEST 8 ABM CATEGORIA ORIGEN ############################
btn_categoriasOrigen = "//a[@id='categoriasWeb']/following-sibling::a[1]"
input_categoriaOrigen = "//div[@class='col-md-6 mb-3']//input[1]"
btn_guardar_categoriaOrigen = "(//form[@name='categoria_back']//button)[3]"
box_tipo = "(//div[@class='filter-option-inner']//div)[1]"
select_empleo = "//a[@id='bs-select-1-4']/span[1]"
box_categoriaWeb = "(//div[@class='filter-option-inner']//div)[2]"
select_categoriaWebAuto = "(//a[@id='bs-select-2-29']//span)[2]"
select_habilidad = "//a[@id='bs-select-1-2']//span[1]"
############################ TEST 9 BUSCAR CATEGORIA ORIGEN ############################
input_categoriaWeb_en_origen = "(//div[contains(@class,'col-md col-xl-4')]//input)[2]"
############################ TEST 10 ABM PROGRAMA ############################
btn_programas = "//a[@id='categorias']/following-sibling::a[1]"
btn_guardar_programa = "//div[@class='row mb-4']/following-sibling::button[1]"
input_cod_programa = "(//div[contains(@class,'col-md-6 col-xl')]//input)[1]"
input_nom_programa = "(//div[contains(@class,'col-md-6 col-xl')]//input)[2]"
box2_ministerio = "(//div[@class='filter-option-inner']//div)[1]"
box_reparticion = "(//div[@class='filter-option-inner']//div)[2]"
select_reparticion_auto = "//a[@id='bs-select-2-1']/span[1]"
input_duracion_estimada = "(//div[contains(@class,'col-lg-6 col-xl-3')]//input)[3]"
input_fecha_inscripcion = "//label[text()='Fechas de Inscripción Estimadas']/following-sibling::input"
############################ TEST 11 BUSCAR PROGRAMA ############################
input_cod_programa_buscar = "(//div[contains(@class,'col-md-4 col-xl')]//input)[1]"
input_nom_programa_buscar = "(//div[contains(@class,'col-md-4 col-xl')]//input)[2]"
box3_ministerio = "(//div[@class='filter-option-inner']//div)[1]"
select_automatizaion_en_programa = "//a[@id='bs-select-1-1']//span[1]"
############################ TEST 12 ABM PREGUNTA FRECUENTE ############################
btn_preguntasFrecuentes = "//a[@id='programas']/following-sibling::a[1]"
box4_ministerio = "(//div[@class='filter-option-inner']//div)[1]"
box_programa = "(//div[@class='filter-option-inner']//div)[3]"
select_programa = "//a[@id='bs-select-3-1']/span[1]"
box_capacitacion = "//div[text()='Seleccionar...']"
select_python = "//a[@id='bs-select-4-1']/span[1]"
input_pregunta = "//div[@class='col-12 mb-3']//input[1]"
input_respuesta = "//div[@class='col-12 mb-3']//textarea[1]"
btn_editar_preguntasFrecuentes = "(//div[@class='d-flex align-items-center']//button)[1]"
btn_guardar_preguntaFrecuente = "//div[@class='row mb-4']/following-sibling::button[1]"
btn_tachito_preguntaFrecuente = "(//div[@class='d-flex align-items-center']//button)[2]"
btn_eliminar_preguntaFrecuente = "(//div[@class='modal-footer']//button)[2]"
############################ TEST 13 ABM APTITUDES ############################
btn_aptitudes = "//a[@id='preguntasFrecuentes']/following-sibling::a[1]"
input_aptitud = "//div[contains(@class,'col-md-6 col-xl-4')]//input[1]"
btn_guardar_aptitud = "//form[@name='AptitudType']//button[1]"
############################ TEST 14 BUSCAR APTITUD ############################
############################ TEST 15 ABM GRUPOS ############################
btn_grupos = "//a[@id='aptitudes']/following-sibling::a[1]"
input_grupo = "//div[contains(@class,'col-md-6 col-xl-4')]//input[1]"
btn_switch = "(//div[@class='custom-control custom-switch']//label)[1]"
select_capacitacion1 = "customCheck2"
select_capacitacion2 = "customCheck4"
btn_publicar = "//div[@class='card mb-5']/following-sibling::button[1]"
############################ TEST 16 BUSCAR GRUPOS ############################
############################ TEST 17 ABM TIPO FORMACION WEB ############################
btn_educacion = "//div[@class='d-flex show']//span[1]"
btn_tiposFormacionWeb = "(//div[@id='educacionCollapse']//a)[2]"
input_formacionWeb = "//div[contains(@class,'col-12 col-md-6')]//input[1]"
box_colorEtiqueta = "//div[@class='filter-option-inner']//div[1]"
select_verde = "//a[@id='bs-select-1-2']//span[1]"
select_rojo = "//a[@id='bs-select-1-4']/span[1]"
btn_guardar_formacionWeb = "(//form[@name='tipo_formacion_web']//button)[2]"
############################ TEST 18 BUSCAR TIPO FORMACION WEB ############################
############################ TEST 19 ABM TIPO FORMACION ORIGEN ############################
btn_tiposFormacionOrigen = "//div[@id='educacionCollapse']//a[1]"
input_formacionOrigen = "(//div[contains(@class,'col-md-6 col-xl-4')]//input)[1]"
box_formacionWeb = "//div[@class='filter-option-inner']//div[1]"
select_automatizacion_formacionWeb = "//a[@id='bs-select-1-15']/span[1]"
btn_guardar_formacionOrigen = "(//form[@name='tipo_formacion_origen']//button)[2]"