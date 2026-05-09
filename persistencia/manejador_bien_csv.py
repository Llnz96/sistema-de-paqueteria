from csv import writer

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