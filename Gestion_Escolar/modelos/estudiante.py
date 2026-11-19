class Estudiante:
    
    CALIFICACION_MINIMA = 0.0
    CALIFICACION_MAXIMA = 10.0
    CALIFICACION_APROBATORIA = 7.0
    
    def __init__(self, nombre, matricula, calificaciones=None):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del estudiante no puede estar vacio")
        if not (isinstance(matricula, str) and matricula.isdigit() and len(matricula) == 8):
            raise ValueError("La matricula debe de contener exactamente 8 digitos")
        
        self._nombre = nombre
        self.__matricula = matricula
        self._calificaciones = []
        
        if calificaciones:
            for nota in calificaciones:
                self.agregar_calificaciones(nota)
        
    @property
    def nombre(self): #GET
        return self._nombre
        
    @nombre.setter
    def nombre(self, valor): #SET
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre del estudiante no puede estar vacio")
        self._nombre = valor.strip()
        
    @property
    def matricula(self):
        return self.__matricula
        
    @property
    def calificaciones(self):
        return list(self._calificaciones)
        
    @property
    def promedio(self):
        if not self._calificaciones:
            return 0.0
        return round(sum(self._calificaciones)/len(self._calificaciones))
        
    @property
    def estado(self):
        if not self._calificaciones:
            return 'SIN CALIFICACIONES'
        return "APROBADO" if self.promedio >= Estudiante.CALIFICACION_APROBATORIA else "REPROBADO"
        
    def agregar_calificaciones(self, nota):
        self.__validar_calificacion(nota)
        self._calificaciones.append(float(nota))
        
    def insertar_calificaciones(self, indice, nota):
        self.__validar_calificacion(nota)
        if not isinstance(indice, int) or indice < 0 or indice > len(self._calificaciones):
            raise IndexError(f"Indice invalido {indice}")
        self._calificaciones.insert(indice, float(nota))
        
    def eliminar_calificacion(self, indice):
        if not isinstance(indice, int) or indice < 0 or indice > len(self._calificaciones):
            raise IndexError(f"Indice invalido {indice}")
        return self._calificaciones.pop(indice)
        
    def eliminar_valor(self, nota):
        try:
            self._calificaciones.remove(float(nota))
        except ValueError:
            raise(f"La calificacion {nota} no existe")
        
    def buscar_calificacion(self, nota):
        try:
            return self._calificaciones.index(float(nota))
        except ValueError:
            return -1
        
    def obtener_calificacion(self, indice):
        if not isinstance(indice, int) or indice < 0 or indice > len(self._calificaciones):
            raise IndexError(f"Indice invalido {indice}")
        return self._calificaciones[indice]
        
    def cantidad_calificaciones(self):
        return len(self._calificaciones)
        
    ############################################
        
    def calificacion_maxima(self):
        if not self._calificaciones:
            return None
        return max(self._calificaciones)
        
    def calificacion_minima(self):
        if not self._calificaciones:
            return None
        return min(self._calificaciones)
        
    def calificaciones_aprobatorias(self):
        return [c for c in self._calificaciones if c>=Estudiante.CALIFICACION_APROBATORIA]
        
    def calificaciones_reprobadas(self):
        return [c for c in self._calificaciones if c < Estudiante.CALIFICACION_APROBATORIA]
        
    def ordernar_ascendente(self):
        return sorted(self._calificaciones)
        
    def ordernar_descendente(self):
        return sorted(self._calificaciones, reverse=True)
    
    def historial(self):
        return list(self._calificaciones)
        
    def es_aprobado(self):
        return self.estado == "APROBADO"
        
    #####################################################
    def __validar_calificacion(self, nota):
        if not isinstance(nota, (int, float)):
            raise ValueError("La calificacion debe de ser un numero")
        if not (Estudiante.CALIFICACION_MINIMA <= nota <= Estudiante.CALIFICACION_MAXIMA):
            raise ValueError(f"La calificacion debe de estar entre {Estudiante.CALIFICACION_MAXIMA} y {Estudiante.CALIFICACION_MINIMA}")
            
    def __str__(self):
        return (f"Estudiante: {self._nombre}, Matricula: {self.__matricula}, promedio: {self.promedio}, estado: {self.estado}")
        
    def __repr__(self):
        return self.__str__()