from tkinter import messagebox
from re import match
from datetime import datetime

def validar_expresion(patron: str, cadena: str) -> bool:
    return bool(match(patron, cadena))

def validar_bien(id: str, desc: str, modelo: str, valor: str, estatus: str) -> bool:
    if not id or not desc or not modelo or not valor or not estatus:
        messagebox.showerror("Error", "Debes completar todos los campos.")
        return False

    patrones = {
        "id": r"^\d+$",
        "desc": r"^[a-zA-Z.,\- ]+$",
        "modelo": r"^[a-zA-Z\d ]+$",
        "valor": r"^\d{1,3}(,\d{1,3})*(\.\d+)?$"
    }

    if not validar_expresion(patrones["id"], id):
        messagebox.showerror("Error", "El ID debe ser númerico.")
        return False
    
    if not validar_expresion(patrones["desc"], desc):
        messagebox.showerror("Error", "No se permiten números o caracteres especiales en el modelo excepto: \".\", \",\", \"-\".")
        return False

    if not validar_expresion(patrones["modelo"], modelo):
        messagebox.showerror("Error", "No se permiten caracteres especiales en el modelo.")
        return False
    
    if not validar_expresion(patrones["valor"], valor):
        messagebox.showerror("Error", "Use el formato correcto de miles y decimales. Ejemplo: 1,000.50")
        return False

    return True


def validar_cliente(id: str, nombre: str, apellidos: str, celular: str) -> bool:
    if not id or not nombre or not apellidos or not celular:
        messagebox.showerror("Error", "Debes completar todos los campos.")
        return False

    patrones = {
        "id": r"^CLI-\d{5}-\d{4}$",
        "nombre": r"^[a-zA-Z ]{2,}$",
        "apellidos": r"^[a-zA-Z ]{2,}$",
        "celular": r"^\d{10}$"
    }

    if not validar_expresion(patrones["id"], id):
        messagebox.showerror("Error", "El ID debe serguir el formato \"CLI-00000-YYYY\"")
        return False
    
    anio_id = id[-4:]
    anio = int(anio_id)
    anio_actual = datetime.now().year

    if anio < 2000 or anio > anio_actual:
        messagebox.showerror("Error", "El año debe respetar el rango 2000-Actual.")
        return 

    if not validar_expresion(patrones["nombre"], nombre):
        messagebox.showerror("Error", "El nombre no puede contener caracteres especiales o números.")
        return False

    if not validar_expresion(patrones["apellidos"], apellidos):
        messagebox.showerror("Error", "El apellido no puede contener caracteres especiales o números.")
        return False

    if not validar_expresion(patrones["celular"], celular):
        messagebox.showerror("Error", "El celular solo deben 10 digitos.")
        return False
    
    return True


def validar_direccion(id: str, colonia: str, calle: str, localidad: str, estado: str, postal: str) -> bool:
    if not id or not colonia or not calle or not localidad or not estado or not postal:
        messagebox.showerror("Error", "Debes completar todos los campos.")
        return False

    patrones = {
        "id": r"^CLI-\d{5}-\d{4}$",
        "colonia": r"^[a-zA-Z ]+$",
        "calle": r"^[a-zA-Z ]+$",
        "localidad": r"^[a-zA-Z ]+$",
        "estado": r"^[a-zA-Z ]+$",
        "postal": r"^\d{5}$"
    }

    if not validar_expresion(patrones["id"], id):
        return False
    
    anio_id = id[-4:]
    anio = int(anio_id)
    anio_actual = datetime.now().year

    if anio < 2000 or anio > anio_actual:
        messagebox.showerror("Error", "El año debe respetar el rango 2000-Actual.")
        return 

    if not validar_expresion(patrones["colonia"], colonia):
        messagebox.showerror("Error", "La colonia solo debe contener letras.")
        return False

    if not validar_expresion(patrones["calle"], calle):
        messagebox.showerror("Error", "La calle solo debe contener letras.")
        return False

    if not validar_expresion(patrones["localidad"], localidad):
        messagebox.showerror("Error", "La localidad solo debe contener letras.")
        return False

    if not validar_expresion(patrones["estado"], estado):
        messagebox.showerror("Error", "El estado solo debe contener letras.")
        return False

    if not validar_expresion(patrones["postal"], postal):
        messagebox.showerror("Error", "El código postal solo debe contener 5 dígitos.")
        return False
    
    return True