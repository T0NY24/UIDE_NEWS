import os
from datetime import date
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
import uuid

from Controlador.Controlador import (
    agregarCategoria,
    findCategorias,
    eliminarCategoria,
    actualizarCategoria,
    agregarArticulo,
    findArticulos,
)
from Util.mongoUtil import autentication, mongo_show_all

current_directory = os.path.abspath(os.path.dirname(__file__))
template_folder = os.path.join(current_directory, "..", "templates")
static_folder = os.path.join(current_directory, "..", "static")

# Definir la aplicación Flask con las rutas de plantillas y archivos estáticos
app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
app.secret_key = os.urandom(24)

login_manager = LoginManager()
login_manager.init_app(app)


class Usuario(UserMixin):
    def __init__(self, user_id):
        self.id = user_id


@app.route("/")
def index():
    # Categorizar las noticias por categoría
    news_data = mongo_show_all("Articulo")
    categorized_news = {}

    for news_item in news_data:
        category = news_item["Categoria"]
        if category not in categorized_news:
            categorized_news[category] = []
        categorized_news[category].append(news_item)

    # Obtener todas las categorías
    categorias_data = mongo_show_all("Categoria")

    # Obtener todas las noticias
    articulos_data = mongo_show_all("Articulo")

    return render_template(
        "index.html",
        categorias=categorias_data,
        articulos=articulos_data,
        articulos_categorizados=categorized_news,
    )


@app.route("/categoria", methods=["GET", "POST"])
@login_required
def categoria():
    if request.method == "POST":
        # Aquí irá el código para agregar una nueva categoría
        nombre = request.form["nombre"]
        descripcion = request.form["descripcion"]
        agregarCategoria(nombre, descripcion)
        return redirect(url_for("categoria"))
    else:
        # Si se accede a la ruta mediante GET, simplemente renderiza la plantilla de agregar categoría
        categorias = findCategorias()
        return render_template("categoria.html", categorias=categorias)


@app.route("/categoria/eliminar", methods=["GET", "POST"])
@login_required
def removeCategoria():
    id = request.form.get("id")
    eliminarCategoria(id)
    return redirect(url_for("categoria"))


@app.route("/categoria/actualizar", methods=["POST"])
@login_required
def updateCategoria():
    id = request.args.get("id")
    data = {
        "Nombre": request.form["nombre"],
        "Descripcion": request.form["descripcion"],
    }
    actualizarCategoria(id, data)
    return redirect(url_for("categoria"))


@app.route("/cv")
def cv():
    return render_template("cv.html")

@app.route("/PopularNews")
def PopularNews():
    return render_template("PopularNews.html")


@app.route("/estadisticas")
def estadisticas():
    return render_template("estadisticas.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/blog", methods=["GET", "POST"])
@login_required
def blog():
    if request.method == "POST":
        titulo = request.form["title"]
        contenido = request.form["content"]
        autor = request.form["author"]
        categoria = request.form["category"]
        imagen = request.form["imageUrl"]

        agregarArticulo(titulo, contenido, autor, categoria, imagen)
        return "Article added successfully!"
    else:
        articulos = findArticulos()
        categorias = findCategorias()
        return render_template("blog.html", categorias=categorias, articulos=articulos)


@app.route("/upload-image", methods=["POST"])
@login_required
def upload_image():
    if "image" in request.files:
        image = request.files["image"]
        rand_name = str(uuid.uuid4())
        image_url = "uploads/" + rand_name + ".jpg"
        url = "static/" + image_url
        image.save(url)
        return jsonify({"url": image_url})
    else:
        return jsonify({"error": "No image provided."})


# Función para cargar un usuario desde el ID (esto debe estar definido en tu lógica de usuarios)
@login_manager.user_loader
def load_user(user_id):
    return Usuario(user_id)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        # Verificar las credenciales utilizando la función de autenticación
        authenticated, message = autentication(email, password)

        if authenticated:
            # Si las credenciales son válidas, cargar el usuario y iniciar sesión
            user = Usuario(email)
            login_user(user)

            if email == "anthonyperez@gmail.com":
                return redirect(url_for("admin"))

            return redirect(url_for("index"))
        else:
            # Si las credenciales son incorrectas, mostrar un mensaje de error en la plantilla de inicio de sesión
            return render_template("login.html", error_message=message)
    else:
        return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("login"))


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.route("/protegido")
@login_required
def protegido():
    return "¡Esta es una página protegida! Solo puedes verla si has iniciado sesión."


if __name__ == "__main__":
    app.run(debug=True)
