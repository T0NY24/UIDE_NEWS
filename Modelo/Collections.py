from datetime import datetime

class Articulo:
    def __init__(self, Titulo, Contenido, Autor, Categoria, ImagenUrl):
        self.Titulo = Titulo
        self.Contenido = Contenido
        self.Fecha_publicacion = datetime.now()
        self.Autor = Autor
        self.Categoria = Categoria
        self.ImagenUrl = ImagenUrl

    def get_document(self):
        document = {
            "Titulo": ""+self.Titulo+"",
            "Contenido": ""+self.Contenido+"",
            "Fecha_publicacion": ""+self.Fecha_publicacion.strftime('%Y-%m-%d %H:%M:%S')+"",
            "Autor": ""+self.Autor+"",
            "Categoria": ""+self.Categoria+"",
            "ImagenUrl": ""+self.ImagenUrl+"",
        }
        return document
    

class Imagenes_Multimedia:
    
    def __init__(self,Nombre,Url):
        self.Nombre=Nombre
        self.Url = Url
       
    
    def get_document(self):
        document= {
        "Nombre": ""+self.Nombre+"",
        "Url": ""+self.Url+"",
        
        }
        return document
    
class Categoria:
    
    def __init__(self,Nombre,Descripcion):
        self.Nombre = Nombre
        self.Descripcion = Descripcion
            
    def get_document(self):
        document= {
        "Nombre": ""+self.Nombre+"",
        "Descripcion": ""+self.Descripcion+""
        }
        return document

class Etiqueta:
    def __init__(self,Nombre,Descripcion):
        self.Nombre = Nombre
        self.Descripcion = Descripcion
            
    def get_document(self):
        document= {
        "Nombre": ""+self.Nombre+"",
        "Descripcion": ""+self.Descripcion+""
        }
        return document
    
class Administradores:

    def __init__(self, Nombre_Usuario, Correo_Electronico, Contraseña):
        self.Nombre_Usuario = Nombre_Usuario
        self.Correo_Electronico = Correo_Electronico
        self.Contraseña = Contraseña

    def get_document(self):
        document = {
            "Nombre_Usuario": ""+self.Nombre_Usuario+"",
            "Correo_Electronico": ""+self.Correo_Electronico+"",
            "Contraseña": ""+self.Contraseña+"",
        }
        return document

class Interaccion:
     
    def __init__(self,Tipo_Interaccion,Fecha_Interaccion,Calificacion,Comentario):
        self.Tipo_Interaccion =Tipo_Interaccion
        self.Fecha_Interaccion = Fecha_Interaccion
        self.Calificacion = Calificacion
        self.Comentario = Comentario
        
    
    def get_document(self):
        document= {
        "Tipo_Interacion": ""+self.Tipo_Interaccion+"",
        "Fecha_Interacion": ""+self.Fecha_Interaccion+"",
        "Calificacion": "["+self.Calificacion+"]",
        "Comentario": ""+self.Comentario+"",
        }
        return document

    
