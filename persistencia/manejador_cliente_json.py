from json import dump, load, JSONDecodeError

def guardar_clientes(cliente: dict) -> None:
    clientes = obtener_clientes()
    clientes.append(cliente)

    with open("clientes.json", "w", encoding="utf-8") as archivo:
        dump(clientes, archivo, ensure_ascii=False, indent=4)

def obtener_clientes() -> list[dict]:
    try:
        with open("clientes.json", "r", encoding="utf-8") as archivo:
            data = load(archivo)
        
        if isinstance(data, list):
            return data
        
        return[data]
    except (FileNotFoundError, JSONDecodeError):
        return []