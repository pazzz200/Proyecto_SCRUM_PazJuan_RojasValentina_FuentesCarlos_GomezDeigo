import datos


def reporte_clientes():
    """Imprime un listado de todos los clientes con sus servicios."""
    if not datos.clientes:
        print("No hay clientes registrados.")
        return
    print("\n--- REPORTE DE CLIENTES ---")
    for c in datos.clientes:
        servicios = ", ".join(c["servicios"]) if c["servicios"] else "Ninguno"
        print(f"ID: {c['id']} | Nombre: {c['nombre']} | Cédula: {c['cedula']} | "
              f"Edad: {c['edad']} | Servicios: {servicios}")


def reporte_instructores():
    """Imprime un listado de todos los instructores."""
    if not datos.instructores:
        print("No hay instructores registrados.")
        return
    print("\n--- REPORTE DE INSTRUCTORES ---")
    for i in datos.instructores:
        print(f"ID: {i['id']} | Nombre: {i['nombre']} | Especialidad: {i['especialidad']}")


def reporte_inscripciones_por_servicio():
    """Muestra cuántos clientes hay inscritos en cada servicio."""
    print("\n--- INSCRIPCIONES POR SERVICIO ---")
    for servicio in datos.servicios_disponibles:
        cantidad = sum(1 for m in datos.matriculas if m["servicio"] == servicio)
        print(f"{servicio}: {cantidad} inscrito(s)")


def reporte_general():
    """Muestra un resumen general del estado del gimnasio."""
    print("\n=== REPORTE GENERAL DEL GIMNASIO FORCETECH ===")
    print(f"Total de clientes: {len(datos.clientes)}")
    print(f"Total de instructores: {len(datos.instructores)}")
    print(f"Total de matrículas: {len(datos.matriculas)}")
    reporte_inscripciones_por_servicio()

