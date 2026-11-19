from abc import ABC, abstractmethod


class Notificacion(ABC):
    """
    Contrato base para todos los canales de notificación.
    Toda subclase DEBE implementar enviar() y costo().
    """

    def __init__(self, destinatario, mensaje):
        if not isinstance(destinatario, str) or not destinatario.strip():
            raise ValueError("El destinatario no puede estar vacío.")
        if not isinstance(mensaje, str) or not mensaje.strip():
            raise ValueError("El mensaje no puede estar vacío.")

        self._destinatario = destinatario.strip()
        self._mensaje = mensaje.strip()

    @property #GET
    def destinatario(self):
        return self._destinatario

    @property
    def mensaje(self):
        return self._mensaje

    @abstractmethod
    def enviar(self):
        """Envía la notificación. Cada canal lo hace a su manera."""
        ...

    @abstractmethod
    def costo(self):
        """Devuelve el costo del envío en USD."""
        ...

    def resumen(self):
        """Descripción genérica, común a todos los canales."""
        return (f"[ {self._destinatario} | "
                f"mensaje: '{self._mensaje}' | "
                f"costo: ${self.costo():.2f}")