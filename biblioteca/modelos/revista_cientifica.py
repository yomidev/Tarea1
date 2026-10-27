from .revista import Revista

class RevistaCientifica(Revista):
    
    def __init__(self, titulo, year, editorial, numero_edicion, area, factor_impacto):
        if not isinstance(area, str) or not area.strip():
            raise ValueError("El area no puede estar vacia")
        if not isinstance(factor_impacto, str) or not factor_impacto.strip():
            raise ValueError("El factor de impacto no puede estar vacio")
        super().__init__(titulo, year, editorial, numero_edicion)
        self._area = area.strip()
        self._factor_impacto = factor_impacto.strip()
        
    @property
    def area(self):
        return self._area
    
    @area.setter
    def area(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El area no puede estar vacia")
        self._area = valor.strip()
        
    @property
    def factor_impacto(self):
        return self._factor_impacto
    
    @factor_impacto.setter
    def factor_impacto(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El factor de impacto no puede estar vacio")
        self._factor_impacto = valor.strip()
        
    def mostrar_info(self):
        base = super().mostrar_info()
        return f"{base} | Area: {self._area} | Factor de impacto: {self._factor_impacto}"