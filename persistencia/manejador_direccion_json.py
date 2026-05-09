from json import dump, load, JSONDecodeError

def guardar_direcciones(direccion: dict) -> None:
    direcciones = obtener_direcciones()
    direcciones.append(direccion)

    with open("direcciones.json", "w", encoding="utf-8") as archivo:
        dump(direcciones, archivo, ensure_ascii=False, indent=4)

def obtener_direcciones() -> list[dict]:
    try:
        with open("direcciones.json", "r", encoding="utf-8") as archivo:
            data = load(archivo)
        
        if isinstance(data, list):
            return data
        
        return[data]
    except (FileNotFoundError, JSONDecodeError):
        return []