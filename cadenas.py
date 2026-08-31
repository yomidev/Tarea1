"""
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
 */
"""

#def diferencia(str1, str2):
    #out1 = ""
    #out2 = ""
    
    #for i in range(len(str)-1, 1):
        #encontrado = False
        #for c in str2:
            #if c == caracter:
                #encontrado = True
                #break
        #if not encontrado:
            #out1 = out1+caracter
            
    #for caracter in str2:
            #encontrado = False
            #for c in str1:
                #if c == caracter:
                    #encontrado = True
                    #break
            #if not encontrado:
                #out2 = out2+caracter
    
    #print("Cadena sin carateres de str2:", out1)
    #print("Cadena sin caratecter de str1: ", out2)
def diferencia(str1, str2):
    
    set1 = set(str1)
    set2 = set(str2)
    
    out1 = set1 - set2
    out2 = set2 - set1
    
    print("Cadena sin carateres de str2:", str(out1))
    print("Cadena sin caratecter de str1: ", str(out2))


str1 = input("Ingresa una cadena de texto: ")
str2 = input("Ingresa otra cadena de texto: ")

diferencia(str1, str2)