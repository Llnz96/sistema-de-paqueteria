from tkinter import Tk, Toplevel, Label, ttk, Text, Button, END
from utilidades.centrar_ventana import centrar_interfaz
from seguridad.bitacora import registrarEvento

def visualizar_reporte(ventana: Tk) -> None:
    gui_reporte = Toplevel(ventana)
    gui_reporte.title("Listado de bienes")
    centrar_interfaz(gui_reporte, 600, 300)

    etq_formato = Label(gui_reporte, text="Mostrar desde:")
    etq_formato.grid(row=0, column=0, sticky="e")

    formatos = ["CSV", "JSON"]
    fmt_combo = ttk.Combobox(gui_reporte, values=formatos, state="readonly")
    fmt_combo.grid(row=0, column=1, sticky="w")
    fmt_combo.current(0)

    texto = Text(gui_reporte, width=60, height=15)
    texto.grid(row=1, column=1)

    texto.insert(END, "Selecione desde que tipo de archivo leer datos...")

    btn_actualizar = Button(gui_reporte, text="Actualizar")
    btn_actualizar.grid(row=2, column=0, sticky="e")

    btn_regresar = Button(gui_reporte, text="Regresar", command=lambda: regresar_menu_principal(ventana, gui_reporte))
    btn_regresar.grid(row=2, column=1, sticky="w")

    registrarEvento("ha entrado a la visualización del reporte.")

    gui_reporte.protocol("WM_DELETE_WINDOW", lambda: regresar_menu_principal(ventana, gui_reporte))

def regresar_menu_principal(ventana: Tk, gui_reporte: Tk) -> None:
    gui_reporte.destroy()
    ventana.deiconify()
    registrarEvento("ha salido de la visualización del reporte.")