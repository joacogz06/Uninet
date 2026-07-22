
from flask import request, session, redirect, render_template
import mariadb  # sin este paquete, Python no tendría ninguna forma de conectarse a una base de datos SQL
############################################################################
################### FUNCIONES PRINCIPALES ####################################
def conectarBD(configDB=None): 
    ''' # Establecer una conexión con el servidor MySQL
        # retorna la conexión
    '''
    mydb=None
    if configDB!=None:
        try:        
            mydb = mariadb.connect( #la coneccion con la base de datos
                    host=configDB.get("host"), 
                    user=configDB.get("user"),
                    password=configDB.get("pass"),
                    database=configDB.get("dbname")
            )
        except mariadb.Error as e:
            print("ERROR en funcion conectar BD ->",e)
    else:
        print("no funca config=None")  
    return mydb

def cerrarBD(mydb):
    ''' # Realiza el cierra un conexión a una base de datos.
        # recibe 'mydb' una conexion a una base de datos
    '''
    if mydb!=None:
        mydb.close()

def consultarDB(mydb,sQuery="",val=None,title=False): 
    if type(val) not in (tuple,list):
        val=(val,) # si el valor no vino en una tupla lo meto adentro de una, porque mariadb necesita eso si o si
    myresult=None
    try:
        if mydb!=None:
            mycursor = mydb.cursor() # Creo el cursor, el que manda y recibe los datos
            if val==None:
                mycursor.execute(sQuery)
            else:
                mycursor.execute(sQuery,val) # Si tengo valores, se los mando aparte (mas seguro)
            myresult = mycursor.fetchall() # Traigo TODAS las filas que encontró la consulta
            if title:
                myresult.insert(0,mycursor.column_names)
    except mariadb.Error as e:
        print("ERROR en funcion consultar BD ->",e)  
    #print("esto es lo que sacade la base de datos", myresult) 
    return myresult

def ejecutarDB(mydb,sQuery="",val=None):
    ''' # Realiza las consultas 'INSERT' 'UPDATE' 'DELETE'
        # recibe 'mydb' una conexion a una base de datos
        # recibe 'sQuery' la cadena con la consulta (query) sql.
        # recibe 'val' valores separados anti sql injection
        # retorna la cantidad de filas afectadas con la query.
    '''
    if type(val) not in (tuple,list):
        val=(val,)
    res=None
    try:
        
        mycursor = mydb.cursor()
        if val==None:
            mycursor.execute(sQuery)
        else:
            mycursor.execute(sQuery,val)   
        res=mycursor.rowcount        # filas afectadas
        mydb.commit()
    except mariadb.Error as e:
        mydb.rollback()
        print("ERROR ->",e)
    finally:
        mycursor.close()
    return res
    
############################################################################

############################################################################
## - - - FUNCIONES SECUNDARIAS - - - - - - - - - - - - - - - - - - - - - -
## UTILIZA LAS FUNCIONES PRINCIPALES PARA ACCEDER A LA BASE DE DATOS
##  
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def selectDB(configDB=None,sql="",val=None,title=False):
    ''' ########## SELECT
        # recibe 'configDB' un 'dict' con los parámetros de conexion
        # recibe 'sql' una cadena con la consulta sql
        # recibe 'val' valores separados anti sql injection
        # recibe 'title' booleana
        # retorna una 'list' con el resultado de la consulta
        #     cada fila de la 'list' es una 'tuple'
        #     Si 'title' es True, entonces agrega a la lista
        #     los títulos de las columnas.
    '''
    resQuery=None
    if configDB!=None:
        mydb=conectarBD(configDB)
        resQuery=consultarDB(mydb,sQuery=sql,val=val,title=title)
        cerrarBD(mydb)
    return resQuery

def insertDB(configDB=None,sql="",val=None):
    ''' ########## INSERT
        # recibe 'configDB' un 'dict' con los parámetros de conexion
        # recibe 'sql' una cadena con la consulta sql
        # recibe 'val' valores separados anti sql injection
    '''
    res=None
    if configDB!=None:
        mydb=conectarBD(configDB)
        res=ejecutarDB(mydb,sQuery=sql,val=val)
        cerrarBD(mydb)
    return res

def updateDB(configDB=None,sql="",val=None):
    res=None
    if configDB!=None:
        mydb=conectarBD(configDB)
        res=ejecutarDB(mydb,sQuery=sql,val=val)
        cerrarBD(mydb)
    return res #debuelve cuántas filas modificó la consulta UPDATE, 1 si modificó una fila, 0 si no modificó ninguna.

def deleteDB(configDB=None,sql="",val=None):
    ''' ########## DELETE
        # recibe 'configDB' un 'dict' con los parámetros de conexion
        # recibe 'sql' una cadena con la consulta sql
        # recibe 'val' valores separados anti sql injection
    '''
    res=None
    if configDB!=None:
        mydb=conectarBD(configDB)
        res=ejecutarDB(mydb,sQuery=sql,val=val)
        cerrarBD(mydb)
    return res

############################################################################ 


########################################################################## 
## CONFIGURACION DE LA CONEXION A LA BASE DE DATOS
## DICCIONARIO con los datos de la conexión
## Nota: Sería una buena práctica colocar este diccionario con los datos 
##       de la conexion en el archivo de configuración de la app
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

#es el unico diccionario que esta global, no puedo modificarlo desde cualquier lado, es una constante.
BASE={ "host":"localhost", #host: dónde vive el servidor de base de datos
        "user":"root", # user: con qué usuario de MySQL te conectás. root: es el usuario administrador 
        "pass":"", #contrasenia del usuario (root no tiene)
        "dbname":"uninet"} #nombre de la base de datos



############################################################################
###########################################################################