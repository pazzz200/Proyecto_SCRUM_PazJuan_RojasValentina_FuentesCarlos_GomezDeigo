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

        if opcion == "1":
            registrar_cliente_menu()
        elif opcion == "2":
            registrar_instructor_menu()
        elif opcion == "3":
            inscribir_cliente_menu()
        elif opcion == "4":
            listar_clientes_menu()
        elif opcion == "5":
            listar_instructores_menu()
        elif opcion == "6":
            menu_reportes()
        elif opcion == "0":
            print("¡Gracias por usar el sistema de Gimnasio ForceTech!")
            break
        else:
            print("Opción inválida, intenta de nuevo.")


def registrar_cliente_menu():
    nombre = input("Nombre del cliente: ")
    cedula = input("Cédula: ")
    edad = input("Edad: ")
    exito, mensaje = gestion.registrar_cliente(nombre, cedula, edad)
    print(mensaje)


def registrar_instructor_menu():
    nombre = input("Nombre del instructor: ")
    print(f"Especialidades disponibles: {', '.join(datos.servicios_disponibles)}")
    especialidad = input("Especialidad: ")
    exito, mensaje = gestion.registrar_instructor(nombre, especialidad)
    print(mensaje)


def inscribir_cliente_menu():
    try:
        cliente_id = int(input("ID del cliente: "))
    except ValueError:
        print("ID inválido.")
        return
    print(f"Servicios disponibles: {', '.join(datos.servicios_disponibles)}")
    servicio = input("Servicio: ")
    exito, mensaje = gestion.inscribir_cliente_en_servicio(cliente_id, servicio)
    print(mensaje)


def listar_clientes_menu():
    clientes = gestion.listar_clientes()
    if not clientes:
        print("No hay clientes registrados.")
        return
    for c in clientes:
        print(f"ID: {c['id']} | Nombre: {c['nombre']} | Cédula: {c['cedula']} | Edad: {c['edad']}")


def listar_instructores_menu():
    instructores = gestion.listar_instructores()
    if not instructores:
        print("No hay instructores registrados.")
        return
    for i in instructores:
        print(f"ID: {i['id']} | Nombre: {i['nombre']} | Especialidad: {i['especialidad']}")


def menu_reportes():
    print("\n--- MENÚ DE REPORTES ---")
    print("1. Reporte de clientes")
    print("2. Reporte de instructores")
    print("3. Inscripciones por servicio")
    print("4. Reporte general")
    opcion = input("Selecciona una opción: ").strip()

    if opcion == "1":
        reportes.reporte_clientes()
    elif opcion == "2":
        reportes.reporte_instructores()
    elif opcion == "3":
        reportes.reporte_inscripciones_por_servicio()
    elif opcion == "4":
        reportes.reporte_general()
    else:
        print("Opción inválida.")


if __name__ == "__main__":
    menu_principal()

