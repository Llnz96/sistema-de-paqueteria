def crea_bien(id: str, descripcion: str, modelo: str, valor: float, estatus: str) -> dict:
    dict_bien={
        "id": id,
        "descripcion": descripcion,
        "modelo": modelo,
        "valor": valor,
        "estatus": estatus
    }
    return dict_bien