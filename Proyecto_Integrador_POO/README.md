# Sistema de Gestión de Biblioteca
### Proyecto Integrador — Programación Orientada a Objetos en Python

---

## Estructura del proyecto

```
Proyecto_Integrador_POO/
│
├── main.py                          ← Punto de entrada (demo)
│
├── models/                          ← Clases de dominio (entidades)
│   ├── __init__.py
│   ├── persona.py                   ← Clase abstracta base (ABC)
│   ├── libro.py                     ← Entidad Libro con @property
│   ├── prestamo.py                  ← Composición ◆ con Libro y Socio
│   └── socio.py                     ← Socio, SocioVIP, Bibliotecario
│
├── services/                        ← Lógica de negocio
│   ├── __init__.py
│   └── biblioteca_service.py        ← Orquestador principal (Biblioteca)
│
├── utils/                           ← Utilidades y datos de ejemplo
│   ├── __init__.py
│   └── datos_demo.py                ← Datos de prueba reutilizables
│
└── tests/                           ← Pruebas unitarias
    ├── __init__.py
    └── test_biblioteca.py           ← 30+ casos de prueba con unittest
```

---

## Cómo ejecutar

### Requisitos
- Python 3.10 o superior (se usa f-strings con expresiones)
- No requiere librerías externas

### Demo completa
```bash
# Desde la carpeta Proyecto_Integrador_POO/
python main.py
```

### Tests unitarios
```bash
# Con unittest estándar
python -m unittest tests/test_biblioteca.py -v

# Con pytest (si está instalado)
pip install pytest
pytest tests/ -v
```

---

## Conceptos POO demostrados

| Archivo | Conceptos |
|---|---|
| `persona.py` | Clase abstracta, `@abstractmethod`, `@property`, `__str__`, `__repr__` |
| `libro.py` | Encapsulamiento, `@property`, `__str__`, `__eq__` |
| `prestamo.py` | Composición ◆, atributos de clase, propiedades calculadas |
| `socio.py` | Herencia simple, polimorfismo, atributo de clase sobreescrito, `__len__` |
| `biblioteca_service.py` | Agregación ◇, SRP, métodos privados, `__len__`, `__str__` |
| `main.py` | Instanciación, polimorfismo, manejo de excepciones |
| `test_biblioteca.py` | Tests unitarios, casos límite, integración |

---

## Diagrama UML simplificado

```
  «abstract»
┌──────────────────┐
│      Persona     │
├──────────────────┤
│ - __nombre: str  │
│ - __dni: str     │
├──────────────────┤
│ + presentarse()  │  ← abstracto
│ + __str__()      │
└────────┬─────────┘
         │ ▲  (herencia)
    ┌────┴────┐
    │         │
┌───┴──────┐  ┌────────────────┐
│  Socio   │  │ Bibliotecario  │
├──────────┤  ├────────────────┤
│+nro_socio│  │ + legajo       │
│+MAX_PREST│  └────────────────┘
└───┬──────┘
    │ ▲
┌───┴──────┐
│ SocioVIP │  MAX_PRESTAMOS = 7
└──────────┘

┌──────────────┐  ◇ 0..*   ┌────────────────────┐
│    Libro     │◄──────────│     Biblioteca     │
├──────────────┤           ├────────────────────┤
│ + isbn       │           │ + agregar_libro()  │
│ + titulo     │           │ + prestar_libro()  │
│ + disponible │           │ + devolver_libro() │
└──────────────┘           │ + reporte()        │
                           └────────────────────┘

┌──────────────────┐  ◆ 1   ┌──────────┐
│     Prestamo     ├───────>│  Libro   │
├──────────────────┤  ◆ 1   ├──────────┤
│ + fecha_inicio   ├───────>│  Socio   │
│ + fecha_venc     │        └──────────┘
│ + DIAS_PRESTAMO  │
│ + esta_activo    │
│ + devolver()     │
└──────────────────┘
```

---

## Extensiones sugeridas

Una vez que el sistema base funciona, podés extenderlo para demostrar dominio avanzado:

1. **Persistencia JSON** — guardar y cargar catálogo con `json.dump` / `json.load`
2. **Menú interactivo** — bucle `while` con `input()` para operar desde consola
3. **Sistema de multas** — calcular `$X` por día de retraso en la devolución
4. **Búsqueda avanzada** — buscar por autor, título parcial o año con comprensiones de lista
5. **Estadísticas** — libro más prestado, socio más activo usando `@classmethod`
6. **Tests con pytest** — ampliar la suite de tests con fixtures y parametrización
