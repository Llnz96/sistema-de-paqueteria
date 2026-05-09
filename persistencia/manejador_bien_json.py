from json import dump, load, JSONDecodeError

def guardar_bienes(bien: dict) -> None:
    bienes = obtener_bienes()
    bienes.append(bien)

    with open("bienes.json", "w", encoding="utf-8") as archivo:
        dump(bienes, archivo, ensure_ascii=False, indent=4)

def obtener_bienes() -> list[dict]:
    try:
        with open("bienes.json", "r", encoding="utf-8") as archivo:
            data = load(archivo)
        
        if isinstance(data, list):
            return data
        
        return[data]
    except (FileNotFoundError, JSONDecodeError):
        return []