import csv


def guardar_bien(bien):

    with open("bienes.csv", "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([
            bien["id"],
            bien["descripcion"],
            bien["modelo"],
            bien["valor"],
            bien["estatus"]

])
