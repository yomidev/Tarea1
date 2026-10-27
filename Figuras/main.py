from modelos import Figura,Circulo, Rectangulo, Cuadrado, Triangulo

def pedir_texto(mensaje, obligatorio=True):
    while True:
        valor = input(mensaje).strip()
        if obligatorio and not valor:
            print("Este campo no puede estar vacio")
            continue
        return valor

def pedir_float(mensaje, minimo=None):
    while True:
        valor = float(input(mensaje).strip())
        if minimo is not None and valor < minimo:
            print(f"El numero debe de ser mayor a {minimo}")
            continue
        return valor

def pedir_int(mensaje, minimo=1):
    while True:
        valor = int(input(mensaje).strip())
        if valor < minimo:
            print(f"El numero debe de ser mayor a {minimo}")
            continue
        return valor
    
def mostrar_lista(figuras):
    if not figuras:
        print("No hay figuras creadas")
        return
    print("----Figuras registradas----")
    for i, f in enumerate(figuras, 1):
        print(f"{i}, {f.describir()}")
        
def accion_crear_circulo(figuras):
    radio = pedir_float("Radio", minimo=0.01)
    try:
        c= Circulo(radio)
        figuras.append(c)
        print(f"Creado: {c.describir()}")
    except (ValueError, TypeError) as e:
        print("Error", {e})
        
def accion_crear_rectangulo(figuras):
    base = pedir_float("Base: ", minimo=0.01)
    altura = pedir_float("Altura: ", minimo=0.01)

    try:
        r= Rectangulo(base, altura)
        figuras.append(r)
        print(f"Creado: {r.describir()}")
    except (ValueError, TypeError) as e:
        print("Error", {e})
        
def accion_crear_cuadrado(figuras):
    lado = pedir_float("Lado: ", minimo=0.01)
    try:
        square= Cuadrado(lado)
        figuras.append(square)
        print(f"Creado: {square.describir()}")
    except (ValueError, TypeError) as e:
        print("Error", {e})
        
def accion_crear_triangulo(figuras):
    lado_a = pedir_float("Lado A: ", minimo=0.01)
    lado_b = pedir_float("Lado B: ", minimo=0.01)
    lado_c = pedir_float("Lado C: ", minimo=0.01)


    try:
        t= Triangulo(lado_a, lado_b, lado_c)
        figuras.append(t)
        print(f"Creado: {t.describir()}")
    except (ValueError, TypeError) as e:
        print("Error", {e})
        
def accion_ver_por_tipo(figuras):
    if not figuras:
        print("No hay figuras creadas")
        return

    tipos_disponibles = []
    for f in figuras:
        tipos_disponibles[f.tipo] = tipos_disponibles.get(f.tipo, 0)+1
    
    for tipo, cantidad, in tipos_disponibles.items():
        print(f"{tipo}: {cantidad}")
        
    tipo_buscado = pedir_texto("¿Que figura buscas?")
    filtradas = [f for f in figuras if f.tipo.lower() == tipo_buscado.lower()]
    if not filtradas:
        print("No hay figuras de este tipo")
        return
    for f in filtradas:
        print(f"{f.describir()}")
        

def menu():
    figuras = []
    
    try:
        figuras.append(Circulo(5))
        figuras.append(Rectangulo(4,6))
        figuras.append(Triangulo(3,4,5))
        figuras.append(Cuadrado(5))
    except (ValueError, TypeError) as e:
        print("Error: ", {e})
    
    while True:
        print("1. Ver figuras")
        print("2. Crear circulo")
        print("3. Crear rectangulo")
        print("4. Crear triangulo")
        print("5. Crear cuadrado")
        print("6. Ver figuras por tipo")
        print('7. Salir')
        
        op = pedir_int("Ingresa una opcion: ")
        try:
            if op == 1:
                mostrar_lista(figuras)
            elif op == 2:
                accion_crear_circulo(figuras)
            elif op == 3:
                accion_crear_rectangulo(figuras)
            elif op == 4:
                accion_crear_triangulo(figuras)
            elif op == 5:
                accion_crear_cuadrado(figuras)
            elif op == 6:
                accion_ver_por_tipo(figuras)
            elif op == 7:
                print("Salir")
                break
            else:
                print("Opcion no valida")
        except KeyboardInterrupt:
            print("accion interrumpida")
            break

menu()