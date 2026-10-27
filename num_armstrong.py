def es_armstrong(numero):
    if not isinstance(numero, int) or numero < 0:
        return False
    
    if numero == 0:
        return True
    
    temp = numero
    digitos = 0
    while temp > 0:
        digitos += 1
        temp //= 10
        
    temp = numero
    suma = 0
    while temp > 0:
        digito = temp % 10
        
        potencia = 1
        contador = 0
        while contador < digitos:
            potencia *= digito
            contador += 1
        
        suma += potencia
        temp //=10
    
    return suma == numero

numero = int(input("Ingresa un numero: "))
if es_armstrong(numero):
    print(f"El numero {numero} es un numero Armstrong")
else:
    print(f"El numero {numero} no es un numero Armstrong")
    
        