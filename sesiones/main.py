import gc #Garbage collector
from modelos import Sesion

def pedir_texto(mensaje, obligatorio=True):
    while True:
        valor = input(mensaje).strip()
        if obligatorio and not valor:
            print("El campo no puede estar vacio")
            continue
        return valor
    
def pedir_int(mensaje, minimo=1):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < minimo:
                print("El numero ingresado debe de ser >= 1")
                continue
            return valor
        except ValueError:
            print("Debes de ingresar un numero entero")
            
def accion_crear_sesion(sesiones):
    print("===== CRESAR SESION ====")
    usuario = pedir_texto("Usuario: ")
    if not Sesion.es_usuario_valido(usuario):
        print("El usuario debe de ser una cadena de texto y tener minimo 3 carateres")
        return
    print("Roles disponibles: Invitado, Usuario, Admin")
    rol = pedir_texto("Rol: ").capitalize()
    try:
        s = Sesion(usuario, rol)
        sesiones.append(s)
        print(f"Sesion creada: {s.describir()}")
    except (ValueError, TypeError) as e:
        print(f"Error al crear la sesion: {e}")
        
def accion_cerrar_sesion(sesiones):
    activas = [s for s in sesiones if s.activa] #0
    if not activas:
        print("No hay sesiones activas")
        return
    
    print("Sesiones Activas")
    for i, s in enumerate(activas, 1):
        print(f"{i}. {s.describir()}")
    
    idx = pedir_int("Numero a cerrar: ") - 1
    if 0 <= idx <= len(activas):
        activas[idx].cerrar()
    else:
        print("Indice invalido.")
        
def accion_eliminar_referencia(sesiones):
    if not sesiones:
        print("No hay sesiones")
        return
    
    print("Sesiones en Memoria")
    for i, s in enumerate(sesiones, 1):
        print(f"{i}. {s.describir()}")
        
    idx = pedir_int("Numero de sesion a eliminar de la lista: ") - 1
    if 0 <= idx <= len(sesiones):
        eliminada = sesiones.pop(idx)
        print("Se elimino la referencia")
    else:
        print("Indice Invalido")
        
def accion_forzar_gc():
    gc.collect()
    print("gc.collect ejecutando. Los objetos sin referencia serian eliminados")
    
def accion_registrar_accion(sesiones):
    activas = [s for s in sesiones if s.activa] #0
    if not activas:
        print("No hay sesiones activas")
        return
    
    print("Sesiones Activas")
    for i, s in enumerate(activas, 1):
        print(f"{i}. {s.describir()}")
        
    idx = pedir_int("Numero de sesion: ") - 1
    if not (0 <= idx <= len(activas)):
        print("Indice Invalido")
        return
    
    accion = pedir_texto("Accion a registrar: (ej, ver perfil, cambiar contraseña, etc)")
    try:
        total = activas[idx].registrar_accion(accion)
        print(f"Accion registrada, Total:{total}")
    except (ValueError, TypeError) as e:
        print("Error", e)
        
def menu():
    sesiones = []
    while True:
        print("\n" + "="*55)
        print("SISTEMA DE SESIONES")
        print("\n" + "="*55)
        print("1. Crear sesion")
        print("2. Registrar acciones")
        print("3. Cerrar sesion")
        print("4. Eliminar referencia")
        print("5. Forzar la recoleccion de basura")
        print("6. Sesiones en memoria")
        print("7. Salir")
        
        op = pedir_int("Opcion (1-7):")
        if op > 7:
            print("Opcion Invalida")
            continue
        try:
            if op == 1:
                accion_crear_sesion(sesiones)
            elif op ==2:
                accion_registrar_accion(sesiones)
            elif op == 3:
                accion_cerrar_sesion(sesiones)
            elif op == 4:
                accion_eliminar_referencia(sesiones)
            elif op == 5:
                accion_forzar_gc()
            elif op == 6:
                if not sesiones:
                    print("No hay sesiones activas")
                for s in sesiones:
                    print(f"{s.describir()}")
            elif op == 7:
                print("Saliendo")
                break
        except KeyboardInterrupt:
            print("Interrupcion detectada")
            break
        except Exception as e:
            print("Error inesperado", e)

try:
    menu()
except Exception as e:
    print("Error fatal", e)