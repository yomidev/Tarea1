from .publicacion import Publicacion

class Revista(Publicacion):
    
    def __init__(self, titulo, year, editorial, numero_edicion):
        if not isinstance(editorial, str) or not editorial.strip():
            raise ValueError("La editorial no puede estar vacia")
        if not isinstance(numero_edicion, int) or numero_edicion <= 0 :
            raise ValueError("El numero de edición debe de ser superior a 0")
        super().__init__(titulo, year)
        self._editorial = editorial.strip()
        self._numero_edicion = int(numero_edicion)
        
    @property
    def editorial(self):
        return self._editorial
    
    @editorial.setter
    def editorial(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La editorial no puede estar vacia")
        self._editorial = valor.strip()
        
    @property
    def numero_edicion(self):
        return self._numero_edicion
    
    @numero_edicion.setter
    def numero_edicion(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("El numero de edicion debe de ser mayor que 0")
        self._numero_edicion = int(valor)
        
    def mostrar_info(self):
        base = super().mostrar_info()
        return f"{base} | Editorial: {self._editorial} | Numero de edicion: {self._numero_edicion}"