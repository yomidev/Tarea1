from .estudiante import Estudiante

class Curso:
    def __init__(self, nombre_curso):
        if not isinstance(nombre_curso, str) or not nombre_curso.strip():
            raise ValueError('El nombre del curso no puede estar vacio ')
        self._nombre_curso = nombre_curso.strip()
        self._estudiantes = []
    
    @property
    def nombre_curso(self):
        return self._nombre_curso
    
    @property
    def estudiantes(self):
        return list(self._estudiantes)
    
    @property
    def estado_curso(self):
        return "VACIO" if not self._estudiantes else "ACTIVO"
    
    def inscribir(self, estudiante):
        if not isinstance(estudiante, Estudiante):
            raise TypeError("Solo se pueden añadir estudiantes")
        if self.hay_estudiantes(estudiante.matricula):
            raise ValueError("El estudiante ya existe")
        self._estudiantes.append(estudiante)
    
    def dar_de_baja(self, matricula):
        for i, e in enumerate(self._estudiantes):
            if e.matricula == matricula:
                return self._estudiantes.pop(i)
        raise LookupError("La matricula no existe")
    
    def buscar_por_matricula(self, matricula):
        for e in self._estudiantes:
            if e.matricula == matricula:
                return e
        return None
    
    def hay_estudiantes(self, matricula):
        return self.buscar_por_matricula(matricula)
    
    def cantidad_estudiantes(self):
        return len(self._estudiantes)
    
    ##################################################
    
    def promedio_general(self):
        if not self._estudiantes:
            return 0.0
        suma = sum(e.promedio for e in self._estudiantes)
        return round(suma/len(self._estudiantes), 2)
    
    def mejor_estudiante(self):
        if not self._estudiantes:
            return None
        return max(self._estudiantes, key=lambda e: e.promedio)
    
    def peor_estudiante(self):
        if not self._estudiantes:
            return None
        return min(self._estudiantes, key=lambda e: e.promedio)
    
    def estudiantes_aprobados(self):
        return [e for e in self._estudiantes if e.es_aprobado()]
    
    def estudiantes_reprobados(self):
        return [e for e in self._estudiantes if not e.es_aprobado()]
    
    def top_n(self, n):
        if not isinstance(n, int) or n <= 0:
            raise ValueError("n debe ser un numero")
        ordenados = sorted(self._estudiantes, key=lambda e: e.promedio, reverse=True)
        return ordenados[:n]
    
    def listar(self):
        return [e.nombre for e in self._estudiantes]
    
    def __str__(self):
        return f"Curso({self._nombre_curso}, {self.cantidad_estudiantes()} estudiantes)"
    