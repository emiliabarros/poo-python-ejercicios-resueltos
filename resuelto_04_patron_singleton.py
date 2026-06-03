"""
Resuelto 04 — Patrón de Diseño: Singleton
==========================================
Objetivo: garantizar que solo exista UNA instancia de la clase
Configuracion en toda la ejecución del programa.

Conceptos aplicados:
- Patrón Singleton mediante __new__.
- Atributos de clase como estado compartido.
- __new__ se llama ANTES de __init__; __init__ puede re-ejecutarse.
- Guardia _inicializado para evitar reset en cada acceso.

Cuándo usar Singleton:
- Configuración global del sistema.
- Conexión única a base de datos.
- Logger compartido por toda la app.
"""


class Configuracion:
    """
    Singleton: solo puede existir UNA instancia de esta clase.

    Cualquier llamada a Configuracion() devuelve SIEMPRE el mismo objeto.
    Cambiar la configuración desde cualquier parte del código afecta
    a todos los que la usen.
    """

    _instancia    = None    # referencia a la única instancia (o None si no existe)
    _inicializado = False   # evita re-ejecutar __init__ en llamadas posteriores

    def __new__(cls) -> "Configuracion":
        """
        __new__ se llama ANTES de __init__.
        Solo creamos el objeto la primera vez; en adelante devolvemos el existente.
        """
        if cls._instancia is None:
            # Primera vez: crear el objeto real en memoria
            cls._instancia = super().__new__(cls)
        return cls._instancia    # siempre devuelve LA MISMA instancia

    def __init__(self) -> None:
        """
        Se ejecutaría en cada llamada a Configuracion(), pero la guardia
        _inicializado evita re-asignar los valores por defecto.
        """
        if not self._inicializado:
            # Solo se ejecuta una vez, la primera vez
            self.db_host  = "localhost"
            self.db_port  = 5432
            self.debug    = False
            self.app_name = "MiApp"
            Configuracion._inicializado = True

    def __str__(self) -> str:
        return (
            f"Configuracion("
            f"db={self.db_host}:{self.db_port}, "
            f"debug={self.debug}, "
            f"app={self.app_name!r})"
        )

    def __repr__(self) -> str:
        return f"<Configuracion id={id(self)}>"


# ── Bloque de ejecución ─────────────────────────────────────────────────────
if __name__ == "__main__":
    print("--- Creando instancias ---")
    cfg1 = Configuracion()
    cfg2 = Configuracion()
    cfg3 = Configuracion()

    # Las tres variables apuntan al MISMO objeto
    print(f"cfg1 is cfg2: {cfg1 is cfg2}")   # True
    print(f"cfg2 is cfg3: {cfg2 is cfg3}")   # True
    print(f"id(cfg1): {id(cfg1)}")
    print(f"id(cfg2): {id(cfg2)}")           # mismo id

    print("\n--- Estado inicial ---")
    print(cfg1)

    print("\n--- Modificando desde cfg1 ---")
    cfg1.debug    = True
    cfg1.app_name = "MiApp v2"

    # El cambio se refleja en cfg2 y cfg3 porque son el mismo objeto
    print(f"cfg2.debug:    {cfg2.debug}")       # True  ← cambió
    print(f"cfg3.app_name: {cfg3.app_name}")    # MiApp v2 ← cambió
    print(cfg2)

    print("\n--- Modificando desde cfg3 ---")
    cfg3.db_port = 3306
    print(f"cfg1.db_port: {cfg1.db_port}")     # 3306 ← cambió
