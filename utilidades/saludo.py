from datetime import datetime

def obtener_saludo() -> str:
    hoy = datetime.now().hour

    if hoy < 6:
        return "¡Buena... ¿madrugada?, Empleado!"
    elif hoy < 12:
        return "¡Buen día, Empleado!"
    elif hoy < 19:
        return "¡Buena tarde, Empleado!"
    elif hoy < 24:
        return "¡Buena noche, Empleado!"
    
    return "¡Bienvenido!"