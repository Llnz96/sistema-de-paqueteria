import tkinter as tk
from tkinter import messagebox, ttk
from re import match
import sqlite3
from socket import gethostbyname, gethostname
from datetime import datetime

patrones = {
    "ID": r"^\d+$",
    "bien": r"^[a-zA-Z ]+$",
    "marca": r"^[a-zA-Z\d ]+$",
    "valor": r"^\d{1,3}(,\d{1,3})*(\.\d+)?$"
}

# ---------------- FUNCIONES ----------------

def validarExpresion(patron: str, cadena: str) -> bool:
    return bool(match(patron, cadena))


def validarEntradas(id_bien:str , bien: str, marca: str, valor: str) -> bool:
    if not id_bien or not bien or not marca or not valor:
        messagebox.showerror("Error", "Debes llenar todos los campos.")
        return False

    if not validarExpresion(patrones["ID"], id_bien):
        messagebox.showerror("Error", "El ID debe ser un valor númerico.")
        return False
    
    if not validarExpresion(patrones["bien"], bien):
        messagebox.showerror("Error", "No se permiten números ni caracteres especiales en el bien.")
        return False
    
    if not validarExpresion(patrones["marca"], marca):
        messagebox.showerror("Error", "No se permiten caracteres especiales en la marca.")
        return False
    
    if not validarExpresion(patrones["valor"], valor):
        messagebox.showerror("Error", "Use el formato correcto de miles y decimales. Ejemplo: 1,000.50")
        return False
    
    return True


def generarBaseDeDatos() -> None:
    conn = sqlite3.connect("bienes.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS bienes(
        id INTEGER,
        bien TEXT,
        marca TEXT,
        valor REAL,
        estado TEXT
    )
    """)

    conn.commit()
    conn.close()


def registrarEvento(mensaje: str) -> None:
    ip = gethostbyname(gethostname())
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("bienes.log", "a", encoding="utf-8") as archivo:
        archivo.write(f"[{fecha}] {ip} {mensaje}\n")


def registrarBien(id: int, bien: str, marca: str, valor: str, estado: str) -> None:
    conn = sqlite3.connect("bienes.db")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO bienes (id, bien, marca, valor, estado) VALUES (?, ?, ?, ?, ?)",
        (id, bien, marca, valor, estado)
    )

    registrarEvento(f"ha registrado el producto: {id} - {bien} - {marca} - {valor} - {estado}")

    conn.commit()
    conn.close()


def enviar():
    id_bien = txt_id.get().strip()
    bien = txt_bien.get().strip()
    marca = txt_marca.get().strip()
    valor = txt_valor.get().strip()
    estado = combo.get()

    if not validarEntradas(id_bien, bien, marca, valor):
        return
    
    valor = valor.replace(",", "")
    precio = float(valor)

    registrarBien(id_bien, bien, marca, precio, estado)

    messagebox.showinfo("Producto agregado", f"{bien} registrado correctamente")

    if not chk_mantener.get():
        txt_id.delete(0, "end")
        txt_bien.delete(0, "end")
        txt_marca.delete(0, "end")
        txt_valor.delete(0, "end")
        combo.current(0)


def mostrarListado():
    ventana.withdraw()

    lista_win = tk.Toplevel()
    lista_win.title("Listado de bienes")
    lista_win.geometry("500x300")

    conn = sqlite3.connect("bienes.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM bienes")
    datos = cur.fetchall()

    conn.close()

    texto = tk.Text(lista_win, width=60, height=15)
    texto.pack()

    texto.insert(tk.END, "ID | BIEN | MARCA | VALOR | ESTADO\n")
    texto.insert(tk.END, "-" * 50 + "\n")

    for fila in datos:
        texto.insert(tk.END, f"{fila[0]} | {fila[1]} | {fila[2]} | {fila[3]} | {fila[4]}\n")

    registrarEvento(f"ha entrado a la visualización de bienes registrados.")

    def regresar():
        lista_win.destroy()
        ventana.deiconify()
        registrarEvento("ha regresado al registro de bienes.")

    btn_regresar = tk.Button(lista_win, text="Regresar", command=regresar)
    btn_regresar.pack(pady=10)


# ---------------- INTERFAZ ----------------

if __name__ == "__main__":
    generarBaseDeDatos()
    registrarEvento("ha ingresado al sistema.")

    ventana = tk.Tk()
    ventana.title("Sistema de registro de bienes")
    ventana.geometry("350x380")

    etq_titulo = tk.Label(ventana, text="Alta de bienes")
    etq_titulo.grid(row=0, column=1)

    etq_id = tk.Label(ventana, text="ID:")
    etq_id.grid(row=1, column=0, pady=10)

    txt_id = tk.Entry(ventana, width=30)
    txt_id.grid(row=1, column=1, pady=10)

    etq_bien = tk.Label(ventana, text="Bien:")
    etq_bien.grid(row=2, column=0, pady=1)

    txt_bien = tk.Entry(ventana, width=30)
    txt_bien.grid(row=2, column=1, pady=10)

    etq_marca = tk.Label(ventana, text="Marca:")
    etq_marca.grid(row=3, column=0, pady=1)

    txt_marca = tk.Entry(ventana, width=30)
    txt_marca.grid(row=3, column=1, pady=10)

    etq_valor = tk.Label(ventana, text="Valor:")
    etq_valor.grid(row=4, column=0, pady=1)

    txt_valor = tk.Entry(ventana, width=30)
    txt_valor.grid(row=4, column=1, pady=10)

    etq_estado = tk.Label(ventana, text="Estado:")
    etq_estado.grid(row=5, column=0, pady=1)

    opciones = ["Nuevo", "Excelente", "Bueno", "Regular", "Desgastado", "Dañado"]
    combo = ttk.Combobox(ventana, values=opciones, state="readonly")
    combo.grid(row=5, column=1, pady=10)
    combo.current(0)

    chk_mantener = tk.BooleanVar()
    chk = tk.Checkbutton(ventana, text="Mantener datos", variable=chk_mantener)
    chk.grid(row=6, column=1)

    btn_enviar = tk.Button(ventana, text="Enviar", command=enviar)
    btn_enviar.grid(row=7, column=1)

    btn_listar = tk.Button(ventana, text="Ver registros", command=mostrarListado)
    btn_listar.grid(row=8, column=1)

    ventana.mainloop()

    registrarEvento("ha salido del sistema.")