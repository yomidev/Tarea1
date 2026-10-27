"""
 * Crea un función que reciba un texto y retorne la vocal que
 * más veces se repita.
 * - Ten cuidado con algunos casos especiales.
 * - Si no hay vocales podrá devolver vacío.
 */
"""

def vocal_mas_repetida(texto):
    contadorA = 0
    contadorE = 0
    contadorI = 0
    contadorO = 0
    contadorU = 0
    
    for caracter in texto:
        caracter = caracter.lower()
        
        if caracter == 'a':
            contadorA += 1
        elif caracter == 'e':
            contadorE += 1
        elif caracter == 'i':
            contadorI += 1
        elif caracter == 'o':
            contadorO += 1
        elif caracter == 'u':
            contadorU += 1
    
    max_contador = 0
    vocal_ganadora = ""
    
    if contadorA > max_contador:
        max_contador = contadorA
        vocal_ganadora = 'a'
    if contadorE > max_contador:
        max_contador = contadorE
        vocal_ganadora = 'e'
    if contadorI > max_contador:
        max_contador = contadorI
        vocal_ganadora = 'i'
    if contadorO > max_contador:
        max_contador = contadorO
        vocal_ganadora = 'o'
    if contadorU > max_contador:
        max_contador = contadorU
        vocal_ganadora = 'u'
        
    if max_contador == 0:
        return ""
    else:
        return vocal_ganadora

print(vocal_mas_repetida("Hola mundo"))
print(vocal_mas_repetida("AEIOU"))
print(vocal_mas_repetida("bcgdft"))
print(vocal_mas_repetida("Tres tristes tigres"))
print(vocal_mas_repetida("Murcielago"))



