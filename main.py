import gestion
import reportes
import datos


def menu_principal():
    while True:
        print("\n===== GIMNASIO FORCETECH =====")
        print("1. Registrar cliente")
        print("2. Registrar instructor")
        print("3. Inscribir cliente en un servicio")
        print("4. Listar clientes")
        print("5. Listar instructores")
        print("6. Ver reportes")
        print("0. Salir")

        opcion = input("Selecciona una opción: ").strip()


