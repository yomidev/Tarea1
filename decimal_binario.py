'''
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */
'''

def decimal_a_binario(numero):
    if not isinstance(numero, int):
        return "Error: debes ingresar un numero entero"
    if numero < 0:
        return "Error: El numero debe de ser 0 o mayor que 0"
    if numero == 0:
        return "0"
    
    binario = ""
    temp = numero
    while temp > 0:
        residuo = temp % 2
        binario = str(residuo) + binario
        temp //= 2
    return binario

entrada = int(input("Ingresa un numero entero: "))

print(decimal_a_binario(entrada))