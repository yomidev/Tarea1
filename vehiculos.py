#Definicion de clase
class Vehiculo:
    def __init__(self, color, marca, modelo, year):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.year = year
        self.velocidad = 0.0
        
    def acelerar(self, incremento):
        if incremento > 0:
            self.velocidad += incremento
            print(f"Acelerando... Velocidad actual {self.velocidad}")
        else:
            print("El vehiculo esta detenido")
    
    def frenar(self, decremento):
        if self.velocidad == 0:
            print("El vehiculo esta detenido")
            return
        
        nueva_velocidad = self.velocidad - decremento
        if nueva_velocidad < 0:
            print("El vehiculo se detuvo")
            self.velocidad = 0
        else:
            self.velocidad = nueva_velocidad
            print(f"Velocidad actual: {self.velocidad}")
        
    def mostrar_info(self):
        print("Información del vehiculo")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"Año: {self.year}")
        print(f"Velocidad actual: {self.velocidad}")

print("Crea tu vehiculo")
color1 = input("Color: ")
marca = input("Marca: ")
modelo = input("Modelo: ")
year = int(input("Año: "))

mi_auto = Vehiculo(color1, marca, modelo, year)
mi_auto.mostrar_info()

while True:
    print("\nOpciones")
    print("1. Acelerar")
    print("2. Frenar")
    print("3. Mostrar Información")
    opcion = int(input("Ingresa una opcion: "))
    
    if opcion == 1:
        valor = float(input("¿Cuantos Km/h quieres acelerar?: "))
        mi_auto.acelerar(valor)
    elif opcion == 2:
        valor = float(input("¿Cuantos km/h quieres frenar?: "))
        mi_auto.frenar(valor)
    elif opcion == 3:
        mi_auto.mostrar_info()
    elif opcion == 4:
        print("Adios")
        break
    else:
        print("opcion no valida")

