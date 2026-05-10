from csv import writer, reader

def guardar_direcciones(direccion: dict) -> None:
    with open("direcciones.csv", "a", newline="", encoding="utf-8") as archivo:
        escritor = writer(archivo)
        escritor.writerow([
            direccion["id"],
            direccion["colonia"],
            direccion["calle"],
            direccion["localidad"],
            direccion["estado"],
            direccion["postal"]
        ])

def obtener_direcciones() -> list[dict]:
    direcciones = []
    try:
        with open("direcciones.csv", "r", encoding="utf-8") as archivo:
            lector = reader(archivo)
            for fila in lector:
                direcciones.append({
                    "id": fila[0],
                    "colonia": fila[1],
                    "calle": fila[2],
                    "localidad": fila[3],
                    "estado": fila[4],
                    "postal": fila[5]
                })
    except:
        return []

    return direcciones