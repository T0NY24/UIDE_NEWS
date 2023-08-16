class Collection:
    
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    def get_name(self):
        return self.nombre
    
    def get_document(self):
        return self.documento
    
class Sesion:
    def __init__(self, activa):
        self.activa = activa
        self.iniciar = False
    
    def iniciar_sesion(self):
        if self.activa:
            self.iniciar = True
    
    def cerrar_sesion(self):
        self.iniciar = False
        self.activa = False
        print("La sesión ha sido cerrada.")