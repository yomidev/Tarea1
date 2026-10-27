"""
    Sistema de Gestión de Biblioteca
        1. Declaracion de clases: atributos, metodos, encapsulamiento
        2. Instancia de una clase (objetos)
        3. Referencia al objeto (self)
        4. Metodos: declaran, mensajes, paso de parametros, retorno
        5. Constructor y Destructor (__init__, __del__)
        6. Sobrecarga de metodos
        7. Sobrecarga de operadores
"""
"""
    ¿Que es una clase?: Molde o plantilla que nos define como se contruyen los objetos
    ¿Por que?: Reutilizar y escribir solo una vez
"""
class Biblioteca:
    """Clase que representa una biblioteca"""
    """Nombre de las clases: Convencion PascalCase (PEP 8)"""
    """Atributos: Caracteristicas del objeto"""
    """Atributos de instancia"""
    """Metodo Constructor"""
    def __init__(self, nombre):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre de la biblioteca no puede ir vacio")
        self.nombre = nombre.strip() #Atributo publico
        self._libros = [] #Atributo protegido
        
    """Metodo Destructor"""
    def __del__(self):
        print(f"La bibliotec '{self.nombre}' esta cerrada.")
        
        
    """Metodos: Comportamientos del objetos"""
    def agregar_libro(self, titulo, autor, year, copias=1):
        """Agregar un libro a la biblioteca"""
        #Validaciones
        if not titulo or not titulo.strip():
            raise ValueError("El titulo no puede estar vacio")
        if not autor or not autor.strip():
            raise ValueError("El autor no puede estar vacio")
        if year < 0:
            raise ValueError("El año no puede ser menor que cero")
        if copias < 0:
            raise ValueError("Las copias no pueden ser menor que cero")
        
        #Buscar si ya existe
        for libro in self._libros:
            if libro["titulo"].lower() == titulo.lower():
                libro["copias"] += copias
                print(f"Copias actualizadas: '{titulo}' -> {libro['copias']}")
                return
        
        #Agregar nuevo
        self._libros.append({
            "titulo": titulo.strip(),
            "autor": autor.strip(),
            "año": int(year),
            "copias": int(copias)
        })
        
        print(f"Libro '{titulo}'agregado correctamente")
    
    def prestar_libro(self, titulo):
        for libro in self._libros:
            if libro["titulo"].lower() == titulo.lower():
                if libro["copias"] <= 0:
                    raise ValueError(f"No hay copias disponibles para prestar")
                libro["copias"] -= 1
                print(f"Libro '{titulo}' prestado. Copias disponibles: {libro["copias"]}")
                return
        raise ValueError(f"El libro '{titulo}' no se encuentra en esta biblioteca")
    
    def devolver_libro(self, titulo):
        for libro in self._libros:
            if libro["titulo"].lower() == titulo.lower():
                libro["copias"] += 1
                print(f"Libro '{titulo}' devuelto. Copias disponibles: {libro["copias"]}")
                return
        raise ValueError(f"El libro '{titulo}' no pertenece a esta biblioyeca")
    
    def mostrar_catalogo(self):
        if not self._libros:
            print("Biblioteca vacia")
            return
        print("\n" + "="*60)
        print(f"Catalogo: {self.nombre.upper()}")
        print("\n" + "="*60)
        
        for i, libro in enumerate(self._libros, 1):
            estado = "Disponible" if libro["copias"] > 0 else "Agotado"
            print(f"\n {i}. {libro["titulo"]}")
            print(f"Autor: {libro["autor"]}")
            print(f"Año: {libro["año"]}")
            print(f"Copias: {libro["copias"]} - {estado}")
        print("\n" + "="*60)
        
    def libro_mas_antiguo(self):
        if not self._libros:
            return None
        mas_antiguo = min(self._libros, key=lambda l: l["año"])
        return mas_antiguo["titulo"], mas_antiguo["año"]
    
    @property
    def total_titulos(self):
        return len(self._libros)
    
    @property
    def total_copias(self):
        return sum(libro["copias"] for libro in self._libros)
    
    @property
    def libros_agotados(self):
        return [l for l in self._libros if l["copias"] == 0]
    
    def __str__(self):
        return f"Biblioteca '{self.nombre}', ({self.total_titulos} titulos, {self.total_copias} copias)"
    
    def __repr__(self):
        return f"Biblioteca({self.nombre}', titulos={self.total_titulos})"
    
    def __len__(self):
        return len(self._libros)
    
    def __bool__(self):
        return self._libros > 0    
    
    
    def __add__(self, other):
        """Combina dos bibliotecas en una"""
        if not isinstance(other, Biblioteca):
            raise TypeError("Solo se pueden sumar bibliotecas")
        
        nueva = Biblioteca(f"{self.nombre} + {other.nombre}")
        for libro in self._libros:
            nueva._libros.append(libro.copy())
        
        for libro in other._libros:
            nueva.agregar_libro(libro["titulo"], libro["autor"], libro["año"], libro["copias"])
        
        return nueva
    
    def __eq__(self, other):
        """Dos bibliotecas tienes los mismo libros"""
        if not isinstance(other, Biblioteca):
            return False
        if len(self._libros) != len(other._libros):
            return False
        for l1 in self._libros:
            encontrado = False
            for l2 in self._libros:
                if(l1["titulo"].lower() == l2["titulo"].lower() and
                   l1["autor"].lower() == l2["autor"].lower() and
                   l1["año"] == l2["año"] and
                   l1["copias"] == l2["copias"]
                   ):
                    encontrado = True
                    break
            if not encontrado:
                return False
        return True   
    
    def __contains__(self, titulo):
        return any(
            l["titulo"].lower() == titulo.lower()
            for l in self._libros
        )   
        
    def __lt__(self, other):
        return self.total_copias < other.total_copias
    def __gt__(self, other):
        return self.total_copias > other.total_copias
    
    
    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una opcion: ")
            try:
                if opcion == "1":
                    self._opcion_agregar()
                elif opcion == "2":
                    self._opcion_prestar()
                elif opcion == "3":
                    self._opcion_devolver()
                elif opcion == "4":
                    self.mostrar_catalogo()
                elif opcion == "5":
                    self._opcion_mas_antiguo()
                elif opcion == "6":
                    self._opcion_estadisticas()
                elif opcion == "7":
                    self._opcion_agotados()
                elif opcion == "8": 
                    print("Gracias por usar el sistema")
                    break
                else:
                    print("Opcion no valida")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error: {e}")
    
    def mostrar_menu(self):
        print("\n" + "="*50)
        print(f"{self.nombre.upper()}")
        print("\n" + "="*50)
        print("1. Agregar Libro")
        print("2. Prestar Libro")
        print("3. Devolver Libro")
        print("4. Mostrar catalogo")
        print("5. Libro mas antiguo")
        print("6. Estadisticas")
        print("7. Libros agotados")
        print("8. Salir")
        print("\n" + "="*50)
        
    def _opcion_agregar(self):
        print("\n Agrega Libro")
        titulo = input("Titulo: ").strip()
        autor = input("Autor: ").strip()
        try:
            year = int(input("Año: "))
        except ValueError:
            raise ValueError("El año debe de ser un numero")
        try:
            copias = int(input("Copias (por defecto 1): ") or "1")
        except ValueError:
            raise ValueError("La copias debe de ser un numero") 
        self.agregar_libro(titulo, autor, year, copias)
    
    def _opcion_prestar(self):
        print("\n Prestar Libro")
        titulo = input("Titulo: ")
        self.prestar_libro(titulo)
        
    def _opcion_devolver(self):
            print("\n Devolver Libro")
            titulo = input("Titulo: ")
            self.devolver_libro(titulo)
            
    def _opcion_mas_antiguo(self):
        resultado = self.libro_mas_antiguo()
        if resultado is None:
            print("La biblioteca esta vacia")
        else:
            titulo, year = resultado
            print("\n Libro mas Antiguo: ")
            print(f"Titulo: {titulo}" )
            print(f"Año: {year}" )
            
    def _opcion_estadisticas(self):
        print("\n"+"="*50)
        print("Estaditicas")
        print("\n"+"="*50)
        print(f"Titulos Diferentes: {self.total_titulos}")
        print(f"total de Copias: {self.total_copias}")
        
    def _opcion_agotados(self):
        agotados = self.libros_agotados
        if not agotados:
            print("No hay libros agotados")
            return
        print("Libros Agotados")
        for libro in agotados:
            print(f"{libro['titulo']} - {libro['titulo']}")


"""Que es una instancia?: Es cuando creamos el objeto a partir de la clase"""
if __name__ == "__main__":
    print("SISTEMA DE GESTION DE BIBLIOTECA")
    biblioteca_central = Biblioteca("Biblioteca Central")
    biblioteca_central.ejecutar()

#Biblioteca.mostrar_nombre(biblioteca_central)


