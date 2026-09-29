# Gimnasio ForceTech — Sistema de Gestión

Sistema de consola en Python para la gestión de un gimnasio: inscripciones de clientes, registro de instructores, matrículas en servicios y generación de reportes. Desarrollado aplicando el marco de trabajo ágil **Scrum**.

## Integrantes del equipo

- Diego Gomez
- Juan David Paz
- Valentina Rojas
- Carlos

## Roles Scrum

| Rol | Integrante |
|---|---|
| Product Owner | Carlos |
| Scrum Master | Valentina |
| Development Team | Juan David y Diego |

## Tecnologías

- **Lenguaje:** Python 3
- **Paradigma:** Programación estructurada / modular (sin librerías externas)

## Estructura del proyecto

```
├── datos.py       # Estructuras de datos iniciales (almacenamiento en memoria)
├── gestion.py      # Lógica de negocio, validaciones y operaciones CRUD
├── reportes.py     # Generación de reportes en consola
├── main.py          # Punto de entrada y menú principal
└── README.md
```

## Cómo ejecutar el sistema

Requiere Python 3 instalado. Desde la raíz del proyecto:

```bash
python main.py
```

Se abrirá un menú interactivo en la consola con las siguientes opciones:

```
===== GIMNASIO FORCETECH =====
1. Registrar cliente
2. Registrar instructor
3. Inscribir cliente en un servicio
4. Listar clientes
5. Listar instructores
6. Ver reportes
0. Salir
```

---

## Descripción detallada de cada archivo

### `datos.py` — Estructuras de datos

Actúa como el almacén central de información del sistema. No contiene funciones, solo variables que guardan el estado mientras el programa corre (simulando una base de datos en memoria):

| Variable | Tipo | Descripción |
|---|---|---|
| `servicios_disponibles` | `list[str]` | Lista fija con los 4 servicios: Yoga, Pilates, Entrenamiento Funcional, Piscina |
| `clientes` | `list[dict]` | Clientes registrados |
| `instructores` | `list[dict]` | Instructores registrados |
| `matriculas` | `list[dict]` | Inscripciones cliente–servicio |
| `contador_cliente_id` | `int` | Siguiente ID disponible para un cliente nuevo |
| `contador_instructor_id` | `int` | Siguiente ID disponible para un instructor nuevo |
| `contador_matricula_id` | `int` | Siguiente ID disponible para una matrícula nueva |

**Estructura de un cliente:**
```python
{"id": 1, "nombre": "Diego Gomez", "cedula": "1234567", "edad": 25, "servicios": ["Yoga"]}
```

**Estructura de un instructor:**
```python
{"id": 1, "nombre": "Ana Pérez", "especialidad": "Pilates"}
```

**Estructura de una matrícula:**
```python
{"id": 1, "cliente_id": 1, "servicio": "Yoga"}
```

---

### `gestion.py` — Lógica de negocio y validaciones

Contiene todas las funciones que crean, validan y consultan los datos de `datos.py`. Depende de `datos.py` (`import datos`).

#### Validaciones

| Función | Parámetros | Retorna | Descripción |
|---|---|---|---|
| `validar_texto_no_vacio(texto)` | `texto: str` | `bool` | Verifica que el texto no esté vacío ni sea solo espacios |
| `validar_cedula(cedula)` | `cedula: str` | `bool` | Verifica que sea numérica y tenga mínimo 6 dígitos |
| `validar_edad(edad)` | `edad: str/int` | `bool` | Verifica que sea un entero entre 0 y 120 |
| `validar_servicio(servicio)` | `servicio: str` | `bool` | Verifica que exista en `servicios_disponibles` |

#### Clientes

| Función | Descripción |
|---|---|
| `registrar_cliente(nombre, cedula, edad)` | Valida los datos y agrega un cliente nuevo. Retorna `(bool, mensaje)` |
| `buscar_cliente_por_id(cliente_id)` | Retorna el diccionario del cliente o `None` si no existe |
| `listar_clientes()` | Retorna la lista completa de clientes |

#### Instructores

| Función | Descripción |
|---|---|
| `registrar_instructor(nombre, especialidad)` | Valida y agrega un instructor nuevo. Retorna `(bool, mensaje)` |
| `listar_instructores()` | Retorna la lista completa de instructores |

#### Matrículas

| Función | Descripción |
|---|---|
| `inscribir_cliente_en_servicio(cliente_id, servicio)` | Valida que el cliente exista, el servicio sea válido y no esté ya inscrito; crea la matrícula. Retorna `(bool, mensaje)` |
| `listar_matriculas()` | Retorna la lista completa de matrículas |

**Convención de retorno:** todas las funciones de registro/inscripción retornan una tupla `(exito: bool, mensaje: str)`, para que quien las llame (normalmente `main.py`) sepa si la operación fue exitosa y qué mensaje mostrarle al usuario.

---

### `reportes.py` — Generación de reportes

Contiene funciones que **leen** los datos de `datos.py` (nunca los modifican) y los imprimen en consola de forma organizada. Depende de `datos.py`.

| Función | Descripción |
|---|---|
| `reporte_clientes()` | Imprime todos los clientes con sus servicios inscritos |
| `reporte_instructores()` | Imprime todos los instructores registrados |
| `reporte_inscripciones_por_servicio()` | Muestra cuántos clientes hay inscritos en cada uno de los 4 servicios |
| `reporte_general()` | Resumen con totales de clientes, instructores, matrículas, y el detalle por servicio |

---

### `main.py` — Punto de entrada y menú principal

Conecta todo el sistema con el usuario a través de un menú de consola en bucle. Depende de `gestion.py`, `reportes.py` y `datos.py`.

| Función | Descripción |
|---|---|
| `menu_principal()` | Bucle principal: muestra el menú y redirige a la opción elegida hasta que el usuario selecciona "Salir" |
| `registrar_cliente_menu()` | Pide los datos de un cliente por consola y llama a `gestion.registrar_cliente()` |
| `registrar_instructor_menu()` | Pide los datos de un instructor por consola y llama a `gestion.registrar_instructor()` |
| `inscribir_cliente_menu()` | Pide un ID de cliente y un servicio, y llama a `gestion.inscribir_cliente_en_servicio()` |
| `listar_clientes_menu()` | Muestra en consola la lista de clientes vía `gestion.listar_clientes()` |
| `listar_instructores_menu()` | Muestra en consola la lista de instructores vía `gestion.listar_instructores()` |
| `menu_reportes()` | Submenú que redirige a las funciones de `reportes.py` |

El bloque `if __name__ == "__main__":` al final asegura que `menu_principal()` solo se ejecute cuando corres `main.py` directamente (no si alguien lo importa como módulo).

---

## Flujo típico de uso

1. El usuario registra uno o más **instructores** (opción 2)
2. El usuario registra uno o más **clientes** (opción 1)
3. Inscribe a un cliente en un **servicio** usando su ID (opción 3)
4. Consulta los **reportes** para ver el estado general del gimnasio (opción 6)

## Diagrama de dependencias entre archivos

```
main.py
  ├── gestion.py
  │     └── datos.py
  ├── reportes.py
  │     └── datos.py
  └── datos.py
```

`datos.py` no depende de ningún otro archivo — es la base del sistema.

## Documentacion del Proyecto 
