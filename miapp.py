import domain.bien as misbienes
import ui.formulario_bien as formularios
import persistencia.manejador_bien_json as driver

#formularios.captura_bien()
b = misbienes.crea_bien(1,2,3,4,5)
print(b)
driver.guardar_bien(b)