"""
datos.py - Estructuras de datos iniciales para el sistema de gestión
del Gimnasio ForceTech.
"""

# Servicios disponibles en el gimnasio
servicios_disponibles = ["Yoga", "Pilates", "Entrenamiento Funcional", "Piscina"]

# Lista de clientes registrados (cada cliente es un diccionario)
clientes = []

# Lista de instructores registrados
instructores = []

# Lista de matrículas/inscripciones (relación cliente-servicio)
matriculas = []

# Contadores para generar IDs únicos de forma automática
contador_cliente_id = 1
contador_instructor_id = 1
contador_matricula_id = 1
