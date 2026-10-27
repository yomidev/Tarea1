from .libro import Libro

class LibroDigital(Libro):
    
    FORMATOS_VALIDOS = ["PDF", "EPUB", "MOBI"]
    
    def __init__(self, titulo, year, autor, paginas, formato, size_mb):
        if formato not in LibroDigital.FORMATOS_VALIDOS:
            raise ValueError("Formato de Libro invalido")
        if not isinstance(size_mb, (int, float)) or size_mb <= 0:
            raise ValueError("El tamaño debe ser mayor a 0")
        
        super().__init__(titulo, year, autor, paginas)
        self._formato = formato
        self._size_mb = float(size_mb)
        
    @property 
    def formato(self):
        return self._formato
    
    @formato.setter
    def formato(self, valor):
        if valor not in LibroDigital.FORMATOS_VALIDOS:
            raise ValueError("Formato de Libro invalido")
        self._formato = valor
    
    @property
    def size_mb(self):
        return self._size_mb
    
    @size_mb.setter
    def size_mb(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("El tamaño debe ser mayor a 0") 
        self._size_mb = float(valor)
        
    def mostrar_info(self):
        base = super().mostrar_info()
        return f"{base} | Formato: {self._formato} | Tamaño: {self._size_mb}"
    
    def pesa_mucho(self):
        return self._size_mb > 50