from _mysql_db import *
from flask import session, url_for
from datetime import datetime

def obtenerCiudades():
    sQuery = "SELECT id, nombre FROM ciudad"
    return selectDB(BASE, sQuery)  # selectDB es tu función para ejecutar SELECT en la base de datos\

def obtenerCarrera():
    sQuery="SELECT id,nombre FROM carrera"
    return selectDB(BASE,sQuery)

#####################################################################################################################################
######################################### UNIVERSIDAD #################################################################################
######################################################################################################################################

def editarperfiluni(diRequest,user_id):
    val = (diRequest.get("nombreuni"),diRequest.get("ciudaduni"),diRequest.get("mailuni"),diRequest.get("telefonouni"),diRequest.get("linkuni"),user_id)

    sQuery = "UPDATE universidad SET nombre = %s, id_ciudad = %s, email = %s, telefono = %s, link = %s WHERE id=%s"
    
    ciudades=obtenerCiudades()

    if updateDB(BASE,sQuery,val): #cant de filas afectadas
        id_ciudad=diRequest.get("ciudaduni")
        ciudad_nombre=""
        for ciudad in ciudades:
            if ciudad[0]==int(id_ciudad):
                ciudad_nombre=ciudad[1]
        session['nombre'] = diRequest.get("nombreuni")
        session['ciudad'] = ciudad_nombre
        session['email'] = diRequest.get("mailuni")
        session['telefono'] = diRequest.get("telefonouni")
        session['link'] = diRequest.get("linkuni")
        res= redirect(url_for('perfil2'))
    else:
        error="Hubo un error en la actualizacion del perfil"

        res= render_template("editar_perfil2.html",error=error)
    return res

def obtenerUniXEmailPass(result, email, password):
    res = False
    sSql = """SELECT universidad.id, universidad.nombre, universidad.link, universidad.email, universidad.pass, universidad.telefono, ciudad.nombre AS nombre_ciudad 
        FROM universidad 
        INNER JOIN ciudad ON universidad.id_ciudad = ciudad.id 
        WHERE universidad.email =%s and universidad.pass=%s;
        """
    val = (email, password)
    
    try:
        fila = selectDB(BASE, sSql, val)
    
        if fila:
            res = True
            result['id'] = fila[0][0]
            result['nombre'] = fila[0][1]
            result['id_ciudad'] = fila[0][2]
            result['email'] = fila[0][3]
            result['password'] = fila[0][4]
            result['telefono'] = fila[0][5]
            result['link'] = fila[0][6]
        else:
            print("No se encontró el usuario con ese email y contraseña.")
        
    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")

    return res

def crearUsuario(di):
    sQuery=""" 
        INSERT INTO universidad
        (id, nombre, id_ciudad, email, pass, telefono, link)
        VALUES
        (%s,%s, %s, %s, %s, %s, %s);
    """
       
    val=(None,di.get('nombreuni'), di.get('id_ciudad'), di.get('mail'), di.get('password'), di.get("telefono"), di.get("link"))
    try:
        resul_insert=insertDB(BASE,sQuery,val) #insert devuelve la cantidad de filas que afecta
        if resul_insert == 1:
            res=True
        else:
            res=False
    except Exception as e:
        res=False
    return res

def obtenerProgramas(email, password):
    sSql = """
        SELECT programa.id, programa.nombre, universidad.nombre AS universidad_programa, programa.precio, programa.requisitos, programa.modalidad, programa.estado, programa.descripcion 
        FROM programa
        JOIN universidad ON programa.id_universidad = universidad.id
        WHERE universidad.email =%s AND universidad.pass =%s;
    """
    val = (email, password)
    
    try:
        filas = selectDB(BASE, sSql, val)
    
        if filas:
            res = filas
        else:
            res="No se encontranon programas correspondientes a la universidad."
        
    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")
    return res

def obtenerSolicitud():
    sQuery = """
        SELECT 
            solicitud.*, 
            universidad.nombre AS nombre_universidad,
            programa.nombre AS nombre_programa,
            alumno.nombre AS nombre_alumno,
            alumno.apellido,
            alumno.email,
            alumno.dni,
            alumno.telefono,
            alumno.promedio,
            alumno.situacion,
            ciudad.nombre AS nombre_ciudad,
            carrera.nombre AS nombre_carrera
        FROM solicitud
        JOIN alumno ON solicitud.id_alumno = alumno.id
        JOIN programa ON solicitud.id_programa = programa.id
        JOIN ciudad ON alumno.id_ciudad = ciudad.id
        JOIN carrera ON alumno.id_carrera = carrera.id
        JOIN universidad ON programa.id_universidad = universidad.id
        WHERE programa.id_universidad =%s AND solicitud.estado="solicitado";
        """
    val=session.get("id_uni")
    try:
        filas = selectDB(BASE, sQuery, val)

        if filas:
            res = filas
        else:
            res=None
        
    except Exception as e:
        print(f"Error al ejecutar la consulta de solicitudes: {e}")

    return res

def info_alu(id):
    sQuery="""
    SELECT alumno.*, 
    carrera.nombre AS carrera_nombre, 
    ciudad.nombre AS ciudad_nombre FROM alumno
    INNER JOIN carrera ON alumno.id_carrera=carrera.id
    INNER JOIN ciudad ON alumno.id_ciudad=ciudad.id
    WHERE alumno.id=%s"""
    val=(id,)
    result=selectDB(BASE,sQuery,val)
    return result 

def cambiarestado_a(id, valor):
    sQuery = """
            UPDATE solicitud
            SET estado = %s
            WHERE id = %s;
            """
    val=(valor, id)
    return updateDB(BASE, sQuery, val)

def cambiarestado_p(id, valor):
    sQuery = """
            UPDATE programa
            SET estado = %s
            WHERE id = %s;
            """
    val=(valor, id)
    return updateDB(BASE, sQuery, val)

def insertar_programa(di):
    sQuery = """
        INSERT INTO programa
        (id, nombre, id_universidad, precio, requisitos, modalidad, estado, descripcion)
        VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s);
        """
    val = (None, di.get('nombrepro'), session.get('id_uni'), di.get('precio'), di.get('requisitos'), di.get("modalidad"), 'disponible', di.get("descripcion"))
    try:
        resul_insert=insertDB(BASE,sQuery,val)
        if resul_insert == 1:
            res=True
        else:
            res=False
    except:
        res=False
    return res

####################################################################################################################
################# ALUMNOOOOO  ####################################################################################
##################################################################################################################

def crearUsuario1(di):
    sQuery="INSERT INTO alumno (id,nombre,apellido,email,pass,dni,telefono,promedio,id_ciudad,id_carrera,situacion) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    val=(None,di.get("nombrealu"),di.get("apellidoalu"),di.get("emailalu"),di.get("passalu"),di.get("dnialu"),di.get("telefonoalu"),di.get("promedioalu"),di.get("ciudadalu"),di.get("carreraalu"),di.get('situacionalu'))
    #no esta para completar lo de situacion
    #borrar columna situacion de alumno
    resul_insert=insertDB(BASE,sQuery,val)
    if resul_insert == 1:
        res=True
    else:
        res=False
    return res

def obtenerAluXEmailPass(result, email, password):
    res = False 
    sSql = """ SELECT alumno.id, alumno.nombre, alumno.apellido, alumno.email, alumno.pass, alumno.dni, alumno.telefono, 
    alumno.promedio, ciudad.nombre AS id_ciudad, carrera.nombre AS id_carrera, alumno.situacion FROM alumno 
    INNER JOIN ciudad ON alumno.id_ciudad = ciudad.id 
    INNER JOIN carrera ON alumno.id_carrera = carrera.id 
    WHERE alumno.email =%s AND alumno.pass =%s; """ 
    val = (email, password) 
    try: 
        fila = selectDB(BASE, sSql, val) 
        if fila:
            res = True 
            result['id'] = fila[0][0] 
            result['nombre'] = fila[0][1] 
            result['apellido'] = fila[0][2] 
            result['email'] = fila[0][3] 
            result['password'] = fila[0][4] 
            result['dni'] = fila[0][5] 
            result['telefono'] = fila[0][6] 
            result['promedio'] = fila[0][7] 
            result['id_ciudad'] = fila[0][8] 
            result['id_carrera'] = fila[0][9] 
            result['situacion'] = fila[0][10] 
        else: 
            print("No se encontró el usuario con ese email y contraseña.") 
    except Exception as e: 
        print(f"Error al ejecutar la consulta: {e}")
    return res

def ObtenertodosProgramas():
    sQuery = """
        SELECT programa.id, programa.nombre, universidad.nombre AS universidad_nombre, 
           programa.precio, programa.requisitos, programa.modalidad, programa.estado, programa.descripcion
        FROM programa
        INNER JOIN universidad ON programa.id_universidad = universidad.id
        LEFT JOIN solicitud ON programa.id = solicitud.id_programa AND solicitud.id_alumno = %s
        WHERE solicitud.id_programa IS NULL;
    """
    #El LEFT JOIN asegura que:Se incluyan todas las filas de programa, aunque no tengan una solicitud asociada.
    # el WHERE, Filtra los programas que no tienen una solicitud asociada para el alumno especificado 
    id_alu = session.get('id_alu')

    val=(id_alu)
    result=selectDB(BASE,sQuery,val)
    lista=[]
    for programa in result:
        if programa[6]=="disponible":
            lista.append(programa)

    return lista

def buscar_aceptar_rechazar(id):
    sQuery="""
        SELECT 
            solicitud.*, 
            universidad.nombre AS nombre_universidad,
            programa.nombre AS nombre_programa,
            alumno.nombre AS nombre_alumno
        FROM solicitud
        JOIN alumno ON solicitud.id_alumno = alumno.id
        JOIN programa ON solicitud.id_programa = programa.id
        JOIN universidad ON programa.id_universidad = universidad.id
        WHERE alumno.id = %s AND (solicitud.estado = 'aceptado' OR solicitud.estado = 'rechazado');
        """
    val = (id,) #como el id lo estoy pasando yo esto no seria necesario, pero por consumbre queda.
    try:
        filas=selectDB(BASE,sQuery,val)
        print(filas)
        res = filas
    except Exception as e:
        print(f"Error al ejecutar la consulta de respuestas: {e}")
        res=None
    return res

def solicitud_programa(di):
    sQuery="""INSERT INTO solicitud (id,id_alumno,id_programa,fechahora,estado)
    VALUES (%s,%s,%s,%s,%s)"""
    val=(None, session.get("id_alu"),di.get("idprograma"),datetime.now(),"solicitado")
    print(val)
    if insertDB(BASE,sQuery,val)==1:
        return True
    else:
        return False
    
def editarperfilalu(di,id_user):
    id_carrera = di.get("id_carrera")
    id_ciudad = di.get("id_ciudad")
    sQuery="""UPDATE alumno SET nombre=%s, apellido=%s, email=%s, pass=%s, dni=%s, telefono=%s, promedio=%s, id_carrera=%s, id_ciudad=%s WHERE id=%s"""
    val=(di.get("nombrealu"),di.get("apellidoalu"),di.get("emailalu"),di.get("password"),di.get("dnialu"),di.get("telefonoalu"),di.get("promedioalu"),id_carrera,id_ciudad,id_user)
    ciudades=obtenerCiudades()
    carreras=obtenerCarrera()
    print(ciudades)
    try:
        if updateDB(BASE,sQuery,val):
            session['id_alu'] = id_user
            session['nombre'] = di.get("nombrealu")
            session['apellido'] = di.get("apellidoalu")
            session['email'] = di.get("emailalu") # es el mail
            session['password'] = di.get("password")
            session['dni'] = di.get("dnialu")
            session['telefono'] = di.get("telefonoalu")
            session['promedio'] = di.get("promedioalu")
            ciudad_nombre=""
            for ciudad in ciudades:
                if ciudad[0]==int(id_ciudad):
                    ciudad_nombre=ciudad[1]
            for carrera in carreras:
                if carrera[0]==int(id_carrera):
                    carrera_nombre=carrera[1]
            session['id_ciudad'] = ciudad_nombre
            session['id_carrera'] = carrera_nombre
            session["time"] = datetime.now()
            return render_template("perfil.html")
        else:
            error="Error al actualizar el perfil"
            return render_template("editar_perfil.html",error=error,ciudades=ciudades, carreras=carreras)
    except Exception as e:
        error="ERROR:",e
        return render_template("editar_perfil.html",error=error,ciudades=ciudades, carreras=carreras)

def Delete_Soli(id):
    sQuery="""
        DELETE FROM solicitud WHERE id=%s
        """
    val=(id)
    print('llego al model')
    try:
        filas=deleteDB(BASE,sQuery,val)
    
        if filas:
            res = filas
        else:
            res=None
        
    except Exception as e:
        print(f"Error al eliminar la fila de solicitudes: {e}")
    return res

def obtener_enviadas(id):
    sQuery="""
    SELECT solicitud.id_alumno, programa.nombre AS programa_nombre, programa.precio, programa.modalidad, programa.descripcion,
    universidad.nombre AS universidad_nombre, ciudad.nombre, solicitud.estado, solicitud.fechahora FROM solicitud 
    INNER JOIN programa ON solicitud.id_programa=programa.id
    INNER JOIN universidad ON programa.id_universidad=universidad.id
    INNER JOIN ciudad ON universidad.id_ciudad=ciudad.id
    WHERE solicitud.id_alumno=%s AND solicitud.estado=%s
    """
    val=(id,"solicitado")
    try:
        filas=selectDB(BASE,sQuery,val)
    
        if filas:
            res = filas
        else:
            res=None
        
    except Exception as e:
        print(f"Error al eliminar la fila de solicitudes: {e}")
    return res

def obtenerPrograma(id_programa):
    sQuery="""SELECT programa.*, universidad.nombre AS universidad_nombre, ciudad.nombre AS ciudad_nombre FROM programa
    INNER JOIN universidad ON programa.id_universidad=universidad.id
    INNER JOIN ciudad ON universidad.id_ciudad=ciudad.id
    WHERE programa.id=%s"""
    val=(id_programa,)
    return selectDB(BASE,sQuery,val)