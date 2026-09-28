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



