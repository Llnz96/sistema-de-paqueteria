def crea_direccion(id: str, colonia: str, calle: str, localidad: str, estado: str, postal: str) -> dict:
    dict_direccion = {
        "id": id,
        "colonia": colonia,
        "calle": calle,
        "localidad": localidad,
        "estado": estado,
        "postal": postal
    }

    return dict_direccion