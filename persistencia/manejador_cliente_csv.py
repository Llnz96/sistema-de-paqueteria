from csv import writer, reader

def guardar_clientes(cliente: dict) -> None:
    with open("clientes.csv", "a", newline="", encoding="utf-8") as archivo:
        escritor = writer(archivo)
        escritor.writerow([
            cliente["id"],
            cliente["nombre"],
            cliente["apellido"],
            cliente["celular"]
        ])

def obtener_clientes() -> list[dict]:
    clientes = []
    try:
        with open("clientes.csv", "r", encoding="utf-8") as archivo:
            lector = reader(archivo)
            for fila in lector:
                clientes.append({
                    "id": fila[0],
                    "nombre": fila[1],
                    "apellido": fila[2],
                    "celular": fila[3]
                })
    except:
        return []

    return clientes