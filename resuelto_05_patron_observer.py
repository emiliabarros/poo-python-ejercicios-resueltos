"""
Resuelto 05 — Patrón de Diseño: Observer
=========================================
Objetivo: implementar un sensor de temperatura que notifica
automáticamente a todos sus suscriptores cuando supera un umbral.

Conceptos aplicados:
- Patrón Observer (Publicador-Suscriptor).
- Callbacks almacenados como funciones en una lista.
- @property con setter que dispara notificaciones.
- Callable como tipo para funciones de callback.
- Herencia simple: SensorTemperatura hereda de Observable.

Cuándo usar Observer:
- GUI: el modelo notifica a las vistas cuando cambia.
- Eventos del sistema: un sensor notifica a múltiples manejadores.
- Sistemas de alertas y monitoreo.
"""

from typing import Callable, List, Any


# ── Clase base: Observable ───────────────────────────────────────────────────
class Observable:
    """
    Mixin que da capacidad de suscripción/notificación a cualquier clase.
    Las subclases llaman self.notificar(datos) para avisar a suscriptores.
    """

    def __init__(self) -> None:
        self._suscriptores: List[Callable[[Any], None]] = []

    def suscribir(self, fn: Callable[[Any], None]) -> None:
        """Registra una función para recibir notificaciones."""
        self._suscriptores.append(fn)

    def desuscribir(self, fn: Callable[[Any], None]) -> None:
        """Elimina una función de la lista de suscriptores."""
        self._suscriptores.remove(fn)

    def notificar(self, datos: Any) -> None:
        """Llama a todos los suscriptores con los datos del evento."""
        for fn in self._suscriptores:
            fn(datos)


# ── Sensor concreto ──────────────────────────────────────────────────────────
class SensorTemperatura(Observable):
    """
    Sensor de temperatura con umbral configurable.
    Notifica a todos los suscriptores cuando la temperatura supera el umbral.
    """

    def __init__(self, nombre: str, umbral: float) -> None:
        """
        Args:
            nombre:  Identificador del sensor.
            umbral:  Temperatura en °C que dispara las notificaciones.
        """
        super().__init__()           # inicializa la lista de suscriptores
        self.nombre  = nombre
        self.umbral  = umbral
        self._temp   = 20.0          # temperatura inicial por defecto

    @property
    def temperatura(self) -> float:
        """Devuelve la temperatura actual."""
        return self._temp

    @temperatura.setter
    def temperatura(self, nueva: float) -> None:
        """
        Actualiza la temperatura. Si supera el umbral, notifica a suscriptores.
        """
        anterior   = self._temp
        self._temp = nueva

        print(f"[{self.nombre}] {anterior:.1f}°C → {nueva:.1f}°C", end="  ")

        if nueva > self.umbral:
            print(f"⚠️  umbral ({self.umbral}°C) superado!")
            self.notificar({
                "sensor": self.nombre,
                "temp":   nueva,
                "umbral": self.umbral,
            })
        else:
            print("OK")


# ── Callbacks (funciones suscriptoras) ──────────────────────────────────────
def alerta_visual(datos: dict) -> None:
    """Muestra una alerta visible en la consola."""
    print(f"  🔴 ALERTA:  {datos['sensor']} — {datos['temp']}°C")

def log_archivo(datos: dict) -> None:
    """Simula escritura en un archivo de log."""
    print(f"  📄 LOG:     {datos['sensor']} — temperatura crítica: {datos['temp']}°C")

def notificacion_email(datos: dict) -> None:
    """Simula el envío de un email de alerta."""
    print(f"  📧 EMAIL:   Alerta enviada — sensor {datos['sensor']!r} a {datos['temp']}°C")


# ── Bloque de ejecución ─────────────────────────────────────────────────────
if __name__ == "__main__":
    sensor = SensorTemperatura("Sala de servidores", umbral=30.0)

    # Suscribimos tres observadores distintos
    sensor.suscribir(alerta_visual)
    sensor.suscribir(log_archivo)
    sensor.suscribir(notificacion_email)

    print("--- Variaciones de temperatura ---")
    sensor.temperatura = 22    # debajo del umbral → sin notificaciones
    sensor.temperatura = 28    # debajo del umbral
    sensor.temperatura = 31    # SUPERA el umbral → 3 suscriptores notificados
    sensor.temperatura = 29    # vuelve debajo
    sensor.temperatura = 35    # vuelve a superar

    print("\n--- Desuscribiendo log_archivo ---")
    sensor.desuscribir(log_archivo)
    sensor.temperatura = 40    # ahora solo alerta_visual y email

    print("\n--- Temperatura actual ---")
    print(f"Temperatura actual: {sensor.temperatura}°C")
