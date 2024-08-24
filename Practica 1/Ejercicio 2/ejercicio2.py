PATH_ARCHIVO= 'nombrearchivo.txt'

LENGTH_APELLIDO = 16
LENGTH_NOMBRE = 16
LENGTH_CODIGO = 4
LENGTH_DATO= LENGTH_APELLIDO + LENGTH_NOMBRE + LENGTH_CODIGO

LENGTH_FILE= 700 * LENGTH_DATO
HASH=701

def hashFunction(codigo):
    return codigo % 701
 

def readByPK(codigo):
    index= hashFunction(codigo)
    return readByOffset(index)

def readByOffset(index):
    pos=(index-1) * LENGTH_DATO
    with open(PATH_ARCHIVO,'r') as archivo:
        archivo.seek(pos)
        apellido = archivo.read(LENGTH_APELLIDO).strip()
        nombre = archivo.read(LENGTH_NOMBRE).strip()
        codigo = archivo.read(LENGTH_CODIGO).strip()
        return apellido,nombre,codigo



    


    







