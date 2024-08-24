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
        apellido = archivo.read(LENGTH_APELLIDO).strip() #chequear que hace el strip, puede fallar aca por como lo lees en writebypk
        nombre = archivo.read(LENGTH_NOMBRE).strip()
        codigo = archivo.read(LENGTH_CODIGO).strip()
        return apellido,nombre,codigo


def writeByPK(apellido,nombre,codigo):
    datos= readByPK(codigo)
    if (datos == "".ljust(LENGTH_DATO)):
       index= hashFunction(codigo)
       writeByOffset(index,apellido,nombre,codigo)
    else:
        return # aca iria overflow creo
    
def writeByOffset(index,apellido,nombre,codigo):
    pos= (index-1)* LENGTH_DATO
    with open(PATH_ARCHIVO,'r+b') as archivo:
        archivo.seek(pos)
        archivo.write(apellido.ljust(LENGTH_APELLIDO).encode("utf-8"))
        archivo.write(nombre.ljust(LENGTH_NOMBRE).encode("utf-8"))
        archivo.write(codigo.ljust(LENGTH_CODIGO).encode("utf-8"))
    # tene cuidado con el tema del overflow aca chequealo 

def insert(new_apellido,new_nombre,new_codigo):
    writeByPK(new_apellido,new_nombre,new_codigo)

def delete (codigo):
    index= hashFunction(codigo)
    pos=(index-1)*LENGTH_DATO
    # IF ESTA EN EL HASH LO BORRO SINO BUSCO EN OVERFLOW

    

    
    


    







