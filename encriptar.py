from cryptography.fernet import Fernet

def generar_clave() :
    clave = Fernet.generate_key()
    #print(clave)

    archivo_clave = open("clave.txt","wb")
    archivo_clave.write(clave)
    archivo_clave.close()

def cargar_clave():
    clave = open("clave.txt","r")
    almacenar_clave = clave.read()
    return almacenar_clave

def encriptar_archivo(archivo,clave):
    f = Fernet(clave)

    txt = open(archivo,"rb")
    almacenamos = txt.read()
    txt.close()

    texto_encriptado = f.encrypt(almacenamos)

    txt = open(archivo,"wb")
    txt.write(texto_encriptado)
    txt.close()

def desencriptar_archivo(archivo,clave):
    f = Fernet(clave)

    txt = open(archivo,"rb")
    almacenamos = txt.read()
    txt.close()

    texto_desencriptado = f.decrypt(almacenamos)

    txt = open(archivo,"wb")
    txt.write(texto_desencriptado)
    txt.close()


clave = cargar_clave()

archivo = input("\n Introduzca el archivo a encriptar: ")
#encriptar_archivo(archivo,clave)
#desencriptar_archivo(archivo,clave)