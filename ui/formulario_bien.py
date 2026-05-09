import tkinter as tk
from tkinter import messagebox, ttk
from re import match
import sqlite3
from socket import gethostbyname, gethostname
from datetime import datetime

def captura_bien():

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

    btn_enviar = tk.Button(ventana, text="Enviar")
    btn_enviar.grid(row=7, column=1)

    btn_listar = tk.Button(ventana, text="Ver registros")
    btn_listar.grid(row=8, column=1)

    ventana.mainloop()
