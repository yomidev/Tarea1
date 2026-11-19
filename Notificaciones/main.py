from notificacion import Notificacion
from email import Email
from sms import SMS
from push import PushNotification


def main():
    print("=" * 60)
    print("   📬 SISTEMA DE NOTIFICACIONES")
    print("=" * 60)

    # ============ 1. Crear instancias ============
    print("\n--- 1. Crear una instancia de cada subclase ---")
    email = Email(
        destinatario="ana.lopez",
        mensaje="Tu pedido fue enviado",
        asunto="Pedido enviado",
        cuerpo="Tu pedido llegará el viernes.",
        dominio="gmail.com",
    )
    sms = SMS(
        destinatario="Carlos Ruiz",
        mensaje="Tu código de verificación es 1234",
        numero_telefono="5512345678",
        operadora="Telcel",
    )
    push = PushNotification(
        destinatario="Luis Pérez",
        mensaje="¡Tienes una nueva oferta!",
        dispositivo="Android",
        token="abc123def456ghi789",
    )

    # ============ 2. Lista polimórfica ============
    notificaciones = [email, sms, push]
    print(f" {len(notificaciones)} notificaciones creadas")

    # ============ 3. Recorrer y usar ============
    print("\n--- 2. Recorrido polimórfico ---")
    for n in notificaciones:
        print(f"\n  {n.resumen()}")
        resultado = n.enviar()
        print(f"  Envío → {resultado}")
        print(f"  Costo: ${n.costo():.2f}")

    # ============ 4. Intentar instanciar la abstracta ============
    print("\n--- 3. Intentar instanciar Notificacion (debe fallar) ---")
    try:
        Notificacion("Ana", "Hola")
    except TypeError as e:
        print(f"Error esperado: {e}")

    # ============ 5. Subclase incompleta ============
    print("\n--- 4. Subclase incompleta sin enviar() (debe fallar) ---")
    class WhatsApp(Notificacion):
        def costo(self):
            return 0.05
        # falta implementar enviar 

    try:
        WhatsApp("Ana", "Hola")
    except TypeError as e:
        print(f"Error esperado: {e}")

    # ============ 6. MRO ============
    print("\n--- 5. MRO de cada subclase ---")
    for clase in [Email, SMS, PushNotification]:
        print(f"  {clase.__name__}: {[c.__name__ for c in clase.__mro__]}")




main()