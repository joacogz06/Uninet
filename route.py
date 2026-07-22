from flask import render_template, request, session, jsonify, Response # redirect: redirigir a otras rutas # url_for: generar URLs dinámicamente # request: gestiona las solicitudes http recibidas 
from appConfig import config                  # Archivo de configuracion de la aplicación                       
from controller import *                    

def route(app):

########################################################################################################################
##################################### UNIVERSIDAD ########################################################################
##########################################################################################################################
    @app.route("/")
    def home():
        return Traerpagina_home2()

    @app.route("/login")
    def login():
        return render_template('inicio.html')
    
    @app.route('/signin', methods =["GET", "POST"])
    def signin(): 
        error=''
        return ingresoUsuarioValido(error,request)
    
    @app.route("/paginacrearuniversidad")
    def rutacrearUniversidad():
        return Traerpagina_crearcuenta()
    
    @app.route('/crearUsuario',methods = ['POST', 'GET']) #que es?? get--> la info que esta enviando se ve en la barra de navegacion, poca info  #post --> no veo la info, mas info(ejemplo archivo)
    def crearUsuario():
        diRequest={}
        error=""
        return registrarUsuario2(diRequest,request, error)        # Devuelve el diccionario que contiene todos los datos de la solicitud y la información de la carga de archivos

    @app.route('/perfil2') 
    def perfil2():
        return render_template('perfil2.html')
    
    @app.route('/solicitud2') #esta es la ruta de las solicitudes que te llegan
    def solicitud2():
        return solicitudes()
    
    @app.route('/info_alumno', methods=["POST"]) #ruta de ajax
    def info_alumno():
        data = request.get_json()
        id = data['id']
        listas = info_del_alumno(id)
        return jsonify(listas)

    @app.route("/editar_perfil_uni")
    def editarperfil():
        ciudades= obtenerCiudades()
        return render_template("editar_perfil2.html", ciudades=ciudades)
    
    @app.route("/nuevo_perfil_uni", methods=["GET", "POST"])#volver a chequear los cambios de matilda
    def nuevo_perfil_uni():
        return editar__perfil_uni()

    @app.route('/actualizarestado', methods=['POST']) #cambiar la solicitud de un alumno a rechazado o a aceptado
    def estado_solicitud():
        data = request.get_json()
        id = data['id']
        nuevo_valor = data['nuevo_valor']
        cambiarestado_al(id, nuevo_valor)
        return '{"success":1}'
    
    @app.route('/actualizarestado_programa', methods=['POST']) #cambia de disponible a no disponible un prgrama
    def estado_programa():
        print("funciona")
        data = request.get_json()
        id = data['id']  # Extrae el ID de los datos recibidos
        nuevo_valor = data['nuevo_valor']  # Extrae el nuevo valor del enum
        cambiarestado_progra(id, nuevo_valor)
        return jsonify(True)
    
    @app.route('/pagina_agregarprograma')
    def pagina_agregarprograma():
        return render_template('agregar_programa2.html')
    
    @app.route('/nuevo_programa', methods=['POST'])
    def nuevo_programa():
        error=''
        return cargar_programa(error, request)
        
###########################################################################################################################
################# ALUMNOOOOO  ##############################################################################################
#############################################################################################################################

    @app.route("/paginacrearcuentaalumno")
    def crearalumno():
        ciudades=obtenerCiudades()
        carreras=obtenerCarrera()
        return render_template("crearcuenta.html",ciudades=ciudades,carreras=carreras)
    
    @app.route("/crearUsuarioalu", methods=["POST"])
    def crearalumnousuario():
        diRequest={}
        error=''
        return registrarUsuario1(diRequest,request, error)

    @app.route("/perfilalu")
    def perfil_alu():
        return render_template("perfil.html")
    
    @app.route("/perfileditaralu")
    def perfil_editar_alu():
        ciudades=obtenerCiudades()
        carreras=obtenerCarrera()
        return render_template("editar_perfil.html",ciudades=ciudades,carreras=carreras)
    
    @app.route("/homealu")
    def homealu():
        programas=ObtenertodosProgramas()
        return render_template("home.html",programas=programas)

    @app.route("/editar_perfil", methods=["POST"])
    def editar_perfil():
        res= editar_perfil_alu()
        return res
    
    @app.route("/info_programa",methods=["post"])
    def info_programa():
        programa=ver_mas()
        return render_template("info_programa.html",programa=programa)
    
    @app.route("/solicitud_programa",methods=["post"])
    def solicitud_programa():
        res= mandar_solicitud()
        return Response(status=204)
    
    @app.route("/enviadas")
    def enviadas():
        solicitudes=obtenerEnviadas()
        return render_template("enviadas.html",solicitudes=solicitudes)
    
    @app.route("/respuestasalu")
    def respuestas_alu():
        respuestas = Obtener_respuestas()
        if respuestas is None:
            respuestas=[]
        return render_template("respuestas.html", respuestas=respuestas)
    
    @app.route("/info_programa1",methods=["post"])
    def info_programa_respuestas():
        programas=info_programa_respuesta()
        programas=programas[0]
        print(programas)
        return render_template("info_programa_respuestas.html",programas=programas)
    
    @app.route("/borrar_solicitud",  methods=["GET", "POST"])
    def borrar_soli():
        print('llego  a la ruta.')
        data = request.get_json()
        id = data['id']  
        return Solicitud_borrar(id)
    
    @app.route("/buscar_home", methods=["GET", "POST"])
    def buscar_h():
        return buscarHome()
    
    @app.route("/buscar_enviadas", methods=["GET", "POST"])
    def buscar_e():
        return buscarEnviadas()
    
    @app.route("/buscar_respuestas", methods=["GET", "POST"])
    def buscar_r(): 
        consulta_busqueda= request.args.get('busqueda')
        respuestas=Obtener_respuestas()
        resultados_busqueda = []
        for respuesta in respuestas:
            if consulta_busqueda.lower() in respuesta[6].lower():
                resultados_busqueda.append(respuesta)
        return render_template('enviadas.html', respuestas=resultados_busqueda)
    
    @app.route("/cerrarSession")
    def cerrar():
        cerrarSesion()
        return render_template('inicio.html')