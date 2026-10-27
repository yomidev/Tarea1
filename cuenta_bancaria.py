class CuentaBancaria:
    def __init__(self, titular, numero_cuenta, pin, saldo_inicial=0):
        self.titular = titular
        self._numero_cuenta = numero_cuenta
        self.__pin = pin
        self.__saldo = saldo_inicial
        
    def consultar_saldo(self):
        return f"Saldo disponible: ${self.__saldo}"

    def depositar(self, monto):
        if monto <= 0:
            return "El monto a depositar debe de ser positivo"
        self.__saldo += monto
        return f"Deposito realizado con exito. Nuevo saldo ${self.__saldo}"
    
    def retirar(self, monto):
        if monto <= 0:
            return "El monto a retirar debe de ser positivo"
        if monto > self.__saldo:
            return "Fondos insuficientes"
        self.__saldo -= monto
        return f"Retiro realizado con exito. Saldo disponible: ${self.__saldo}"
    
    def cambiar_pin(self, pin_actual,pin_nuevo):
        if pin_actual != self.__pin:
            return "PIN incorrecto. No se pudo cambiar"
        self.__pin = pin_nuevo
        return "PIN actualizado correctamente"
    
    def verificar_pin(self, pin):
        return pin == self.__pin #True o False
    
#Programa Principal
def crear_cuenta():
    print("\n==== Crear Nueva Cuenta ====\n")
    titular = input("Nombre del titular: ").strip()
    numero_cuenta = input("Numero de cuenta: ").strip()
    pin = input("PIN (4 Digitos): ").strip()
    while True:
        try:
            saldo = float(input("Saldo inicial (ingresa 0 si no tienes): "))
            if saldo < 0:
                print("El saldo inicial no puede ser negativo")
                continue
            break
        except ValueError:
            print("Error: Ingresa un numero valido")        
    return CuentaBancaria(titular, numero_cuenta, pin, saldo)
    
def menu_operaciones(cuenta):
    while True:
        print("\n==Menu de Operaciones==")
        print("1. Consultar saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Cambiar PIN")
        print("5. Salir")
        
        opcion = input("Elige una opcion (1-5): ").strip()
        
        match(opcion):
            case "1":
                pin = input("Ingresa tu pin: ")
                if cuenta.verificar_pin(pin):
                    print("Saldo: ", cuenta.consultar_saldo)
                else:
                    print("PIN Incorrecto. Intenta de nuevo")
            case "2":
                try:
                    monto = float(input("Monto a depositar: "))
                    print(cuenta.depositar(monto))
                except ValueError:
                    print("Error. Ingresa un numero valido")
            case "3":
                try:
                    monto = float(input("Monto a retirar: "))
                    print(cuenta.retirar(monto))
                except ValueError:
                    print("Error. Ingresa un numero valido")
            case "4":
                pin_actual = input("PIN actual: ")
                pin_nuevo = input("PIN nuevo: ")
                print(cuenta.cambiar_pin(pin_actual, pin_nuevo))
            case "5":
                print("Saliendo...")
                break
            case _:
                print("Opcion Invalida. Intenta de nuevo")
                
print("\n==SISTEMA BANCARIO==")
cuenta = crear_cuenta()
print(f"Cuenta creada con exito.")
menu_operaciones(cuenta)
                
    
    
    
    
    
    
    
#c = CuentaBancaria("xxxx","iskjdhsj", 1223, 90)   
#print(c._CuentaBancaria.__saldo)