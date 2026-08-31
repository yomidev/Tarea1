"""
 * Crea una función que transforme grados Celsius en Fahrenheit
 * y viceversa.
 *
 * - Para que un dato de entrada sea correcto debe poseer un símbolo "°"
 *   y su unidad ("C" o "F").
 * - En caso contrario retornará un error.
"""

def convertir_temperatura(dato):
    dato.strip() #Limpar espacios vacios
    
    if len(dato) < 2:
        return "Error. Formato de tempatura invalido."
    
    unidad = dato[-1].upper()
    valor_str = dato[:-1]
    
    if unidad not in ("C", "F"):
        return f"Error: unidad {unidad} no es valida. Por favor use C o F"
    
    if unidad == "C":
        resultado = float(valor_str) * 9/5 + 32
        return f"{resultado}F"
    else: 
        resultado = (float(valor_str) - 32) * 5/9
        return f"{resultado}C"
    
temperatura = input("Ingresa la temperatura actual (C o F): ")

print(convertir_temperatura(temperatura))
    