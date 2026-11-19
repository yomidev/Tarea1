from modelos import Estudiante, Curso

def main():
    print("1. Crear Estudiante")
    
    ana = Estudiante("Ana Lopez", "20150001", [9.0, 8.5, 10.0])
    carlos = Estudiante("Carlos Ruiz", "20150002", [5.0, 4.5, 6.0])
    luis = Estudiante("Luis Perez", "20150003", [7.5, 8.0, 6.5])
    marta = Estudiante("Marta Diaz", "20150004", [3.0, 4.0, 4.5])
    
    for e in [ana, carlos, luis, marta]:
        print(f" {e}")
        
    print("2. Probar metodos")
    
    print(f" Historial inicial: {ana.historial()}")
    ana.agregar_calificaciones(8.5)
    print(f"Historial Actualizado: {ana.historial()}")
    ana.insertar_calificaciones(0, 9.0)
    print(f"Historial Actualizado: {ana.historial()}")
    eliminada = ana.eliminar_calificacion(1)
    print(f"Lista con dato eliminado: {eliminada}: {ana.historial()}")
    ana.eliminar_valor(8.5)
    print(f"Historial Actualizado: {ana.historial()}")
    
    idx = ana.buscar_calificacion(9.0)
    print("Indice de 9.0", idx)
    
    print(f"1. Calificacion en [0]: {ana.obtener_calificacion(0)}")
    print(f"Cantidad: {ana.cantidad_calificaciones()}")
    print(f"Promedio: {ana.promedio}")
    print(f"Maxima:  {ana.calificacion_maxima()}")
    print(f"Minima: {ana.calificacion_minima()}")
    print(f"Aprobadas: {ana.calificaciones_aprobatorias()}")
    print(f"Reprobadas: {ana.calificaciones_reprobadas()}")
    print(f"Reprobadas: {ana.calificaciones_reprobadas()}")
    print(f"Ordenar ASC: {ana.ordernar_ascendente()}")
    print(f"Ordenar DESC: {ana.ordernar_descendente()}")
    print(f"Estado: {ana.estado}")
    
    
    curso = Curso("Introducción al desarrollo web")
    print(f"Estado : {curso.estado_curso}")
    
    for e in [ana, carlos, luis, marta]:
        curso.inscribir(e)
        
    print(f"Despues de inscribir: {curso}")
    print(f"Estudiantes: {curso.listar()}")
    print(f"Promedio general: {curso.promedio_general()}")
    print(f"Mejor: {curso.mejor_estudiante().nombre}")
    print(f"Peor: {curso.peor_estudiante().nombre}")
    print(f"Aprobados: {[e.nombre for e in curso.estudiantes_aprobados()]}")
    print(f"Aprobados: {[e.nombre for e in curso.estudiantes_reprobados()]}")
    
    print("Top 2: ")
    for i, e in enumerate(curso.top_n(2),1):
        print(f"{i}. {e.nombre} -> {e.promedio}")
        
    print(f"Desinscribir: {curso.dar_de_baja("20150003")}")
    print(f"Listar: {curso.listar()}")
    
    print(f"Datos del eliminado {luis.nombre}")
    


        
main()