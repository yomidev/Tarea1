from abc import ABC, abstractmethod
import datetime


# ============================================================
# CLASE ABSTRACTA
# ============================================================
class MetodoPago(ABC):
    def __init__(self, titular):
        if not isinstance(titular, str) or not titular.strip():
            raise ValueError("El titular no puede estar vacío.")
        self._titular = titular.strip()

    @property
    def titular(self):
        return self._titular

    @abstractmethod
    def procesar(self, monto):
        """
        Procesa un pago por el monto indicado.
        Cada método de pago lo implementa a su manera.
        """
        ...

    def describir(self):
        """
        Descripción genérica, válida para todos los métodos de pago.
        Usa self.tipo (property calculada) y self._titular (heredado).
        """
        return (f"[{self.tipo}] Titular: {self._titular} "
                f"| Estado: {self.estado()}")

    @property
    def tipo(self):
        """Devuelve el nombre de la clase real (Tarjeta o Transferencia)."""
        return type(self).__name__

    def estado(self):
        """Estado base. Cada subclase puede sobrescribirlo si quiere."""
        return "listo para procesar"
    
class Criptomoneda(MetodoPago):
    REDES_SOPORTADAS = {
        "BTC" :{"Nombre": "Bitcoin", "Comision": 0.01, "min_wallet": 26, "max_wallet": 62}, 
        "ETH" :{"Nombre": "Eterium", "Comision": 0.01, "min_wallet": 42, "max_wallet": 42}, 
        "USDT" :{"Nombre": "Tether", "Comision": 0.01, "min_wallet": 34, "max_wallet": 34}, 
        
    }
    MONTO_MAXIMO_USD: 5000
    
    def __init__(self, titular, wallet, red, tipo_de_cambio):
        if red not in Criptomoneda.REDES_SOPORTADAS:
            raise ValueError(
                f"Red: {red} no soportada. Use una de:"
                f"{list(Criptomoneda.REDES_SOPORTADAS.keys())}"
            )
        self.__validar_wallet(wallet, red)
        if not isinstance(tipo_de_cambio, (int, float)) or tipo_de_cambio <= 0:
            raise ValueError("El tipo de cambio debe ser mayor a 0.")
        super().__init__(titular)
        
        self._wallet = wallet
        self._red = red
        self._tipo_de_cambio = tipo_de_cambio
        
    def __validar_wallet(self, wallet, red):
        if not isinstance(wallet, str) or not wallet.strip():
            raise ValueError("La wallet no debe de estar vacia")
        
        reglas = Criptomoneda.REDES_SOPORTADAS[red]
        longitud = len(wallet)
        
        if not (reglas["min_wallet"] <= longitud <= reglas["max_wallet"]):
            raise ValueError(
                f"Wallet invalida para {red}: longitud: {longitud}"
                f"Debe de estar entre los valores {reglas['min_wallet']} y {reglas['max_wallet']}"
            )

    @property
    def wallet(self):
        return self._wallet
    
    @property
    def red (self):
        return self._red
    
    @property
    def tipo_de_cambio (self):
        return self._tipo_de_cambio
    
    @property
    def comision(self):
        return Criptomoneda.REDES_SOPORTADAS[self._red]["Comision"]
    
    def procesar(self, monto):
        if not isinstance(monto, (int, float)) or monto <= 0:
           raise ValueError("El monto debe de ser positivo")
       
        if monto > 5000:
            raise ValueError(
                f"El monto maximo para criptomonedas es 5000"
            )

        comision = monto * self.comision
        total_usd = monto + comision
        
        cantidad_cripto = round(total_usd/self.tipo_de_cambio, 8)
        return {
            "metodo": "Criptomoneda",
            "red": self._red,
            "monto_usd": monto,
            "comision_usd": round(comision, 2),
            "total_usd": round(total_usd, 2),
            "cantidad_cripto": cantidad_cripto,
            "wallet": self._wallet,
            "fecha": datetime.datetime.today().isoformat(),
            "estado":"CONFIRMADO"
        }
    
    def describir(self):
        base = super().describir()
        return (f"{base} | Red: {self._red} | wallet: {self._wallet}")
            
    


# ============================================================
# SUBCLASE 1: Tarjeta
# ============================================================
class Tarjeta(MetodoPago):
    def __init__(self, titular, numero, cvv, banco="BBVA"):
        if not (isinstance(numero, str) and numero.isdigit() and len(numero) == 16):
            raise ValueError("El número de tarjeta debe tener 16 dígitos.")
        if not (isinstance(cvv, str) and cvv.isdigit() and len(cvv) == 3):
            raise ValueError("El CVV debe tener 3 dígitos.")

        super().__init__(titular)

        self._numero = numero
        self.__cvv = cvv          # privado, no se puede leer desde fuera
        self._banco = banco
        self._comision = 0.02     # 2% de comisión

    def procesar(self, monto):
        if not isinstance(monto, (int, float)) or monto <= 0:
            raise ValueError("El monto debe ser un número positivo.")

        comision = monto * self._comision
        total = monto + comision

        return {
            "metodo": "Tarjeta",
            "monto": monto,
            "comision": round(comision, 2),
            "total_cobrado": round(total, 2),
            "tarjeta": f"**** **** **** {self._numero[-4:]}",
            "banco": self._banco,
            "fecha": datetime.date.today().isoformat(),
            "estado": "APROBADO",
        }

    def describir(self):
        base = super().describir()
        return f"{base} | Tarjeta: ****{self._numero[-4:]} ({self._banco})"

    def estado(self):
        return f"tarjeta terminada en {self._numero[-4:]}"


# ============================================================
# SUBCLASE 2: Transferencia
# ============================================================
class Transferencia(MetodoPago):
    def __init__(self, titular, banco, clabe):
        if not (isinstance(clabe, str) and clabe.isdigit() and len(clabe) == 18):
            raise ValueError("La CLABE debe tener 18 dígitos.")
        if not (isinstance(banco, str) and banco.strip()):
            raise ValueError("El banco no puede estar vacío.")

        super().__init__(titular)

        self._banco = banco.strip()
        self._clabe = clabe
        self._comision = 0.0

    # ============ SOBRESCRITURA DEL MÉTODO ABSTRACTO ============
    def procesar(self, monto):
        if not isinstance(monto, (int, float)) or monto <= 0:
            raise ValueError("El monto debe ser un número positivo.")

        comision = monto * self._comision
        total = monto + comision

        return {
            "metodo": "Transferencia",
            "monto": monto,
            "comision": round(comision, 2),
            "total_cobrado": round(total, 2),
            "banco": self._banco,
            "clabe": f"****{self._clabe[-4:]}",
            "fecha": datetime.date.today().isoformat(),
            "estado": "PENDIENTE",
        }

    def describir(self):
        base = super().describir()
        return f"{base} | CLABE: ****{self._clabe[-4:]} ({self._banco})"

    def estado(self):
        return f"transferencia desde {self._banco}"


# ============================================================
# DEMO
# ============================================================
if __name__ == "__main__":
    print("=" * 55)
    print("   SISTEMA DE MÉTODOS DE PAGO")
    print("=" * 55)

    # 1. Intentar instanciar la clase abstracta
    print("\n--- 1. Intentar instanciar MetodoPago (debe fallar) ---")
    try:
        mp = MetodoPago("Ana")
    except TypeError as e:
        print(f"❌ Error esperado: {e}")

    # 2. Crear métodos de pago concretos
    print("\n--- 2. Crear métodos de pago ---")
    tarjeta = Tarjeta("Ana López", "1234567890123456", "123", "BBVA")
    transferencia = Transferencia("Carlos Ruiz", "Santander", "012345678901234567")
    cripto = Criptomoneda(
        titular= "Luis Perez",
        wallet="bc1hdshdkr3jkfnkwj45kwjkjrmmsjal45kkjdkfsj46mnfektfgdgtddt4y67",
        red="BTC",
        tipo_de_cambio=67000.0
    )

    print(tarjeta.describir())
    print(transferencia.describir())
    print(cripto.describir())

    # 3. Procesar pagos
    print("\n--- 3. Procesar pagos ---")
    resultado1 = tarjeta.procesar(1000)
    for k, v in resultado1.items():
        print(f"   {k}: {v}")

    print()
    resultado2 = transferencia.procesar(2500)
    for k, v in resultado2.items():
        print(f"   {k}: {v}")

    # 4. Polimorfismo
    print("\n--- 4. Polimorfismo (mismo método, distintos objetos) ---")
    metodos = [tarjeta, transferencia, cripto]
    for m in metodos:
        r = m.procesar(1000)
        print(f"   {m.tipo}")
        for k, v in r.items():
            print(f"{k}:{v}")
            
    try:
        cripto.procesar(6000)
    except ValueError as e:
        print(f"{e}")

    # 5. Verificar isinstance
    print("\n--- 5. isinstance() ---")
    print(f"¿Tarjeta es MetodoPago?       {isinstance(tarjeta, MetodoPago)}")
    print(f"¿Transferencia es MetodoPago? {isinstance(transferencia, MetodoPago)}")
    print(f"¿Tarjeta es Transferencia?    {isinstance(tarjeta, Transferencia)}")

    # 6. Ver el MRO
    print("\n--- 6. MRO ---")
    print(f"Tarjeta:       {[c.__name__ for c in Tarjeta.__mro__]}")
    print(f"Transferencia: {[c.__name__ for c in Transferencia.__mro__]}")

    # 7. Errores en validaciones
    print("\n--- 7. Validaciones ---")
    try:
        Tarjeta("Luis", "123", "123")
    except ValueError as e:
        print(f"{e}")

    try:
        Transferencia("Ana", "BBVA", "123")
    except ValueError as e:
        print(f"{e}")

    try:
        tarjeta.procesar(-100)
    except ValueError as e:
        print(f"{e}")