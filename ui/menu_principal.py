from tkinter import Tk, Label, Button
from utilidades.centrar_ventana import centrar_interfaz
from utilidades.saludo import obtener_saludo
from .formulario_bien import formulario_captura_bien
from .interfaz_reporte import visualizar_reporte

def menu() -> None:
    ventana = Tk()
    ventana.title("Sistema de registro de bienes")
    centrar_interfaz(ventana, 350, 280)

    saludo = obtener_saludo()

    etq_saludo = Label(ventana, text=saludo, font=("Helvatica", 18, "bold"))
    etq_saludo.pack(pady=10)

    etq_mensaje = Label(ventana, text="¿Qué operación desea realizar?", font=("Helvatica", 16))
    etq_mensaje.pack()

    btn_cliente = Button(ventana, text="Registrar cliente")
    btn_cliente.pack(pady=5)

    btn_direccion = Button(ventana, text="Registrar direccion")
    btn_direccion.pack(pady=5)
        
    btn_bien = Button(ventana, text="Registrar bien", command=lambda: formulario_registrar_bien(ventana))
    btn_bien.pack(pady=5)

    btn_reporte = Button(ventana, text="Ver registros", command=lambda: ver_reporte(ventana))
    btn_reporte.pack(pady=5)

    btn_salir = Button(ventana, text="Salir", command=lambda: salir(ventana))
    btn_salir.pack(pady=5)

    ventana.mainloop()

def formulario_registrar_cliente(ventana: Tk) -> None:
    ventana.withdraw()

def formulario_registrar_direccion(ventana: Tk) -> None:
    ventana.withdraw()

def formulario_registrar_bien(ventana: Tk) -> None:
    ventana.withdraw()
    formulario_captura_bien(ventana)

def ver_reporte(ventana: Tk) -> None:
    ventana.withdraw()
    visualizar_reporte(ventana)

def salir(ventana: Tk) -> None:
    ventana.destroy()