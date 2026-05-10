from . import manejador_bien_csv
from . import manejador_bien_json
from . import manejador_cliente_csv
from . import manejador_cliente_json
from . import manejador_direccion_csv
from . import manejador_direccion_json

def guardar_bien(bien: dict, formato: str) -> None:
    if formato == "CSV":
        manejador_bien_csv.guardar_bienes(bien)
    elif formato == "JSON":
        manejador_bien_json.guardar_bienes(bien)

def guardar_cliente(cliente: dict, formato: str) -> None:
    if formato == "CSV":
        manejador_cliente_csv.guardar_clientes(cliente)
    elif formato == "JSON":
        manejador_cliente_json.guardar_clientes(cliente)

def guardar_direccion(direccion: dict, formato: str) -> None:
    if formato == "CSV":
        manejador_direccion_csv.guardar_direcciones(direccion)
    elif formato == "JSON":
        manejador_direccion_json.guardar_direcciones(direccion)


def generar_dict_bienes(formato: str) -> dict:
    if formato == "CSV":
        return manejador_bien_csv.obtener_bienes()
    elif formato == "JSON":
        return manejador_bien_json.obtener_bienes()
    
def generar_dict_clientes(formato: str) -> dict:
    if formato == "CSV":
        return manejador_cliente_csv.obtener_clientes()
    elif formato == "JSON":
        return manejador_cliente_json.obtener_clientes()
    
def generar_dict_direcciones(formato: str) -> dict:
    if formato == "CSV":
        return manejador_direccion_csv.obtener_direcciones()
    elif formato == "JSON":
        return manejador_direccion_json.obtener_direcciones()