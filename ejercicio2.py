# Dado un numero entero positivo N que el usuario va a ingresar, imprime todos los numeros desde 1 hasta N en una sola linea separados por espacio

# while True: 
    #numero = int(input("Ingresa un numero: "))
    #if numero > 0:
        #break
    #else:
        #print("Ingresa un numero positivo. Por favor")
numero = int(input("Ingresa un numero: "))
while (numero <= 0):
    print("El numero debe de ser positivo.")       
    numero = int(input("Ingresa un numero: "))



for i in range(1, numero+1):
    print(i, end=" ")