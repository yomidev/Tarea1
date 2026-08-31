"""
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def invertir_cadena(texto):
    
    if not isinstance(texto, str):
        return "Error: Lo ingresado no es un texto"
    
    invertida = ""
    
    for i in range(len(texto)-1, -1, -1):
        invertida += texto[i]
    
    return invertida

palabra = input("Ingresa un texto: ")
print("Texto invertido: ", invertir_cadena(palabra))


    