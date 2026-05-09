from tkinter import messagebox
from re import match

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


def validar_usuario(id: str, nombre: str, apellidos: str, celular: str) -> bool:
    patrones = {
        "id": r"^CLI-\d{5}-2[0-6]{3}$",
        "nombre": r"^[a-zA-Z ]{2,}$",
        "apellidos": r"^[a-zA-Z ]+$",
        "celular": r"^\d{10}$"
    }

    if not validar_expresion(patrones["id"], id):
        return False

    if not validar_expresion(patrones["nombre"], id):
        return False

    if not validar_expresion(patrones["apellidos"], id):
        return False

    if not validar_expresion(patrones["celular"], id):
        return False
    
    return True


def validar_direccion(id: str, colonia: str, calle: str, localidad: str, estado: str, postal: str) -> bool:
    patrones = {
        "id": r"^CLI-\d{5}-2[0-6]{3}$",
        "colonia": r"^[a-zA-Z ]+$",
        "calle": r"^[a-zA-Z ]+$",
        "localidad": r"^[a-zA-Z ]+$",
        "estado": r"^[a-zA-Z ]+$",
        "postal": r"^\d{5}$"
    }

    if not validar_expresion(patrones["id"], id):
        return False

    if not validar_expresion(patrones["colonia"], id):
        return False

    if not validar_expresion(patrones["calle"], id):
        return False

    if not validar_expresion(patrones["localidad"], id):
        return False

    if not validar_expresion(patrones["estado"], id):
        return False

    if not validar_expresion(patrones["postal"], id):
        return False
    
    return True