# Calcula el factorial de un numero n!

numero = int(input("Ingresa un numero: "))

if numero < 0:
    print ("Numero negativo. No es posible calcular el factorial")
else:
    resultado = 1
    for i in range(1,numero+1):
        resultado = resultado * i

    print(f"El factorial de {numero} es: {resultado}")
        