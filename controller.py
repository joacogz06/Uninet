from flask import request, session, render_template
from datetime import datetime
from model import *
from appConfig import config

#####################################################################################################################################
######################################### FUNCIONES CONJUNTAS  ###############################################################
#####################################################################################################################

def ingresoUsuarioValido(error,request): #request lo genera flask automaticamente, datos del navegador como matodo o datos del formulario
    mirequest={}
    getRequet(mirequest)
    tipo_usuario = mirequest.get("alu/uni") #busca el valor de alu/uni
    user=mirequest.get("user_mail")
    password=mirequest.get("password")
    
    if user=='' or password=='':
        error= "No se completaron todos los campos"
    elif tipo_usuario=="Universidad":
        if crearSesion(request):
            programas=obtenerProgramas(user,password)
            res=render_template('home2.html',error=error, programas=programas) #render_template arma y muestra un HTML sin cambiar la URL (una sola petición).
        else:
            error = "Error: Usuario o contraseña inválidos para Universidad."
    elif tipo_usuario=="Alumno":
        if crearSesion1(request):
            programas=ObtenertodosProgramas()
            res=render_template('home.html',error=error,programas=programas)
        else:
            error = "Error: Usuario o contraseña inválidos para Alumno."
    
    if error!='':
        res = render_template('inicio.html', error=error)  
    return res

def cerrarSesion():
    try:    
        session.clear()
    except:
        pass

def getRequet(diResult):  # Función para obtener los datos de la solicitud y almacenarlos en un diccionario
    if request.method=='POST':                   #request es global # Si el método de la solicitud es POST
        for name in request.form.to_dict().keys():  #to_dict(): lo convierte a diccionario normal de Python, keys() solo las claves, sin los valores
            li=request.form.getlist(name)           # Obtiene la lista de valores para cada clave
            if len(li)>1:                           # Si hay más de un valor
                diResult[name]=request.form.getlist(name)  # Almacena la lista de valores en el diccionario
            elif len(li)==1:                        # Si hay un solo valor
                diResult[name]=li[0]                # Almacena el valor en el diccionario
            else:                                   # Si no hay valores
                diResult[name]=""                   # Almacena una cadena vacía en el diccionario
    elif request.method=='GET':                   # Si el método de la solicitud es GET
        for name in request.args.to_dict().keys(): 
            li=request.args.getlist(name)           # Obtiene la lista de valores para cada clave
            if len(li)>1:                           # Si hay más de un valor
                diResult[name]=request.args.getlist(name)  # Almacena la lista de valores en el diccionario
            elif len(li)==1:                        # Si hay un solo valor
                diResult[name]=li[0]                # Almacena el valor en el diccionario
            else:                                   # Si no hay valores
                diResult[name]=""                   # Almacena una cadena vacía en el diccionario



#####################################################################################################################################
######################################### UNIVERSIDAD ###############################################################
#####################################################################################################################

def registrarUsuario2(dic, request, error):
    getRequet(dic)
    ciudades=obtenerCiudades()
    if crearUsuario(dic):
        res=render_template('inicio.html')
    else:
        error="No se pudo crear el usuario"
        res=render_template('crearcuenta2.html', error=error, ciudades=ciudades)
    return res

def Traerpagina_crearcuenta():
    ciudades= obtenerCiudades()
    return render_template("crearcuenta2.html", ciudades=ciudades)

def info_del_alumno(id):
    return info_alu(id)

def registro_pagina(param):
    '''info:
        Carga la pagina 'register'
    '''
    #obtenerMenuBottom(param)       
    return render_template('inicio.html',param=param)

def solicitudes():
    solicitudes = obtenerSolicitud()
    return render_template("solicitud2.html", solicitudes=solicitudes)

def Traerpagina_home2():
    programas=obtenerProgramas(session.get("email"), session.get("password"))
    return render_template('home2.html', programas=programas)

def cambiarestado_al(id, valor):
    cambiarestado_a(id, valor)

def cambiarestado_progra(id, valor):
    cambiarestado_p(id, valor)

def cargar_programa(error, request):
    mirequest={}
    getRequet(mirequest)
    if insertar_programa(mirequest):
        res= Traerpagina_home2()
    else:
        error="Error: No se ha podido crear el programa"
        res= render_template('agregar_programa2.html', error=error)
    return res
    
def editar__perfil_uni():
    diRequest = {}
    getRequet(diRequest)
    user_id = session.get("id_uni")
    res= editarperfiluni(diRequest,user_id)
    return res

############## FUNCIONES (SESSION) UNIVERSIDAD ############################################################

def crearSesion(request):
    sesionValida=False
    mirequest={}
    try: 
        #Carga los datos recibidos del form cliente en el dict 'mirequest'.          
        getRequet(mirequest)
        # CONSULTA A LA BASE DE DATOS. Si usuario es valido => crea session
        dicUsuario={}
        if obtenerUniXEmailPass(dicUsuario,mirequest.get("user_mail"),mirequest.get("password")):
            cargarSesion(dicUsuario)
            sesionValida = True
    except ValueError:  
        print("ERROR EN REALIZAR SESSION")                             
        pass
    return sesionValida

def cargarSesion(dicUsuario):
    session['id_uni'] = dicUsuario['id']
    session['nombre']  = dicUsuario['nombre']
    session['ciudad'] = dicUsuario['link']
    session['email'] = dicUsuario['email'] # es el mail
    session['password'] = dicUsuario['password']
    session['telefono'] = dicUsuario['telefono']
    session['link'] = dicUsuario['id_ciudad']
    session["time"]  = datetime.now()
    session['tipo'] = 'universidad'

##########################################################################################################################################################################


##################################################################################################################################################
################# ALUMNOOOOO  ####################################################################################################################
##############################################################################################################################################
def registrarUsuario1(dic, request, error):
    getRequet(dic)
    if crearUsuario1(dic):
        res=render_template('inicio.html')
    else:
        error="No se pudo crear el usuario"
        res=render_template('crearcuenta.html', error=error)
    return res

def editar_perfil_alu():
    di = {}
    getRequet(di)
    id_user = session.get("id_alu")
    return editarperfilalu(di,id_user)

def ver_mas():
    id_programa = request.form.get('id_programa')  # Captura el ID del programa
    sQuery="""SELECT programa.id,programa.nombre, universidad.nombre AS universidad_nombre, programa.precio, programa.requisitos, programa.modalidad, programa.descripcion 
    FROM programa
    INNER JOIN universidad ON programa.id_universidad = universidad.id
    WHERE programa.id=%s"""
    val=(id_programa)
    programa=selectDB(BASE,sQuery,val)
    programa=programa[0]
    return programa

def mandar_solicitud():
    di={}
    getRequet(di)
    solicitud_programa(di)

def Obtener_respuestas():
    id=session.get('id_alu')
    respuestas = buscar_aceptar_rechazar(id)
    return respuestas

def info_programa_respuesta():
    di={}
    getRequet(di)
    id_programa=di.get("id_programa_respuesta")
    return obtenerPrograma(id_programa)

def Solicitud_borrar(id):
    Delete_Soli(id)

def obtenerEnviadas():
    id=session.get('id_alu')
    enviadas= obtener_enviadas(id)
    ahora=datetime.now()
    enviadas_modificadas = []
    if not(enviadas is None):
        for enviada in enviadas:
            enviada_lista = list(enviada)
            fecha_envio= enviada[8]
            dias_transcurridos = (ahora - fecha_envio).days
            enviada_lista[8] = dias_transcurridos
            enviadas_modificadas.append(tuple(enviada_lista))
    return enviadas_modificadas

def buscarHome():
    diBusqueda={}
    getRequet(diBusqueda)
    consulta_busqueda= diBusqueda.get('busqueda')
    programas=ObtenertodosProgramas()
    resultados_busqueda = []
    for programa in programas:
        if consulta_busqueda.lower() in programa[1].lower():
            resultados_busqueda.append(programa)
    return render_template('home.html', programas=resultados_busqueda)

def buscarEnviadas():
    di={}
    getRequet(di)
    consulta_busqueda= di.get('busqueda')
    solicitudes=obtenerEnviadas()
    resultados_busqueda = []
    for solicitud in solicitudes:
        if consulta_busqueda.lower() in solicitud[1].lower():
            resultados_busqueda.append(solicitud)
    return render_template('enviadas.html', solicitudes=resultados_busqueda)

####################### FUNCIONES (SESION) ALUMNO ##########################################################################

def crearSesion1(request):
    sesionValida=False
    mirequest={}
    try:       
        getRequet(mirequest)
        dicUsuario={}
        if obtenerAluXEmailPass(dicUsuario,mirequest.get("user_mail"),mirequest.get("password")):
            cargarSesion1(dicUsuario)
            sesionValida = True
    except ValueError:
        print("ERROR EN REALIZAR SESSION")                             
        pass
    return sesionValida

def cargarSesion1(dicUsuario):
    session['id_alu'] = dicUsuario['id']
    session['nombre']     = dicUsuario['nombre']
    session['apellido']   = dicUsuario['apellido']
    session['email']   = dicUsuario['email'] # es el mail
    session['password']     = dicUsuario['password']
    session['dni']        = dicUsuario['dni']
    session['telefono']        = dicUsuario['telefono']
    session['promedio']        = dicUsuario['promedio']
    session['id_ciudad']        = dicUsuario['id_ciudad']
    session['id_carrera']        = dicUsuario['id_carrera']
    session['situacion']        = dicUsuario['situacion']  
    session["time"]       = datetime.now()
    session['tipo'] = 'alumno'

###################################################################################################################################