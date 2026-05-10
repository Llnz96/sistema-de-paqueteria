from tkinter import Tk, Toplevel, Label, Entry, ttk, BooleanVar, Checkbutton, Button, messagebox
from utilidades.centrar_ventana import centrar_interfaz
from seguridad.validaciones import validar_cliente
from seguridad.bitacora import registrarEvento
from dominio.cliente import crea_cliente
from persistencia.gestor_manejadores import guardar_cliente

def formulario_captura_cliente(ventana: Tk) -> None:
    form_cli = Toplevel(ventana)
    form_cli.title("Sistema de registro de bienes")
    centrar_interfaz(form_cli, 350, 410)

    etq_titulo = Label(form_cli, text="Registro de cliente", font=("Helvatica", 18, "bold"))
    etq_titulo.grid(row=0, column=1)

    etq_id = Label(form_cli, text="ID:")
    etq_id.grid(row=1, column=0, pady=10, sticky="e")

    txt_id = Entry(form_cli, width=25)
    txt_id.grid(row=1, column=1, pady=10)

    etq_nombre = Label(form_cli, text="Nombre:")
    etq_nombre.grid(row=2, column=0, pady=1, sticky="e")

    txt_nombre = Entry(form_cli, width=25)
    txt_nombre.grid(row=2, column=1, pady=10)

    etq_apellido = Label(form_cli, text="Apellido:")
    etq_apellido.grid(row=3, column=0, pady=1, sticky="e")

    txt_apellido = Entry(form_cli, width=25)
    txt_apellido.grid(row=3, column=1, pady=10)

    etq_celular = Label(form_cli, text="Celular:")
    etq_celular.grid(row=4, column=0, pady=1, sticky="e")

    txt_celular = Entry(form_cli, width=25)
    txt_celular.grid(row=4, column=1, pady=10)

    etq_formato = Label(form_cli, text="Guardar como:")
    etq_formato.grid(row=5, column=0, pady=1, sticky="e")

    formatos = ["CSV", "JSON"]
    fmt_combo = ttk.Combobox(form_cli, values=formatos, state="readonly")
    fmt_combo.grid(row=5, column=1, pady=10, sticky="w")
    fmt_combo.current(0)

    chk_mantener = BooleanVar()
    chk = Checkbutton(form_cli, text="Mantener datos", variable=chk_mantener)
    chk.grid(row=6, column=1, sticky="w")

    btn_enviar = Button(form_cli, text="Registrar cliente", command=lambda: registrar_cliente(txt_id, txt_nombre, txt_apellido, txt_celular, fmt_combo, chk_mantener))
    btn_enviar.grid(row=7, column=1, sticky="w")
    
    btn_regresar = Button(form_cli, text="Regresar", command=lambda: regresar_menu_principal(ventana, form_cli))
    btn_regresar.grid(row=8, column=1, sticky="w")

    registrarEvento("ha entrado al formulario de registro de clientes.")

    form_cli.protocol("WM_DELETE_WINDOW", lambda: regresar_menu_principal(ventana, form_cli))

def registrar_cliente(txt_id: Entry, txt_nombre: Entry, txt_apellido: Entry, txt_celular: Entry, fmt_combo: ttk.Combobox, chk_mantener: Entry) -> None:
    id = txt_id.get().strip()
    nombre = txt_nombre.get().strip()
    apellido = txt_apellido.get().strip()
    celular = txt_celular.get().strip()
    formato = fmt_combo.get()
    persistencia = chk_mantener.get()

    if not validar_cliente(id, nombre, apellido, celular):
        return

    cliente = crea_cliente(id, nombre, apellido, celular)
    guardar_cliente(cliente, formato)

    messagebox.showinfo("Cliente registrado", f"{nombre} registrado satisfactoriamente.")
    registrarEvento(f"ha registrado un cliente satisfactoriamente.")
    
    if not persistencia:
        txt_id.delete(0, "end")
        txt_nombre.delete(0, "end")
        txt_apellido.delete(0, "end")
        txt_celular.delete(0, "end")

def regresar_menu_principal(ventana: Tk, form_cli: Tk) -> None:
    form_cli.destroy()
    ventana.deiconify()