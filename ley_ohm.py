"""
/*
 * Crea una función que calcule el valor del parámetro perdido
 * correspondiente a la ley de Ohm.
 * - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará
 *   el valor del tercero 
 */
"""

def ley_ohm(calcular, **medidas):
    if calcular not in ['V', 'I', 'R']:
        return "Error al calcular. Los valores no coinciden"
    
    V = medidas.get('V')
    R = medidas.get('R')
    I = medidas.get('I')
    
    if calcular == 'V' and 'V' in medidas:
        return "Error: No se requiere el voltaje para calcularse asi mismo"
    if calcular == 'I' and 'I' in medidas:
        return "Error: No se requiere el intensidad para calcularse asi mismo"
    if calcular == 'R' and 'R' in medidas:
        return "Error: No se requiere el resistencia para calcularse asi mismo"
    
    if calcular == 'V':
        necesarios = [('R', R), ("I", I)]
    elif calcular == 'I':
        necesarios = [('R', R), ("V", V)]
    else:
        necesarios = [('V', V), ("I", I)]
    
    for nombre, valor in necesarios:
        if valor is None:
            return f"Error. Falta el parametro '{nombre}'"
        if not isinstance(valor, (int, float)):
            return f"Error: '{nombre}' es un tipo de dato invalido"
        
    if calcular == 'V':
        if R == 0:
            return "Error. La resistencia no puede ser cero."
        resultado = I * R
        return f"El voltaje es {resultado}"
    elif calcular == 'I':
        if R == 0:
            return "Error. La resistencia no puede ser cero."
        resultado =  V / R
        return f"La intensidad es {resultado}"
    else: 
        if I == 0:
            return "Error. La Intensidad no puede ser cero."
        resultado =  V / I
        return f"La resistencia es {resultado}"

print("Calculadora de la Ley de Ohm")

opcion = input("Que quieres calcular: (voltaje, resistencia, intensidad)").strip().lower()

if opcion == 'voltaje':
    calcular = 'V'
    I = float(input("Ingresa el valor de la intensidad: "))
    R = float(input("Ingresa el valor de la resistencia"))
    resultado = ley_ohm(calcular, R=R, I=I)
    print(resultado)
elif opcion == 'resistencia':
    calcular = 'R'
    V = float(input("Ingresa el valor del voltaje: "))
    I = float(input("Ingresa el valor de la intensidad"))
    resultado = ley_ohm(calcular, V=V, I=I)
    print(resultado)
elif opcion == 'intensidad':
    calcular = 'I'
    V = float(input("Ingresa el valor del voltaje: "))
    R = float(input("Ingresa el valor de la resistencia"))
    resultado = ley_ohm(calcular, V=V, R=R, X="hola")
    print(resultado)
else:
    print("La opcion no es valida")
    exit()
    


            

