def crea_cliente(id: str, nombre: str, apellido: str, celular: str) -> dict:
    dict_cliente = {
        "id": id,
        "nombre": nombre,
        "apellido": apellido,
        "celular": celular
    }

    return dict_cliente