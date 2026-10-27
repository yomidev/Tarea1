import datetime

class Publicacion:
    
    total_publicaciones = 0
    
    def __init__(self, titulo, year):
        if not isinstance(titulo, str) or not titulo.strip():
            raise ValueError("El titulo no puede estar vacio")
        if not Publicacion.es_year_valido(year):
            raise ValueError("El año debe de ser un numero entero positivo")
        Publicacion.total_publicaciones += 1
        self._id = Publicacion.total_publicaciones
        self._titulo = titulo.strip()
        self._year = year
        self._disponible = True
        
        print(f"Publicacion Creada: {self._titulo}")
    
    def __del__(self):
        id_ = getattr(self, "_id", "?")
        print(f"Publicacion elminada. Liberando ID={id_}")
        
    @property
    def id(self):
        return self._id
    
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El titulo no puede estar vacio")
        self._titulo = valor.strip()
        
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, valor):
        if not Publicacion.es_year_valido(valor):
            raise ValueError("El año debe de ser un numero entero y positivo")
        self._year = int(valor)
    
    @property
    def disponible(self):
        return self._disponible
    
    def prestar(self):
        if not self._disponible:
            return False
        self._disponible = False
        return True
    
    def devolver(self):
        if self._disponible:
            return False
        self._disponible = True
        return True
    
    def mostrar_info(self):
        estado = "DISPONIBLE" if self._disponible else "PRESTADO"
        return f"ID: {self._id}, Titulo: {self._titulo}, Año: {self._year}: Estatus: {estado}"
        
    @classmethod
    def cuantas_publicaciones(cls):
        return cls.total_publicaciones
    
    @staticmethod
    def es_year_valido(year):
        if not isinstance(year, int):
            return False
        return 1500 <= year <= datetime.date.today().year