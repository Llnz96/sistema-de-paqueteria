def crea_bien(
    id,
    descripcion,
    modelo,
    valor,
    estatus
):
    dict_bien={
        "id": id,
        "descripcion": descripcion,
        "modelo": modelo,
        "valor": valor,
        "estatus": estatus
    }
    return dict_bien

