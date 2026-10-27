class Producto:
    
    IVA = 0.16
    descuento_global = 0.0
    
    def __init__(self, nombre, precio, stock=0, **atributos_extra):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no debe de estar vacio")
        
        self._nombre = nombre.strip()
        self._precio = precio
        self._stock = stock
        self._atributos_extra = atributos_extra #direccionario
        
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("El precio debe de ser un numero")
        if valor <= 0:
            raise ValueError("El precio debe de ser mayor que 0")
        
        self._precio = float(valor)
        
    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self, valor):
        if not isinstance(valor, int):
            raise TypeError("El stock debe de ser un valor numerico")
        if valor < 0:
            raise ValueError("El stock debe de ser >= 0")
        self._stock = int(valor)
       
    @property
    def precio_iva(self):
        return round(self._precio * (1 + Producto.IVA), 2) 
    
    @property
    def precio_final(self):
        descuento = self._precio * Producto.descuento_global
        return round((self._precio - descuento) * (1+Producto.IVA), 2)
    
    @property
    def disponible(self):
        return self._stock > 0
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise TypeError("El nombre debe ser una cadena de texto")
        self._nombre = valor
        
    @property
    def categoria(self):
        return getattr(self, "_categoria", "Sin categoria")
    
    @categoria.setter
    def categoria(self, valor):
        self._categoria = valor
        
    @categoria.deleter
    def categoria(self):
        print("Eliminando categoria de '{self._nombre}'")
        del self._categoria
        
    #--- Metodos de instancia
    def agregar_stock(self, cantidad, motivo="compra"):
        if cantidad <= 0:
            raise ValueError("La cantidad debe de ser positiva.")
        self._stock += cantidad
        print(f" + {cantidad} unidades ({motivo})")        
    
    def registrar_movimiento(self, tipo, **detalles):
        print(f"Movimiento: {tipo}")
        for clave, valor in detalles.items():
            print(f"- {clave} : {valor}")
    
    def aplicar_descuento(self, *productos, porcentaje = 0, **condiciones):
        if porcentaje <= 0 or porcentaje > 90:
            raise ValueError("El porcentaje de descuento debe de ser entre 1 y 90")
        minimo = condiciones.get("minimo", 0)
        if self._precio < minimo:
            print(f"{self.nombre} no supera el valor minimo (${minimo}) para aplicar el descuento.")
            return self._precio
        
        nuevo = round(self._precio*(1-porcentaje/100), 2)
        self._precio = nuevo
        print(f"{self.nombre} ahora cuesta ${nuevo} (-{porcentaje}%)")
        
        for p in productos:
            p.aplicar_descuento(porcentaje = porcentaje, **condiciones)
        
        return nuevo
    
    @classmethod
    def cambiar_descuento_global(cls, porcentaje):
        if porcentaje < 0 or porcentaje > 50:
            raise ValueError("El descuento global debe de estar entre 0 y 50")
        cls.descuento_global = porcentaje / 100
        print(f"Descuento global actualizado: {porcentaje}%")
    
    @staticmethod
    def es_precio_valido(valor):
        return isinstance(valor, (int, float)) and valor > 0
    
    def __str__(self):
        return (f"{self._nombre} ${self._precio} Stock:{self._stock} IVA: ${self.precio_iva}")
    
    
    
    