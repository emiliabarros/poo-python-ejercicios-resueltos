# Programación Orientada a Objetos en Python

> **Unidad de Aprendizaje — Clases, Objetos y los Pilares de la POO**

---

## Objetivos de Aprendizaje

Al completar esta unidad el estudiante será capaz de:

- Definir y utilizar clases y objetos en Python con sintaxis correcta.
- Aplicar encapsulamiento mediante atributos protegidos y el decorador `@property`.
- Implementar herencia simple y múltiple usando `super()` y el MRO.
- Distinguir y aplicar abstracción mediante clases abstractas (`ABC`).
- Reconocer y programar relaciones entre objetos: asociación, agregación y composición.
- Implementar métodos dunder (`__str__`, `__eq__`, `__add__`, etc.).
- Leer e implementar código a partir de diagramas UML.
- Aplicar patrones de diseño básicos: Singleton y Observer.

---

## Conceptos Abordados

| Concepto | Archivos relacionados |
|---|---|
| Clases, objetos, `__init__`, `self` | `ejemplo_01`, `ejemplo_02` |
| Encapsulamiento, `@property` | `ejemplo_02`, `resuelto_01` |
| Herencia, `super()`, sobreescritura | `ejemplo_03`, `resuelto_03`, `resuelto_06` |
| Clases abstractas, `ABC`, `@abstractmethod` | `ejemplo_04`, `resuelto_03`, `resuelto_06` |
| Composición y agregación | `ejemplo_05` |
| Métodos dunder (`__str__`, `__eq__`, `__add__`…) | `resuelto_01`, `resuelto_02` |
| Operadores con `__add__`, `__mul__`, etc. | `resuelto_02` |
| Patrones de diseño: Singleton | `resuelto_04` |
| Patrones de diseño: Observer | `resuelto_05` |
| UML → código Python | `resuelto_06` |

---

## Estructura del Proyecto

```
poo-python-ejercicios-resueltos/
│
├── README.md
│
├── ejemplo_01_clase_persona.py            ← Primera clase básica
├── ejemplo_02_encapsulamiento_property.py ← @property con validación
├── ejemplo_03_herencia_vehiculo.py        ← Herencia y polimorfismo
├── ejemplo_04_clase_abstracta_pagos.py    ← ABC y sistema de pagos
├── ejemplo_05_composicion_agregacion.py   ← Composición vs. agregación
│
├── resuelto_01_circulo_validacion.py      ← Círculo con @property y dunder
├── resuelto_02_fraccion_operadores.py     ← Fracciones matemáticas
├── resuelto_03_jerarquia_animal_abc.py    ← Jerarquía con ABC
├── resuelto_04_patron_singleton.py        ← Patrón Singleton
├── resuelto_05_patron_observer.py         ← Patrón Observer
├── resuelto_06_uml_a_codigo_empleados.py  ← UML → código
│
└── Proyecto_Integrador_POO/               ← Sistema de gestión de biblioteca (con tests)
```

---

## Proyecto Integrador

La carpeta [`Proyecto_Integrador_POO`](Proyecto_Integrador_POO/) reúne todos los conceptos en un sistema de gestión de biblioteca: clases abstractas, herencia y polimorfismo, composición y agregación, separación en capas (`models`, `services`, `utils`) y **35 tests unitarios** con `unittest`.

```bash
cd Proyecto_Integrador_POO
python main.py                                  # demo
python -m unittest tests/test_biblioteca.py -v  # tests
```

---

## Cómo Ejecutar cada Ejemplo desde Visual Studio Code

### Opción 1 — Terminal integrada (recomendada)

1. Abrir la carpeta del proyecto en VS Code: **Archivo → Abrir carpeta**.
2. Abrir la terminal integrada: `Ctrl + `` ` (acento grave) o **Terminal → Nueva terminal**.
3. Ejecutar cualquier archivo con:

```bash
python ejemplo_01_clase_persona.py
python resuelto_02_fraccion_operadores.py
# etc.
```

### Opción 2 — Botón ▶ Run (Play)

1. Abrir el archivo `.py` deseado.
2. Hacer clic en el botón **▶** (esquina superior derecha).
3. Requiere tener instalada la extensión **Python** de Microsoft.

### Opción 3 — Atajo de teclado

Con el archivo abierto y el cursor dentro:

- **Windows/Linux:** `Ctrl + F5`
- **Mac:** `Cmd + F5`

> **Requisito:** Python 3.9 o superior instalado y seleccionado como intérprete en VS Code (esquina inferior izquierda).

---

## Resultados Esperados

### `ejemplo_01_clase_persona.py`
```
Hola, soy Ana y tengo 25 años.
Hola, soy Pedro y tengo 30 años.
Feliz cumpleaños Ana! Ahora tenés 26 años.
ana.edad  = 26
pedro.edad = 30
Persona('Ana', 26 años)
```

### `ejemplo_02_encapsulamiento_property.py`
```
25
26
Hola, soy Ana y tengo 26 años.
--- Probando validación ---
Error capturado: La edad no puede ser negativa. Recibí: -5
Edad después del intento inválido: 26
```

### `ejemplo_03_herencia_vehiculo.py`
```
Toyota Corolla (2022)
Honda CBR (2023)
Auto de 4 puertas
Moto deportiva
Toyota: 60 km/h
Toyota: 40 km/h
Toyota: maletero abierto
Honda: ¡Caballito!
isinstance(auto, Auto):     True
isinstance(auto, Vehiculo): True
isinstance(moto, Auto):     False
--- Polimorfismo: mismo código, distintas respuestas ---
  Toyota: Auto de 4 puertas
  Honda: Moto deportiva
```

### `ejemplo_04_clase_abstracta_pagos.py`
```
Error esperado: Can't instantiate abstract class Pago ...
--- Procesando pagos ---
  Cobrado $500.00 en efectivo
  Cobrado $1200.00 a tarjeta terminada en 1234
  Transferencia de $3000.00 a CBU ****8901
```

### `ejemplo_05_composicion_agregacion.py`
```
--- Pedidos individuales ---
Pedido #1 (Ana):
  Milanesa x1 = $1200.00
  Gaseosa x2 = $600.00
  TOTAL: $1800.00
...
--- Cuenta de la mesa ---
Mesa 5 — 2 pedido(s) — Total: $3500.00
--- Después de borrar la mesa ---
p1 (Ana) sigue vivo: Ana
p2 (Carlos) sigue vivo: Carlos
```

### `resuelto_01_circulo_validacion.py`
```
Círculo(radio=5) → área=78.5398, perímetro=31.4159
Círculo(radio=3.5) → área=38.4845, perímetro=21.9911
c1 == Circulo(5): True
c1 == c2:         False
```

### `resuelto_02_fraccion_operadores.py`
```
a + b = 5/6
a - b = 1/6
a * b = 1/6
a / b = 3/2
a == Fraccion(2, 4): True
```

### `resuelto_03_jerarquia_animal_abc.py`
```
Perro [Rex] | 25.0 kg | omnívoro | dice: ¡Guau! | raza: Labrador
Gato [Michi] | 4.0 kg | carnívoro | dice: ¡Miau!
Aguila [Libertad] | 6.0 kg | carnívoro | dice: ¡Kree! | envergadura: 2.2 m
```

### `resuelto_04_patron_singleton.py`
```
cfg1 is cfg2: True
cfg2 is cfg3: True
cfg2.debug:    True
cfg3.app_name: MiApp v2
```

### `resuelto_05_patron_observer.py`
```
[Sala de servidores] 20.0°C → 22.0°C  OK
[Sala de servidores] 22.0°C → 28.0°C  OK
[Sala de servidores] 28.0°C → 31.0°C  ⚠️  umbral (30.0°C) superado!
  🔴 ALERTA:  Sala de servidores — 31.0°C
  📄 LOG:     Sala de servidores — temperatura crítica: 31.0°C
  📧 EMAIL:   Alerta enviada — sensor 'Sala de servidores' a 31.0°C
```

### `resuelto_06_uml_a_codigo_empleados.py`
```
=== LIQUIDACIÓN MENSUAL ===

Tipo       | Nombre          |          Salario |           Bono
--------------------------------------------------------------------
  Vendedor   | Ana López       | Salario: $50,000 | Bono: $10,000
  Vendedor   | Luis García     | Salario: $50,000 | Bono:  $4,000
  ...
```

---

## Referencias y Material Complementario

- [Documentación oficial de Python — Classes](https://docs.python.org/3/tutorial/classes.html)
- [PEP 8 — Guía de estilo para Python](https://peps.python.org/pep-0008/)
- [módulo `abc` — Abstract Base Classes](https://docs.python.org/3/library/abc.html)
- [Typing — Type Hints](https://docs.python.org/3/library/typing.html)
