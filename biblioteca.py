from datetime import datetime, timedelta
class Libro:
    """Clase que representa un libro en la bibloteca"""
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True
        
    def prestar(self):
        """Marca el libro como prestado si esta disponible"""
        if self.disponible:
            self.disponible = False
            print(f"{self.titulo} ha sido prestado.")
        else:
            print(f"{self.titulo} no esta disponible para prestar")
            
    def devolver(self):
        """Marca el libro como disponible (devuelto)"""
        self.disponible = True
        print(f"{self.titulo} ha sido devuelto")
        
    def mostrar_info(self):
        """Muestra la información del libro"""
        #estado = "Disponible" if self.disponible else "Prestado"
        if self.disponible:
            estado = "Disponible"
        else: 
            estado = "Prestado"
        print(f"{self.titulo} | Autor: {self.autor} | ISBN: {self.isbn} | {estado}")

class Estudiante:
    """Clase que representa un estudiante que pide prestado en la biblioteca"""
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula
        self.libros_prestados = []
    
    def pedir_prestado(self, libro):
        """Pedir prestado un libro, lo añade a la lista de libros prestados y lo marca como no disponible"""
        if libro.disponible:
            libro.prestar()
            self.libros_prestados.append(libro)
            print(f"{self.nombre} ha tomado prestado {libro.titulo}")
        else:
            print(f"{self.nombre} no puede tomar {libro.titulo} porque no esta disponible")
            
    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro)
            print(f"{self.nombre} ha devuelto {libro.titulo}")
        else:
            print(f"{self.nombre} no tiene {libro.titulo} en prestamo")
    
    def mostrar_prestamos(self):
        """Mostrar los libros que el estudiante tiene actualmente en prestamo"""
        if self.libros_prestados:
            print(f"{self.nombre} tiene prestados: ")
            for libro in self.libros_prestados:
                print(f" - {libro.titulo} - {libro.autor}")
        else:
            print(f"{self.nombre} no tiene libros prestados")
            
    
class Bibliotecario:
    """Clase que representa un bibliotecario encargado de gestionar los prestamos"""
    def __init__(self, nombre, numero_empleado):
        self.nombre = nombre
        self.numero_empleado = numero_empleado
        self.prestamos_realizados = []
    
    def registrar_prestamo(self, libro, estudiante, dias_prestamo=7):
        """Registra un nuevo prestamo"""
        if not libro.disponible:
            print(f"El libro {libro.titulo} no se encuentra disponible para prestamo")
            return
        
        fecha_prestamo = datetime.now()
        fecha_devolucion = fecha_prestamo + timedelta(days=dias_prestamo)
        prestamo = Prestamo(libro, estudiante, fecha_prestamo, fecha_devolucion)
        libro.prestar()
        estudiante.libros_prestados.append(libro)
        print(f"Prestamo registrado: {estudiante.nombre} -> {libro.titulo}")
        self.prestamos_realizados.append(prestamo)
        
    def registrar_devolucion(self, libro, estudiante):
        """Registra la devolucion de un libro"""
        prestamo_encontrado = None
        for p in self.prestamos_realizados:
            if p.libro == libro and p.estudiante == estudiante and not p.devuelto:
                prestamo_encontrado = p
                break
        
        if prestamo_encontrado:
            libro.devolver()
            estudiante.devolver_libro(libro)
            prestamo_encontrado.devuelto = True
            print(f"Devolucion registrada")
        else:
            print(f"No se encontro ningun prestamo") 
    
    def mostrar_prestamos(self):
        """Mostrar los prestamos resgitrados"""
        activos = [p for p in self.prestamos_realizados if not p.devuelto]
        if activos:
            print(f"Prestamos activos:")
            for p in activos:
                print(f" - {p.libro.titulo} -> {p.estudiante.nombre} -> dev: {p.fecha_devolucion.strftime('%d/%m/%Y')}")
        else:
            print("No hay prestamos activos")

class Prestamo: 
    """Clase que representa un prestamo de un libro a un estudiante"""
    def __init__(self, libro, estudiante, fecha_prestamo, fecha_devolucion):
        self.libro = libro
        self.estudiante = estudiante
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.devuelto = False
        
    def esta_vencido(self):
        return datetime.now() > self.fecha_devolucion and not self.devuelto
    
    def calcular_dias_restantes(self):
        if self.devuelto:
            return 0
        diferencia = (self.fecha_devolucion - datetime.now()).days
        return diferencia









        
# libro1 = Libro("Python for dummies", "Empresa Fantasma", "1234567890ACV")
# libro1.mostrar_info()
# print("-----------------------")
# libro1.prestar()
# print("-----------------------")
# libro1.prestar()
# print("-----------------------")
# libro1.mostrar_info()
# print("-----------------------")
# libro1.devolver()
# print("-----------------------")
# libro1.mostrar_info()
