from .notificacion import Notificacion


class SMS(Notificacion):
    COSTO_POR_ENVIO = 0.10

    def __init__(self, destinatario, mensaje, numero_telefono, operadora):
        if not (isinstance(numero_telefono, str)
                and numero_telefono.isdigit()
                and len(numero_telefono) == 10):
            raise ValueError("El número de teléfono debe tener exactamente 10 dígitos.")
        if not isinstance(operadora, str) or not operadora.strip():
            raise ValueError("La operadora no puede estar vacía.")

        super().__init__(destinatario, mensaje)
        self._numero_telefono = numero_telefono
        self._operadora = operadora.strip()

    def enviar(self):
        return {
            "canal": "SMS",
            "numero": f"****{self._numero_telefono[-4:]}",
            "operadora": self._operadora,
            "texto": self._mensaje,
            "estado": "ENTREGADO",
        }

    def costo(self):
        return SMS.COSTO_POR_ENVIO

    def resumen(self):
        base = super().resumen()
        return f"{base} | tel: ****{self._numero_telefono[-4:]} ({self._operadora})"