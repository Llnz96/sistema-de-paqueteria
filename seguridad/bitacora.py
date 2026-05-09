from socket import gethostbyname, gethostname
from datetime import datetime

def registrarEvento(mensaje: str) -> None:
    ip = gethostbyname(gethostname())
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("bienes.log", "a", encoding="utf-8") as archivo:
        archivo.write(f"[{fecha}] {ip} {mensaje}\n")