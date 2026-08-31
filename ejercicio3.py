# Dado un numero N, calcula la suma de todos los numeros pares desde 1 hasta N.

numero = int(input("Ingresa un numero: "))
suma = 0
i = 1
while i <= numero:
    if i % 2 == 0:
        suma = suma + i
    i += 1

print(f"La suma de los numeros pares del 1 hasta {numero} es: ", suma)