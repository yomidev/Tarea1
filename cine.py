class Asiento:
    def __init__(self, fila, columna):
        self.fila = fila
        self.numero = columna
        self.ocupado = False
        
    def simbolo(self):
        return "X" if self.ocupado else "0"
    
class Sala:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.asientos = [
            [Asiento(f,c) for c in range(columnas)]
            for f in range(filas)
        ]
    
    def reservar(self, f, c):
        if not (0 <= f < self.filas and 0 <= c < self.columnas):
            print(f"Error: El asiento [{f}][{c}] esta fuera de rango")
            return False
        a = self.asientos[f][c]
        if a.ocupado:
            print(f"El asiento Fila: {f} y Columna: {c} no esta disponible")
            return False
        a.ocupado = True
        print(f"Asiento Reservado: Fila -> {f}, Columna -> {c}")
        return True
    
    def cancelar(self, f, c):
        if not (0 <= f < self.filas and 0 <= c < self.columnas):
            print(f"Error: El asiento [{f}][{c}] esta fuera de rango")
            return False
        a = self.asientos[f][c]
        if not a.ocupado:
            print(f"El asiento Fila: {f}, Columna: {c} no esta disponible para cancelar")
            return False
        a.ocupado = False
        print(f"Se cancelo a reservación del asiento: Fila -> {f}, Columna -> {c}")
        return True
    
    def disponibles(self):
        total = 0
        for fila in self.asientos:
            for a in fila: 
                if not a.ocupado:
                    total += 1
        return total
    
    def mostrar(self):
        print("SALA DE CINE")
        print(" "+" ".join([str(c) for c in range(self.columnas)]))
        for f, fila in enumerate(self.asientos):
            fila_str = " ".join(a.simbolo() for a in fila)
            print(f"F{f}: {fila_str}")
        print()

print("SISTEMA DE SALAS DE CINE")

sala = Sala(7,6)

sala.reservar(0, 1)
sala.reservar(0, 1)
sala.reservar(5, 1)
sala.reservar(2, 3)

sala.mostrar()
print(f"Asientos Disponibles: {sala.disponibles()}")

sala.cancelar(0,1)
sala.mostrar()
    
        
        