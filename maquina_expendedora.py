import datetime
import random

#Clase Producto
class Producto:
    def __init__(self, codigo, nombre, precio, stock=0):
        self._codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.__stock = stock
        
    def __validar_cantidad(self, cantidad):
        return isinstance(cantidad, int) and cantidad > 0 #True o False
    
    def hay_stock(self):
        return self.__stock > 0
    
    def reducir_stock(self):
        if not self.hay_stock():
            return False
        self.__stock -= 1
        return True
    
    def reabastecer(self, cantidad):
        if not self.__validar_cantidad(cantidad):
            return "La cantidad ingresada no es correcta"
        self.__stock += cantidad
        return f"{self.nombre} reabastecido. Nuevo stock: {self.__stock}"
    
    def info(self):
        estado = "Disponible" if self.hay_stock() else "AGOTADO"
        return f"[{self._codigo} {self.nombre:<12} ${self.precio:<5} -> {estado}]"
    
class MaquinaExpendedora:
    total_maquinas = 0
    total_ventas = 0
    
    def __init__(self, modelo,pin_admin):
        self._modelo = modelo
        self.__dinero = 0
        self.__pin_admin = str(pin_admin)
        self.productos = []
        
        MaquinaExpendedora.total_maquinas += 1
        
    def __validar_pin(self, pin):
        return str(pin) == self.__pin_admin

    def __buscar_producto(self, codigo):
        for p in self.productos:
            if p._codigo.upper() == codigo.upper():
                return p
        return None
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
        
    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos")
            return
        for p in self.productos:
            print(p.info())
            
    def comprar(self, codigo, dinero):
        producto = self.__buscar_producto(codigo)
        if producto is None:
            return "Codigo no encontrado"
        if not producto.hay_stock():
            return f"{producto.nombre} esta agotado"
        if dinero < producto.precio:
            return f"Dinero insuficiente. Necesitas {producto.precio}"
        
        producto.reducir_stock()
        self.__dinero += producto.precio
        MaquinaExpendedora.total_ventas += 1
        
        cambio = dinero - producto.precio
        fecha = datetime.date.today()
        return f"Compraste: {producto.nombre}, Tu cambio es {cambio}. Venta efectuada: {fecha}"
    
    def reabastecer(self, codigo, cantidad, pin):
        if not self.__validar_pin(pin):
            return "Pin incorrecto"
        producto = self.__buscar_producto(codigo)
        if producto is None:
            return "Codigo no encontrado"
        return producto.reabastecer(cantidad)
    
    def ver_dinero(self, pin):
        if not self.__validar_pin(pin):
            return "Pin Incorrecto"
        return f"Dinero acumulado: {self.__dinero:.2f}"

def buscar_producto(maquina, codigo):
    for p in maquina.productos:
        if p._codigo.upper() == codigo.upper():
            return p
    return None

def menu_usuario(maquina):
    maquina.mostrar_productos()
    print()
    codigo = input("Codigo del producto: ").strip()
    try:
        dinero = float(input("Cuanto dinero insertas?: "))
    except ValueError:
        print("Debes ingresar un numero")
        return
    print(maquina.comprar(codigo, dinero))
    
def menu_admin(maquina):
    pin = input("PIN del Admin: ").strip()
    print("1. Reabastecer producto")
    print("2. Ver Dinero")
    opcion = input("Opcion").strip()
    if opcion == "1":
        codigo = input("Codigo del producto: ").strip()
        try:
            cantidad = int(input("Cantidad a reabastecer: "))
        except ValueError:
            print("Debe de ingresar un numero entero")
            return
        print(maquina.reabastecer(codigo, cantidad, pin))
        
    elif opcion == "2":
        print(maquina.ver_dinero(pin))
    else: 
        print("Opcion no valida")
        
def menu(maquina):
    while True:
        print("\n" + "="*45)
        print("MAQUINA EXPENDEDORA")
        print("\n" + "="*45)
        print("1. Ver productos")
        print("2. Comprar productos")
        print("3. Modo Admin")
        print("4. Ver estadisticas")
        print("5. Salir")
        
        opcion = input("Ingresa una opcion: ")
        if opcion == "1":
            maquina.mostrar_productos()
        elif opcion == "2":
            menu_usuario(maquina)
        elif opcion == "3":
            menu_admin(maquina)
        elif opcion == "4":
            print(f"Maquinas creadas: {MaquinaExpendedora.total_maquinas}")
            print(f"Total de ventas: {MaquinaExpendedora.total_ventas}")
        elif opcion == "5":
            print("Saliendo")
            break
        else:
            print("Opcion no valida")
            
maquina = MaquinaExpendedora("MOD0001", "1234")
producto = Producto("A1", "Papas", 15, stock=3)
producto1 = Producto("A2", "Refresco", 20, stock=2)
producto2 = Producto("B1", "Chocolate", 12, stock=1)
producto3 = Producto("B2", "Galletas", 10, stock=0)
producto4 = Producto("C1", "Agua", 8, stock=5)


maquina.agregar_producto(producto)
maquina.agregar_producto(producto1)
maquina.agregar_producto(producto2)
maquina.agregar_producto(producto3)
maquina.agregar_producto(producto4)

menu(maquina)
