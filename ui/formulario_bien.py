from tkinter import Tk, Toplevel, Label, Entry, ttk, BooleanVar, Checkbutton, Button, messagebox
from utilidades.centrar_ventana import centrar_interfaz
from seguridad.validaciones import validar_bien
from seguridad.bitacora import registrarEvento
from dominio.bien import crea_bien
from persistencia.gestor_manejadores import guardar_bien

def formulario_captura_bien(ventana: Tk) -> None:
    form_bien = Toplevel(ventana)
    form_bien.title("Sistema de registro de bienes")
    centrar_interfaz(form_bien, 350, 410)

    etq_titulo = Label(form_bien, text="Alta de bienes", font=("Helvatica", 18, "bold"))
    etq_titulo.grid(row=0, column=1)

    etq_id = Label(form_bien, text="ID:")
    etq_id.grid(row=1, column=0, pady=10, sticky="e")

    txt_id = Entry(form_bien, width=25)
    txt_id.grid(row=1, column=1, pady=10)

    etq_desc = Label(form_bien, text="Descripción:")
    etq_desc.grid(row=2, column=0, pady=1, sticky="e")

    txt_desc = Entry(form_bien, width=25)
    txt_desc.grid(row=2, column=1, pady=10)

    etq_modelo = Label(form_bien, text="Modelo:")
    etq_modelo.grid(row=3, column=0, pady=1, sticky="e")

    txt_modelo = Entry(form_bien, width=25)
    txt_modelo.grid(row=3, column=1, pady=10)

    etq_valor = Label(form_bien, text="Valor:")
    etq_valor.grid(row=4, column=0, pady=1, sticky="e")

    txt_valor = Entry(form_bien, width=25)
    txt_valor.grid(row=4, column=1, pady=10)

    etq_estado = Label(form_bien, text="Estatus:")
    etq_estado.grid(row=5, column=0, pady=1, sticky="e")

    opciones = ["Nuevo", "Excelente", "Bueno", "Regular", "Desgastado", "Dañado"]
    combo = ttk.Combobox(form_bien, values=opciones, state="readonly")
    combo.grid(row=5, column=1, pady=10, sticky="w")
    combo.current(0)

    etq_formato = Label(form_bien, text="Guardar como:")
    etq_formato.grid(row=6, column=0, pady=1, sticky="e")

    formatos = ["CSV", "JSON"]
    fmt_combo = ttk.Combobox(form_bien, values=formatos, state="readonly")
    fmt_combo.grid(row=6, column=1, pady=10, sticky="w")
    fmt_combo.current(0)

    chk_mantener = BooleanVar()
    chk = Checkbutton(form_bien, text="Mantener datos", variable=chk_mantener)
    chk.grid(row=7, column=1, sticky="w")

    btn_enviar = Button(form_bien, text="Registrar bien", command=lambda: registrar_bien(txt_id, txt_desc, txt_modelo, txt_valor, combo, fmt_combo, chk_mantener))
    btn_enviar.grid(row=8, column=1, sticky="w")
    
    btn_regresar = Button(form_bien, text="Regresar", command=lambda: regresar_menu_principal(ventana, form_bien))
    btn_regresar.grid(row=9, column=1, sticky="w")

    registrarEvento("ha entrado al formulario del registro de bienes.")

    form_bien.protocol("WM_DELETE_WINDOW", lambda: regresar_menu_principal(ventana, form_bien))

def registrar_bien(txt_id: Entry, txt_desc: Entry, txt_modelo: Entry, txt_valor: Entry, combo: ttk.Combobox, fmt_combo: ttk.Combobox, chk_mantener: Entry) -> None:
    id = txt_id.get().strip()
    desc = txt_desc.get().strip()
    modelo = txt_modelo.get().strip()
    valor = txt_valor.get().strip()
    estatus = combo.get()
    formato = fmt_combo.get()
    persistencia = chk_mantener.get()

    if not validar_bien(id, desc, modelo, valor, estatus):
        return
    
    valor = valor.replace(",", "")
    precio = float(valor)

    bien = crea_bien(id, desc, modelo, precio, estatus)
    guardar_bien(bien, formato)

    messagebox.showinfo("Producto registrado", f"{desc} registrado correctamente.")
    registrarEvento(f"ha registrado un producto satisfactoriamente.")
    
    if not persistencia:
        txt_id.delete(0, "end")
        txt_desc.delete(0, "end")
        txt_modelo.delete(0, "end")
        txt_valor.delete(0, "end")
        combo.current(0)

def regresar_menu_principal(ventana: Tk, form_bien: Tk) -> None:
    form_bien.destroy()
    ventana.deiconify()