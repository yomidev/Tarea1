"""
 * Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
 * de un lugar ficticio al pasar un número concreto de días según estas reglas:
 * - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
 * - Cada día que pasa:
 *   - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
 *   - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día
 *     siguiente aumenta en un 20%.
 *   - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día
 *     siguiente disminuya en un 20%.
 *   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
 * - La función recibe el número de días de la predicción y muestra la temperatura
 *   y si llueve durante todos esos días.
 * - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
 */
"""
import random

def simular_clima(dias, temp_inicial, prob_lluvia):
    if dias <= 0:
        print("El numero de dias debe ser mayor a 0")
        return
    
    temp = temp_inicial
    probabilidad_lluvia = prob_lluvia
    
    probabilidad_lluvia = max(0, min(100, probabilidad_lluvia))
    
    temp_max = temp
    temp_min = temp
    dias_lluvia = 0
    
    print(f"Simulacion para {dias}")
    print(f"Temperatura inicial: {temp}")
    print(f"Probabilidad de lluvia: {probabilidad_lluvia}")
    
    for dia in range(1, dias+1):
        llueve = random.randint(1,100) <= probabilidad_lluvia
        if llueve:
            print(f"Dia {dia}: Temp = {temp}, Lluvia = Si ({probabilidad_lluvia})")
            dias_lluvia = dias_lluvia + 1
        else: 
            print(f"Dia {dia}: Temp = {temp}, Lluvia = No({probabilidad_lluvia})")
        
        if temp > temp_max:
            temp_max = temp
        if temp > temp_min:
            temp_min = temp
            
        
    
    