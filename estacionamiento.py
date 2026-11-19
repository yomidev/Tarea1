class Vehiculo:
    def __init__(self, placa):
        self.placa = placa
        
    def __str__(self):
        return f"{self.placa}"
    
class Estacionamiento:
    def __init__(self, pisos, cajones):
        self.pisos = pisos
        self.cajones = cajones
        self.lugares = [[None] * cajones for _ in range(pisos)]
    
    def estacionar(self, vehiculo):
        for p in range(self.pisos):
            for c in range(self.cajones):
                if self.lugares[p][c] is None:
                    self.lugares[p][c] = vehiculo
                    return (p, c)
        return None
    
    def buscar(self, placa):
        for p in range(self.pisos):
            for c in range(self.cajones):
                v = self.lugares[p][c]
                if v is not None and v.placa == placa:
                    return (p, c)
        return None
    
    def retirar(self, placa):
        posicion = self.buscar(placa)
        if posicion is not None:
            p, c = posicion
            self.lugares[p][c] = None
            print(f"Vehiculo {placa} retirado")
            return True
        print("Vehiculo no encontrado")
        return False
    
    def ocupados_por_pisos(self):
        conteo = []
        for fila in self.lugares:
            ocupados = sum(1 for v in fila if v is not None)
            conteo.append(ocupados)
        return conteo
    
    def lugares_libres(self):
        total_libres = 0
        for fila in self.lugares:
            total_libres += sum(1 for v in fila if v is None)
        return total_libres
    
    def mostrar(self):
        print("ESTADO DEL ESTACIONAMIENTO")
        for p, fila in enumerate(self.lugares):
            cajones_str = []
            for v in fila:
                if v is None:
                    cajones_str.append("[Libre]")
                else:
                    cajones_str.append(f"[{v.placa}]")
            print(f"Piso {p}: " + " " .join(cajones_str))
        print() 
        
e = Estacionamiento(2, 3)
for placa in ["AAAA1", "BBBB2", "CCCC3", "DDDD4"]:
    pos = e.estacionar(Vehiculo(placa))
    print(f"Estacionado {placa} en: {pos}")

e.mostrar()

print(f"Buscar CCCC3: {e.buscar('CCCC3')}")
print(f"Buscar ZZZZZ4: {e.buscar('ZZZZZ4')}")

print(f"Retirar AAAA1: {e.retirar("AAAA1")}")
print(f"Buscar ZZZZZ9: {e.retirar('ZZZZZ9')}")

e.mostrar()

print(f"Ocupados por piso: {e.ocupados_por_pisos()}")
print(f"Lugares libres: {e.lugares_libres()}")

pos_nuevo = e.estacionar(Vehiculo("WWWW5"))
print(f"Estacionado WWWW5 en: {pos_nuevo}")

e.mostrar()

