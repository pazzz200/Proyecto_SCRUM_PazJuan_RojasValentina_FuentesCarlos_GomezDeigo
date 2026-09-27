"""
gestion.py - Lógica de negocio: registro de clientes, instructores,
inscripciones/matrículas y validaciones del sistema Gimnasio ForceTech.
"""

import datos


# ---------- VALIDACIONES ----------

def validar_texto_no_vacio(texto):
    """Verifica que un texto no esté vacío ni sea solo espacios."""
    return isinstance(texto, str) and texto.strip() != ""


def validar_cedula(cedula):
    """Verifica que la cédula sea numérica y tenga al menos 6 dígitos."""
    return cedula.isdigit() and len(cedula) >= 6


def validar_edad(edad):
    """Verifica que la edad sea un número entero válido y realista."""
    try:
        edad = int(edad)
        return 0 < edad < 120
    except (ValueError, TypeError):
        return False


def validar_servicio(servicio):
    """Verifica que el servicio exista en la lista de servicios disponibles."""
    return servicio in datos.servicios_disponibles


# ---------- CLIENTES ----------

def registrar_cliente(nombre, cedula, edad):
    """Registra un nuevo cliente si los datos son válidos."""
    if not validar_texto_no_vacio(nombre):
        return False, "El nombre no puede estar vacío."
    if not validar_cedula(cedula):
        return False, "Cédula inválida (solo números, mínimo 6 dígitos)."
    if not validar_edad(edad):
        return False, "Edad inválida."

    cliente = {
        "id": datos.contador_cliente_id,
        "nombre": nombre.strip(),
        "cedula": cedula,
        "edad": int(edad),
        "servicios": []
    }
    datos.clientes.append(cliente)
    datos.contador_cliente_id += 1
    return True, f"Cliente '{nombre}' registrado con ID {cliente['id']}."


def buscar_cliente_por_id(cliente_id):
    """Busca un cliente por su ID. Retorna None si no existe."""
    for cliente in datos.clientes:
        if cliente["id"] == cliente_id:
            return cliente
    return None


def listar_clientes():
    """Retorna la lista completa de clientes."""
    return datos.clientes


# ---------- INSTRUCTORES ----------

def registrar_instructor(nombre, especialidad):
    """Registra un nuevo instructor si los datos son válidos."""
    if not validar_texto_no_vacio(nombre):
        return False, "El nombre no puede estar vacío."
    if not validar_servicio(especialidad):
        return False, f"Especialidad inválida. Opciones: {', '.join(datos.servicios_disponibles)}"

    instructor = {
        "id": datos.contador_instructor_id,
        "nombre": nombre.strip(),
        "especialidad": especialidad
    }
    datos.instructores.append(instructor)
    datos.contador_instructor_id += 1
    return True, f"Instructor '{nombre}' registrado con ID {instructor['id']}."


def listar_instructores():
    """Retorna la lista completa de instructores."""
    return datos.instructores


# ---------- MATRÍCULAS / INSCRIPCIONES ----------

def inscribir_cliente_en_servicio(cliente_id, servicio):
    """Inscribe a un cliente existente en un servicio del gimnasio."""
    cliente = buscar_cliente_por_id(cliente_id)
    if cliente is None:
        return False, "Cliente no encontrado."
    if not validar_servicio(servicio):
        return False, f"Servicio inválido. Opciones: {', '.join(datos.servicios_disponibles)}"
    if servicio in cliente["servicios"]:
        return False, f"El cliente ya está inscrito en {servicio}."

    matricula = {
        "id": datos.contador_matricula_id,
        "cliente_id": cliente_id,
        "servicio": servicio
    }
    datos.matriculas.append(matricula)
    cliente["servicios"].append(servicio)
    datos.contador_matricula_id += 1
    return True, f"Cliente '{cliente['nombre']}' inscrito en {servicio}."


def listar_matriculas():
    """Retorna la lista completa de matrículas."""
    return datos.matriculas
