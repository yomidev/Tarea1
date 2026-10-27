
"""/*
 * Crea una función que sea capaz de detectar si existe un viernes 13
 * en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */
 """
 
import datetime

def viernes_13(mes, year):
    fecha = datetime.date(year, mes, 13)
    
    return fecha.weekday() == 4

year = int(input("Ingresa un año: "))
mes = int(input("Ingresa un mes: "))
while mes > 12:
    mes = int(input("Ingresa un mes: "))

if viernes_13(mes, year):
    print("Existe un viernes 13 en esta fecha")
else:
    print("No hay viernes 13")
