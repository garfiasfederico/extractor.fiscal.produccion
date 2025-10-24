#from clases.logs import Log
#import getdatacompany

#getdatacompany.getDataCompany("TRA1001211I3")
#if(getdatacompany.contribuyente==""):
#    print("Contribuyente no localizado")
#else:
#    print(f"Contribuyente localizado: {getdatacompany.contribuyente}")

#def pruebaFuncion():
#    return {
#        "result":"ok",
#        "message":"Proceso concluido"
#    }

#prueba = pruebaFuncion()
#log = Log("logs/log_declaraciones.log")
#log.write("info","Hola que tal")


import pathlib
import base64
from base64 import b64decode, b64encode
import getdatacompany

def pdf_to_base64(file):
    try:
        with open(file, "rb") as pdf_file:
            encoded_string = base64.b64encode(pdf_file.read())
            return encoded_string.decode("utf-8")  # Decode bytes to string
    except FileNotFoundError:
        print(f"Error: File not found at {file}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

archivos = []

#for pdf_file in pathlib.Path('E:\\SAT\\SAGF8705279C8').glob('*2019*.pdf'):    
#    archivos.append(pdf_to_base64(pdf_file))

#print(archivos)

getdatacompany.getDataCompany("GAC1409268N9")
print(getdatacompany.password_fiel)



import os,glob

def renombra_ultima_descarga(repo, nuevo_nombre):
    files = glob.glob(repo + '/*')
    print( len(files))
    max_file = max(files, key=os.path.getctime)
    nombre_archivo = max_file.split("/")[-1].split(".")[0]
    nueva_ruta = max_file.replace(nombre_archivo, nuevo_nombre)
    os.rename(max_file, nueva_ruta)
    return nueva_ruta

#renombra_ultima_descarga("/Library/WebServer/Documents/extractorfiscal/ACR140408T34/DM","last_file")

dic = {
    "Enero":"ene",
    "Febrero":"feb",
    "Marzo":"mar",
    "Abril":"abr",
    "Mayo":"may",
    "Junio":"jun",
    "Julio":"jul",
    "Agosto":"ago",
    "Septiembre":"sep",
    "Octubre":"oct",
    "Noviembre":"nov",
    "Diciembre":"dic",
}

print (dic["Enero"])

archivos = ""
for pdf_file in pathlib.Path("/Library/WebServer/Documents/extractorfiscal/ACR140408T34/DM").glob('*.pdf'):    
                archivos = archivos + str(pdf_file) + "|"
print(archivos)

getdatacompany.getDataCompany("CPW011226QT9")
print(getdatacompany.password_fiel)

#import descarga_contabilidad_electronica_modificado

#descarga_contabilidad_electronica_modificado.getfilescontabilidadelectronica("ACR140408T34",2016,2016,"CE")