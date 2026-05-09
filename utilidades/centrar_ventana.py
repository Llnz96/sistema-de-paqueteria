from tkinter import Tk

def centrar_interfaz(interfaz: Tk, ancho: int, alto: int) -> None:
    x = (interfaz.winfo_screenwidth() // 2) - (ancho // 2)
    y = (interfaz.winfo_screenheight() // 2) - (alto // 2)
    interfaz.geometry(f"{ancho}x{alto}+{x}+{y}")