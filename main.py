from Controlador.frontEndController import app
from Controlador.Controlador import agregarAdministradores, agregarArticulo

if __name__ == '__main__':
    # agregarAdministradores("Kevin", "kesuarezar@uide.edu.ec", "12345678")
    # agregarAdministradores("tony", "anthonyperez@gmail.com", "6969")

    app.run(debug=True)
    