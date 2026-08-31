'''
 * Crea una función que reciba días, horas, minutos y segundos (como enteros)
 * y retorne su resultado en milisegundos.
 */
'''

def milisegundos(dias, horas, minutos, segundos):
    for nombre, valor in [("dias", dias), ("horas", horas), ("minutos", minutos), ("segundos", segundos)]:
        if not isinstance(valor, int):
            return "Error: Debes de ingresar un numero entero"
        if valor < 0:
            return "Error: no se puede ingresar el 0"
    
    milisegundos = (
        dias * 24 * 60 * 60 * 1000 +
        horas * 60 * 60 * 1000 +
        minutos * 60 * 1000 +
        segundos * 1000
    )
    
    return milisegundos

dias = int(input("Dias: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

print("La conversion a milisegundos es: ", milisegundos(dias, horas, minutos, segundos))