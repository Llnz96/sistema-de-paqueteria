import json

def guardar_bien(lista_bienes):
    with open("bienes.json", "w", encoding="utf-8") as archivo:
        json.dump(lista_bienes, archivo, ensure_ascii=False, indent=4)