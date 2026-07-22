#crea la app de flask, dice donde estan los templates y statics, configura la clave de sesión,
#cuelga todas las rutas definidas en route.py, y prende el servidor en el puerto 5000 con modo debug activado.

from flask import Flask
from route import route 

def main():
    app = Flask(__name__,template_folder='templates',static_folder='static')

    app.config['SECRET_KEY'] = 'aspiradora' #clave para firmar las cookies de sesion

    route(app)
    app.run('0.0.0.0', 5000, debug=True) 
main()
