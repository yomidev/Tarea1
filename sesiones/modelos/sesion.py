import datetime

class Sesion:
    total_sesiones = 0
    sesiones_activas = 0
    
    def __init__(self, usuario, rol="Invitado"):
        if not usuario or not usuario.strip():
            raise ValueError("El nombre de usuario no puede estar vacio")
        if rol not in("Invitado", "Usuario", "Admin"):
            raise ValueError("Rol invalido")
        
        Sesion.total_sesiones += 1 #Atributo clase
        Sesion.sesiones_activas += 1
        
        self.usuario = usuario.strip() #Atributo de instancia
        self._rol = rol
        self._activa = True
        self._fecha_inicio = datetime.datetime.now()
        self._acciones = []
        self._id_sesion = Sesion.total_sesiones
        
        print(f"Sesion # {self._id_sesion} iniciada existosamente")
        
    def __del__(self):
        usuario = getattr(self, "usuario", "?")
        id_s = getattr(self, "_id_sesion", "?")
        if getattr(self, "_activa", False):
            Sesion.sesiones_activas -= 1
        print(f"Sesion # {id_s} eliminada")
        
    @property
    def rol(self):
        return self._rol
    
    @property
    def activa(self):
        return self._activa
    
    @property 
    def id_sesion(self):
        return self._id_sesion
    
    @property
    def duracion(self):
        segundos = (datetime.datetime.now() - self._fecha_inicio).total_seconds()
        return round(segundos, 2)
    
    def registrar_accion(self, accion):
        if not self._activa:
            raise RuntimeError("La sesion ya esta eliminada")
        if not accion or not accion.strip():
            raise ValueError("La accion no debe de estar vacia")
        self._acciones.append(accion.strip())
        return len(self._acciones)
    
    def cerrar(self):
        if not self._activa:
            return False
        self._activa = False
        Sesion.sesiones_activas -= 1
        print(f"Sesion #{self._id_sesion} cerrada manualmente")
        return True
    
    def describir(self):
        estado = "ACTIVA" if self._activa else "CERRADA"
        return(f"Sesion: #{self._id_sesion} | {self.usuario} | {self._rol} | {estado} | Acciones: {len(self._acciones)} | Duracion: {self.duracion}")
    
    @classmethod
    def sessiones_activas(cls):
        return cls.sesiones_activas
    
    @classmethod
    def crear_admin(cls, usuario):
        return cls(usuario, rol="Admin")
    
    @staticmethod
    def es_usuario_valido(usuario):
        return isinstance(usuario, str) and len(usuario.strip()) >= 3