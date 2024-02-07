############################ TEST 24 LOGIN ############################
URL_front = "https://trabajo-y-progreso-frontend-qa.gcba.gob.ar/"
logoBa_front = "(//img[@alt='Ciudad de Buenos Aires'])[1]"
btn_tuCuenta = "//span[text()='Accedé a tu cuenta']"
btn_ingreso_miBA = "//p[text()='Ingresar con CUIL / email']"
input_email = "(//label[text()='CUIL / Correo electronico *']/following::input)[1]"
email = "noecoppo@yahoo.com.ar"
input_clave = "(//label[text()='Contraseña *']/following::input)[1]"
clave = "Troquel1"
btn_ingresar = "//button[text()='Ingresar']"
############################ TEST 25 BUSCAR CAPACITACION ############################
btn_buscar_en_educacion = "//label[text()=' Buscar en educación ']"
box_categoria = "//label[text()='Categoría']/following-sibling::select"
select_categoria = "//option[text()='CategoríaWeb (automatización)']"
btn_buscar = "//button[text()='Buscar']"
btn_capacitacion = "(//a[@class='card h-100']//div)[2]"
btn_inscribirme = "//button[text()='Inscribirme']"
############################ TEST 26 DESHABILITAR INSCRIPCION CAPACITACION ############################
btn_deshabilitar = "//label[@for='customSwitchEdicion2721']"