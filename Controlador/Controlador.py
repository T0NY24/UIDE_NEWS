from Util.mongoUtil import collection_define
from Util.mongoUtil import mongo_insert
from Util.mongoUtil import mongo_find_all
from Util.mongoUtil import mongo_show_all
from Util.mongoUtil import mongo_find_by_id
from Util.mongoUtil import mongo_update
from Util.mongoUtil import mongo_delete
from Modelo.Collections import Articulo
from Modelo.Collections import Imagenes_Multimedia
from Modelo.Collections import Categoria
from Modelo.Collections import Administradores
from Modelo.Collections import Interaccion
from datetime import datetime, timedelta


# CRUD operations for Categoria (Category) entity


def agregarCategoria(Nombre, Descripcion):
    collection_class = Categoria(Nombre, Descripcion)
    mongo_insert(collection_define(collection_class))
    print("Categoria added:", Nombre, Descripcion)


def eliminarCategoria(id):
    mongo_delete("Categoria", id)
    print("Categoria", id, "deleted successfully")


def actualizarCategoria(id, data):
    mongo_update("Categoria", id, data)
    print("Category updated successfully")


def findCategorias():
    return mongo_find_all("Categoria")


def mostrarCategorias():
    print(mongo_show_all("Categoria"))


# CRUD operations for Articulo (Article) entity


def agregarArticulo(Titulo, Contenido, Autor, Categoria, ImagenUrl):
    collection_class = Articulo(Titulo, Contenido, Autor, Categoria, ImagenUrl)
    mongo_insert(collection_define(collection_class))
    print("Articulo added:", Titulo, Contenido, Autor, Categoria, ImagenUrl)


def findArticulos():
    return mongo_find_all("Articulo")


def findArticulosByLikes():
    # Get the current date and time
    now = datetime.now()
    one_month_ago = now - timedelta(days=30)

    # Retrieve all articles that were published in the last month
    articles = mongo_find_all(
        "Articulo", {"Fecha_publicacion": {"$gte": one_month_ago}}
    )

    # Sort the articles by the number of likes in descending order
    sorted_articles = sorted(articles, key=lambda x: x["Likes"], reverse=True)

    # Return the sorted list of articles
    return sorted_articles


def actualizarArticulo(id, Titulo, Contenido, Fecha_publicacion, Autor, Categoria):
    update_data = {
        "Titulo": Titulo,
        "Contenido": Contenido,
        "Fecha_publicacion": Fecha_publicacion,
        "Autor": Autor,
        "Categoria": Categoria,
    }
    mongo_update("Articulo", id, update_data)
    print("Article updated successfully")


def eliminarArticulo(id):
    mongo_delete("Articulo", id)
    print("Article deleted successfully")


def agregarImagenes_Multimedia(Nombre, Url):
    collection_class = Imagenes_Multimedia(Nombre, Url)
    mongo_insert(collection_define(collection_class))
    print("Imagenes_Multimedia added:", Nombre, Url)


def mostrarImagenes_Multimedia():
    print(mongo_show_all("Imagenes_Multimedia"))


def agregarAdministradores(Nombre_Usuario, Correo_Electronico, Contraseña):
    collection_class = Administradores(Nombre_Usuario, Correo_Electronico, Contraseña)
    mongo_insert(collection_define(collection_class))
    print("Administradores added:", Nombre_Usuario, Correo_Electronico, Contraseña)


def mostrarAdministradores():
    print(mongo_show_all("Administradores"))


def agregarInteraccion(Tipo_Interaccion, Fecha_Interaccion, Calificacion, Comentario):
    collection_class = Interaccion(
        Tipo_Interaccion, Fecha_Interaccion, Calificacion, Comentario
    )
    mongo_insert(collection_define(collection_class))
    print(
        "Interaccion added:",
        Tipo_Interaccion,
        Fecha_Interaccion,
        Calificacion,
        Comentario,
    )


def mostrarInteracciones():
    print(mongo_show_all("Interaccion"))
