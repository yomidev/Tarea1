"""
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
"""

def area_poligono(tipo, **medidas):
    tipo.lower()
    
    if tipo not in ["triangulo", "rectangulo", "cuadrado"]:
        return f"Error: {tipo} no es un poligono valido"
    
    def validar_medidas(valor, nombre):
        if valor is None:
            return f"Error: '{nombre}' esta vacio"
        num = float(valor)
        if num <= 0:
            return f"Error. El numero debe de ser positivo"
        return num
    
    if tipo == "triangulo":
        base = medidas.get("base") or medidas.get("largo")
        altura = medidas.get("altura") or medidas.get("ancho")
        base = validar_medidas(base, "base/largo")
        altura = validar_medidas(altura, "altura/ancho")
        if isinstance(base, str):
            return base
        if isinstance(altura, str):
            return altura
        return (base*altura)/2
    
    elif tipo == "rectangulo":
        base = medidas.get("base") or medidas.get("largo")
        altura = medidas.get("altura") or medidas.get("ancho")
        base = validar_medidas(base, "base/largo")
        altura = validar_medidas(altura, "altura/ancho")
        if isinstance(base, str):
            return base
        if isinstance(altura, str):
            return altura
        return base*altura
    else: 
        lado = validar_medidas(medidas.get("lado"), "lado")
        if isinstance(lado, str):
            return lado
        return lado * lado
    
print(area_poligono("triangulo", base = 10, altura = 4))
print(area_poligono("rectangulo", base=5, altura=3))
print(area_poligono("cuadrado", lado=8))
print(area_poligono("circulo", radio=10))