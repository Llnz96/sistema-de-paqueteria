from tkinter import Tk, Toplevel, Label, ttk, Text, Button, END
from utilidades.centrar_ventana import centrar_interfaz
from seguridad.bitacora import registrarEvento
from persistencia.gestor_manejadores import generar_dict_bienes, generar_dict_clientes, generar_dict_direcciones

def visualizar_reporte(ventana: Tk) -> None:
    gui_reporte = Toplevel(ventana)
    gui_reporte.title("Listado de bienes")
    centrar_interfaz(gui_reporte,1200, 600)

    etq_formato = Label(gui_reporte, text="Mostrar desde:")
    etq_formato.grid(row=0, column=0, sticky="e")

    formatos = ["CSV", "JSON"]
    fmt_combo = ttk.Combobox(gui_reporte, values=formatos, state="readonly")
    fmt_combo.grid(row=0, column=1, sticky="w")
    fmt_combo.current(0)

    texto = Text(gui_reporte, width=140, height=40)
    texto.grid(row=1, column=1)

    texto.insert(END, "Selecione desde que tipo de archivo leer datos...")

    btn_actualizar = Button(gui_reporte, text="Actualizar", command=lambda: mostrar_datos(texto, fmt_combo))
    btn_actualizar.grid(row=2, column=0, sticky="e")

    btn_regresar = Button(gui_reporte, text="Regresar", command=lambda: regresar_menu_principal(ventana, gui_reporte))
    btn_regresar.grid(row=2, column=1, sticky="w")

    registrarEvento("ha entrado a la visualización del reporte.")

    gui_reporte.protocol("WM_DELETE_WINDOW", lambda: regresar_menu_principal(ventana, gui_reporte))

def mostrar_datos(texto: Text, fmt_combo: ttk.Combobox) -> None:
    texto.delete("1.0", END)

    texto.insert(END, "ID | DESCRIPCIÓN | MODELO | VALOR | ESTATUS\n")
    texto.insert(END, "-" * 43 + "\n")

    bienes = generar_dict_bienes(fmt_combo.get())
    for bien in bienes:
        texto.insert(END, f"{bien["id"]} | {bien["descripcion"]} | {bien["modelo"]} | {bien["valor"]} | {bien["estatus"]}\n")

    texto.insert(END, "ID | NOMBRE | APELLIDO | CELULAR\n")
    texto.insert(END, "-" * 32 + "\n")
    
    clientes = generar_dict_clientes(fmt_combo.get())
    for cliente in clientes:
        texto.insert(END, f"{cliente["id"]} | {cliente["nombre"]} | {cliente["apellido"]} | {cliente["celular"]}\n")

    texto.insert(END, "ID | COLONIA | CALLE | LOCALIDAD | ESTADO | POSTAL\n")
    texto.insert(END, "-" * 50 + "\n")
    
    direcciones = generar_dict_direcciones(fmt_combo.get())
    for dir in direcciones:
        texto.insert(END, f"{dir["id"]} | {dir["colonia"]} | {dir["calle"]} | {dir["localidad"]} | {dir["estado"]} | {dir["postal"]}\n")

def regresar_menu_principal(ventana: Tk, gui_reporte: Tk) -> None:
    gui_reporte.destroy()
    ventana.deiconify()
    registrarEvento("ha salido de la visualización del reporte.")