from .notificacion import Notificacion


class Email(Notificacion):
    COSTO_POR_ENVIO = 0.01

    def __init__(self, destinatario, mensaje, asunto, cuerpo, dominio):
        if not isinstance(asunto, str) or not asunto.strip():
            raise ValueError("El asunto no puede estar vacío.")
        if not isinstance(cuerpo, str) or not cuerpo.strip():
            raise ValueError("El cuerpo no puede estar vacío.")
        if not isinstance(dominio, str) or "." not in dominio:
            raise ValueError("El dominio debe tener formato válido (ej: gmail.com).")

        super().__init__(destinatario, mensaje)
        self._asunto = asunto.strip()
        self._cuerpo = cuerpo.strip()
        self._dominio = dominio.strip()

    def enviar(self):
        return {
            "canal": "Email",
            "destinatario": f"{self._destinatario}@{self._dominio}",
            "asunto": self._asunto,
            "cuerpo": self._cuerpo,
            "estado": "ENVIADO",
        }

    def costo(self):
        return Email.COSTO_POR_ENVIO

    def resumen(self):
        base = super().resumen()
        return f"{base} | asunto: '{self._asunto}' → {self._destinatario}@{self._dominio}"