#Escribe un programa que pida un numero entero al usuario e imprima "Par" si es un numero divisible entre 2 o "Impar" en caso contrario

numero1 = int(input("Ingresa un número entero: "))
if numero1 % 2 == 0:
    print("Par")
else:
    print("Impar")