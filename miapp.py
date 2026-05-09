from ui.menu_principal import menu
from seguridad.bitacora import registrarEvento

def mostrar_menu() -> None:
    menu()

if __name__ == "__main__":
    registrarEvento("ha iniciado el sistema.")
    mostrar_menu()
    registrarEvento("ha salido de sistema")