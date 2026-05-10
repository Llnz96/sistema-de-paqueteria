from tkinter import Tk, Toplevel, Label, Entry, ttk, BooleanVar, Checkbutton, Button, messagebox
from utilidades.centrar_ventana import centrar_interfaz
from seguridad.validaciones import validar_direccion
from seguridad.bitacora import registrarEvento
from dominio.direccion import crea_direccion
from persistencia.gestor_manejadores import guardar_direccion

def formulario_captura_direccion(ventana: Tk) -> None:
    form_dir = Toplevel(ventana)
    form_dir.title("Sistema de registro de bienes")
    centrar_interfaz(form_dir, 350, 450)

    etq_titulo = Label(form_dir, text="Registro de dirección", font=("Helvatica", 18, "bold"))
    etq_titulo.grid(row=0, column=1)

    etq_id = Label(form_dir, text="ID:")
    etq_id.grid(row=1, column=0, pady=10, sticky="e")

    txt_id = Entry(form_dir, width=25)
    txt_id.grid(row=1, column=1, pady=10)

    etq_colonia = Label(form_dir, text="Colonia:")
    etq_colonia.grid(row=2, column=0, pady=1, sticky="e")

    txt_colonia = Entry(form_dir, width=25)
    txt_colonia.grid(row=2, column=1, pady=10)

    etq_calle = Label(form_dir, text="Calle:")
    etq_calle.grid(row=3, column=0, pady=1, sticky="e")

    txt_calle = Entry(form_dir, width=25)
    txt_calle.grid(row=3, column=1, pady=10)

    etq_localidad = Label(form_dir, text="Localidad:")
    etq_localidad.grid(row=4, column=0, pady=1, sticky="e")

    txt_localidad = Entry(form_dir, width=25)
    txt_localidad.grid(row=4, column=1, pady=10)

    etq_estado = Label(form_dir, text="Estado:")
    etq_estado.grid(row=5, column=0, pady=1, sticky="e")

    txt_estado = Entry(form_dir, width=25)
    txt_estado.grid(row=5, column=1, pady=10)

    etq_postal = Label(form_dir, text="Postal:")
    etq_postal.grid(row=6, column=0, pady=1, sticky="e")

    txt_postal = Entry(form_dir, width=25)
    txt_postal.grid(row=6, column=1, pady=10)

    etq_formato = Label(form_dir, text="Guardar como:")
    etq_formato.grid(row=7, column=0, pady=1, sticky="e")

    formatos = ["CSV", "JSON"]
    fmt_combo = ttk.Combobox(form_dir, values=formatos, state="readonly")
    fmt_combo.grid(row=7, column=1, pady=10, sticky="w")
    fmt_combo.current(0)

    chk_mantener = BooleanVar()
    chk = Checkbutton(form_dir, text="Mantener datos", variable=chk_mantener)
    chk.grid(row=8, column=1, sticky="w")

    btn_enviar = Button(form_dir, text="Registrar dirección", command=lambda: registrar_direccion(txt_id, txt_colonia, txt_calle, txt_localidad, txt_estado, txt_postal, fmt_combo, chk_mantener))
    btn_enviar.grid(row=9, column=1, sticky="w")
    
    btn_regresar = Button(form_dir, text="Regresar", command=lambda: regresar_menu_principal(ventana, form_dir))
    btn_regresar.grid(row=10, column=1, sticky="w")

    registrarEvento("ha entrado al formulario del registro de direcciones.")

    form_dir.protocol("WM_DELETE_WINDOW", lambda: regresar_menu_principal(ventana, form_dir))

def registrar_direccion(txt_id: Entry, txt_colonia: Entry, txt_calle: Entry, txt_localidad: Entry, txt_estado: Entry, txt_postal: Entry, fmt_combo: ttk.Combobox, chk_mantener: Entry) -> None:
    id = txt_id.get().strip()
    colonia = txt_colonia.get().strip()
    calle = txt_calle.get().strip()
    localidad = txt_localidad.get().strip()
    estado = txt_estado.get().strip()
    postal = txt_postal.get().strip()
    formato = fmt_combo.get()
    persistencia = chk_mantener.get()

    if not validar_direccion(id, colonia, calle, localidad, estado, postal):
        return

    direccion = crea_direccion(id, colonia, calle, localidad, estado, postal)
    guardar_direccion(direccion, formato)

    messagebox.showinfo("Dirección registrada", f"Destino registrado correctamente.")
    registrarEvento(f"ha registrado una dirección satisfactoriamente.")
    
    if not persistencia:
        txt_id.delete(0, "end")
        txt_colonia.delete(0, "end")
        txt_calle.delete(0, "end")
        txt_localidad.delete(0, "end")
        txt_estado.delete(0, "end")
        txt_postal.delete(0, "end")

def regresar_menu_principal(ventana: Tk, form_dir: Tk) -> None:
    form_dir.destroy()
    ventana.deiconify()