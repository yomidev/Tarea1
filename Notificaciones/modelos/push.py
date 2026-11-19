from .notificacion import Notificacion


class PushNotification(Notificacion):
    COSTO_POR_ENVIO = 0.00
    DISPOSITIVOS_VALIDOS = ["Android", "iOS"]

    def __init__(self, destinatario, mensaje, dispositivo, token):
        if dispositivo not in PushNotification.DISPOSITIVOS_VALIDOS:
            raise ValueError(
                f"Dispositivo inválido: '{dispositivo}'. "
                f"Use uno de: {PushNotification.DISPOSITIVOS_VALIDOS}"
            )
        if not isinstance(token, str) or len(token) < 10:
            raise ValueError("El token debe tener al menos 10 caracteres.")

        super().__init__(destinatario, mensaje)
        self._dispositivo = dispositivo
        self._token = token

    def enviar(self):
        return {
            "canal": "PushNotification",
            "dispositivo": self._dispositivo,
            "token": f"{self._token[:6]}...{self._token[-4:]}",
            "texto": self._mensaje,
            "estado": "RECIBIDO",
        }

    def costo(self):
        return PushNotification.COSTO_POR_ENVIO

    def resumen(self):
        base = super().resumen()
        return (f"{base} | dispositivo: {self._dispositivo} "
                f"(token: {self._token[:6]}...)")