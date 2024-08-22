lengthApellido = 16
lengthNombre = 16
lengthCodigo = 4
totallength = 36

tamanoOverflow=209
tamanoHash=491

comienzoOverflow= tamanoOverflow * totallength

filelength= 700 * totallength

def crearArchivo():
    with open('nombrearchivo.txt','w') as archivo:
        archivo.write("".ljust(filelength))

def hashing(codigo):
    posicion=codigo % 491
    return posicion


def buscar(codigo):
    with open('nombrearchivo.txt','r') as archivo:
        posicion=(hashing(codigo)-1) * totallength + lengthApellido + lengthNombre
        archivo.seek(posicion)
        if archivo.read(lengthCodigo) == codigo.ljust(lengthCodigo):
            return posicion
        else:
            archivo.seek(comienzoOverflow + (hashing(codigo)-1) * totallength + lengthApellido + lengthNombre)
            if archivo.read(lengthCodigo) == codigo.ljust(lengthCodigo):  
                return posicion + comienzoOverflow
            else:
                return -1  
            

def alta(apellido,nombre,codigo):
    posicion=hashing(int(codigo))
    
    with open('nombrearchivo.txt','r') as archivo:
        datos=archivo.read()
        datos_antes= datos[0:posicion-1]
        datos_despues=datos[posicion:len(datos)]
    with open('nombrearchivo.txt','w') as archivo:
        archivo.write(datos_antes)
        archivo.seek(posicion)
        archivo.write(apellido.ljust(lengthApellido))
        archivo.write(nombre.ljust(lengthNombre))
        archivo.write(codigo.ljust(lengthCodigo))
        archivo.write(datos_despues)


    


    







