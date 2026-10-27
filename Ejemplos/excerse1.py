def promedio(cal1, cal2, cal3):
    suma = cal1+cal2+cal3
    return suma/3


calificacion1 = float(input("Ingresa una calificación: "))
calificacion2 = float(input("Ingresa una calificación: "))
calificacion3 = float(input("Ingresa una calificación: "))

calificacion_final = promedio(calificacion1, calificacion2, calificacion3)
if calificacion_final >= 70:
    print("Aprobado. Tu promedio es: ", calificacion_final)
else:
    print(f"Reprobado. Tu promedio es: {calificacion_final}")