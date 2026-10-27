"""
 * Crea una función que sea capaz de encriptar y desencriptar texto
 * utilizando el algoritmo de encriptación de Karaca
 */
"""

def encriptar(texto):
    texto = texto.lower()
    
    invertido = ""
    for caracter in texto:
        invertido = caracter + invertido
    
    vocales = {
        "a":"0", "e":"1", "i": "2", "o":"3", "u":"4"
    }
    
    encriptado = ""
    for caracter in invertido:
        if caracter in vocales:
            encriptado += vocales[caracter]
        else:
            encriptado += caracter

    return encriptado + "aca"

def desencriptar(texto):
    texto = texto.lower()
    
    if not texto.endswith("aca"):
        return "Error. El texto no parece que este encriptado"
    
    sin_aca = texto[:-3]
    
    numeros = {
        '0': 'a', '1':'e', '2':'i', '3':'o', '4':'u'
    }
    resultado = ""
    for caracter in sin_aca:
        if caracter in numeros:
            resultado += numeros[caracter]
        else:
            resultado += caracter
    
    desencriptado = ""
    for caracter in resultado:
            desencriptado = caracter + desencriptado
    
    return desencriptado

print("Encriptador/Desencriptado Algoritmo Karaca \n")
print("1. Encriptar")
print("2. Descriptar")
opcion = int(input("Ingresa una opcion: "))

if opcion == 1:
    texto = input("Ingresa un texto a encriptar: ")
    resultado = encriptar(texto)
    print(f"Texto encriptado: {resultado}")
elif opcion == 2:
    texto = input("Ingresa un texto a desencriptar: ")
    resultado = desencriptar(texto)
    print(f"Texto desencriptado: {resultado}")
else:
    print("Opcion no valida")

            