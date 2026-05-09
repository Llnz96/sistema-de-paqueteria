from csv import writer, reader

def guardar_bienes(bien: dict) -> None:
    with open("bienes.csv", "a", newline="", encoding="utf-8") as archivo:
        escritor = writer(archivo)
        escritor.writerow([
            bien["id"],
            bien["descripcion"],
            bien["modelo"],
            bien["valor"],
            bien["estatus"]
        ])

def obtener_bienes() -> list[dict]:
    bienes = []
    try:
        with open("bienes.csv", "r", encoding="utf-8") as archivo:
            lector = reader(archivo)
            for fila in lector:
                bienes.append({
                    "id": fila[0],
                    "descripcion": fila[1],
                    "modelo": fila[2],
                    "valor": fila[3],
                    "estatus": fila[4]
                })
    except:
        return []

    return bienes