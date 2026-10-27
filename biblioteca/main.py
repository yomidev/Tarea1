import datetime
from modelos import (
    Publicacion,
    Libro,
    LibroDigital,
    Revista,
    RevistaCientifica
)

def pedir_texto(mensaje, obligatorio=True):
    while True:
        valor = input(mensaje).strip()
        if obligatorio and not valor:
            print("Este campo no puede estar vacio")
            continue
        return valor

def pedir_int(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje).strip())
            if minimo is not None and valor < minimo:
                print(f"Debe ser >= {minimo}")
                continue
            if maximo is not None and valor > maximo:
                print(f"Debe ser <= {maximo}")
                continue
            return valor
        except ValueError:
            print("Se debe ingresar un numero entero")
            
def pedir_float(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = float(input(mensaje).strip())
            if minimo is not None and valor < minimo:
                print(f"Debe ser >= {minimo}")
                continue
            if maximo is not None and valor > maximo:
                print(f"Debe ser <= {maximo}")
                continue
            return valor
        except ValueError:
            print("Se debe ingresar un numero entero")
            
def mostrar_lista(publicaciones):
    if not publicaciones:
        print("No hay publicaciones disponibles")
        return
    
    print("--PUBLICACIONES--")
    for i, p in enumerate(publicaciones, 1):
        print(f"{i} - {p.mostrar_info()}")
        
def buscar_por_id(publicaciones, id_buscado):
    for p in publicaciones:
        if p.id == id_buscado:
            return p
    return None
        
def agregar_libro(publicaciones):
    titulo = input("Titulo: ")
    year = int(input("Año: "))
    autor = pedir_texto("Autor: ")
    paginas = pedir_int("Paginas: ", minimo=1)
    
    try:
        libro = Libro(titulo, year, autor, paginas)
        publicaciones.append(libro)
        print(f"Libro Agregado: {libro.mostrar_info()}")
        if libro.es_libro_largo:
            print("El libro es muy largo")
    except (ValueError, TypeError) as e:
        print(f"Erro: {e}")

def agregar_libro_digital(publicaciones):
    print("\n=== AGREGAR LIBRO DIGITAL ===")
    titulo = pedir_texto("Título: ")
    year = int(input("Año: "))
    autor = pedir_texto("Autor: ")
    paginas = pedir_int("Páginas: ", minimo=1)

    print(f"Formatos válidos: {LibroDigital.FORMATOS_VALIDOS}")
    formato = pedir_texto("Formato: ").upper()
    tamano = pedir_float("Tamaño (MB): ", minimo=0.01)

    try:
        ld = LibroDigital(titulo, year, autor, paginas, formato, tamano)
        publicaciones.append(ld)
        print(f"Agregado: {ld.mostrar_info()}")
        if ld.pesa_mucho():
            print("¡Pesa más de 50 MB!")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        
def agregar_revista(publicaciones):
    print("\n=== AGREGAR REVISTA ===")
    titulo = pedir_texto("Título: ")
    year = int(input("Año:"))
    editorial = pedir_texto("Editorial: ")
    numero = pedir_int("Número de edición: ", minimo=1)

    try:
        r = Revista(titulo, year, editorial, numero)
        publicaciones.append(r)
        print(f"Agregada: {r.mostrar_info()}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


def agregar_revista_cientifica(publicaciones):
    print("\n=== AGREGAR REVISTA CIENTÍFICA ===")
    titulo = pedir_texto("Título: ")
    year = int(input("Año: "))
    editorial = pedir_texto("Editorial: ")
    numero = pedir_int("Número de edición: ", minimo=1)
    area = pedir_texto("Área (ej: Física, Biología): ")
    factor = pedir_texto("Factor de impacto (0-100): ")

    try:
        rc = RevistaCientifica(titulo, year, editorial, numero, area, factor)
        publicaciones.append(rc)
        print(f"Agregada: {rc.mostrar_info()}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


def prestar(publicaciones):
    mostrar_lista(publicaciones)
    if not publicaciones:
        return

    id_buscado = pedir_int("\nID a prestar: ", minimo=1)
    try:
        p = buscar_por_id(publicaciones, id_buscado)
        if p is None:
            raise LookupError(f"No existe la publicación con ID {id_buscado}.")
        if p.prestar():
            print(f"Prestada: {p.titulo}")
        else:
            print(f"La publicación '{p.titulo}' ya estaba prestada.")
    except LookupError as e:
        print(f"{e}")
    except (ValueError, TypeError) as e:
        print(f"{e}")


def devolver(publicaciones):
    mostrar_lista(publicaciones)
    if not publicaciones:
        return

    id_buscado = pedir_int("\nID a devolver: ", minimo=1)
    try:
        p = buscar_por_id(publicaciones, id_buscado)
        if p is None:
            raise LookupError(f"No existe la publicación con ID {id_buscado}.")
        if p.devolver():
            print(f"Devuelta: {p.titulo}")
        else:
            print(f"La publicación '{p.titulo}' ya estaba disponible.")
    except LookupError as e:
        print(f"{e}")


def ver_mro():
    print("\n=== VER MRO DE UNA CLASE ===")
    print("1. Publicacion")
    print("2. Libro")
    print("3. LibroDigital")
    print("4. Revista")
    print("5. RevistaCientifica")

    op = pedir_int("Opción: ", minimo=1)
    clases = {
        1: Publicacion,
        2: Libro,
        3: LibroDigital,
        4: Revista,
        5: RevistaCientifica,
    }
    clase = clases.get(op)
    if clase is None:
        print("Opción no válida.")
        return

    print(f"\n--- MRO de {clase.__name__} ---")
    for i, c in enumerate(clase.__mro__):
        print(f"  {i}. {c.__name__}")
        
def menu():
    publicaciones = []
    try:
        publicaciones.append(Libro("Cien Años de Soledad", 1967, "Grabiel Garcia Marquez", 471))
        publicaciones.append(LibroDigital("Python Avanzado", 2024, "A. Lopez", 450,"PDF", 20))
        publicaciones.append(Revista("UFOs", 2023, "Gobiern", 245))
        publicaciones.append(RevistaCientifica("Nature", 2024, "Springer", 12, "Ciencias", "50"))
    except (ValueError, TypeError) as e:
        print(f"Error Inesperado: {e}")

    while True:
        print("1. Ver todas las publicaciones")
        print("2. Agregar Libro")
        print("3. Agregar Libro Digital")
        print("4. Agregar Revisa")
        print("5. Agregar Revista Cientifica")
        print("6. Prestar")
        print("7. Devolver")
        print("8. Ver MRO")
        print("9. Salir")
        
        op = pedir_int("Opcion 1-9: ", minimo=1)
        if op > 10:
            print("Opcion Invalida")
            continue
        try:
            if op == 1:
                mostrar_lista(publicaciones)
            elif op == 2:
                agregar_libro(publicaciones)
            elif op == 3:
                agregar_libro_digital(publicaciones)
            elif op == 4:
                agregar_revista(publicaciones)
            elif op == 5:
                agregar_revista_cientifica(publicaciones)
            elif op == 6:
                prestar(publicaciones)
            elif op == 7:
                devolver(publicaciones)
            elif op == 8:
                ver_mro()
            elif op == 9:
                print("Saliendo")
                break
        except KeyboardInterrupt:
            print("Se interrumpio la ejecución por teclado")
            break
        except Exception as e:
            print(f"Error: {e}")
            
menu()
        


