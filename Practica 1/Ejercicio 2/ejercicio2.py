PATH_ARCHIVO= 'nombrearchivo.txt'

LENGTH_APELLIDO = 16
LENGTH_NOMBRE = 16
LENGTH_CODIGO = 4
LENGTH_DATO= LENGTH_APELLIDO + LENGTH_NOMBRE + LENGTH_CODIGO

LENGTH_FILE= 700 * LENGTH_DATO
HASH=701
OVERFLOW= HASH * LENGTH_DATO

def hashFunction(codigo):
    return codigo % HASH
 

def readByPK(codigo):
    index= hashFunction(codigo)
    resultado= readByOffset(index)
    if not resultado:
        resultado =readOverflow(codigo)
    return resultado

def readByOffset(index):
    pos=(index-1) * LENGTH_DATO
    with open(PATH_ARCHIVO,'r') as archivo:
        archivo.seek(pos)
        apellido = archivo.read(LENGTH_APELLIDO).strip() #chequear que hace el strip, puede fallar aca por como lo lees en writebypk
        nombre = archivo.read(LENGTH_NOMBRE).strip()
        codigo = archivo.read(LENGTH_CODIGO).strip()
        return apellido,nombre,codigo

def readOverflow(codigo): 
    with open(PATH_ARCHIVO,'r') as archivo:
        archivo.seek(OVERFLOW)
        registro= archivo.read(LENGTH_DATO)
        while (registro[2] != codigo & registro[2] != "".ljust(LENGTH_DATO)):
            archivo.seek(LENGTH_DATO)
            registro= archivo.read(LENGTH_DATO)
    return registro        

def writeByPK(apellido,nombre,codigo):
    datos= readByPK(codigo)
    if (datos == "".ljust(LENGTH_DATO)):
       index= hashFunction(codigo)
       writeByOffset(index,apellido,nombre,codigo)
    else:
        writeOverflow(apellido,nombre,codigo)
    
def writeByOffset(index,apellido,nombre,codigo):
    pos= (index-1)* LENGTH_DATO
    with open(PATH_ARCHIVO,'r+b') as archivo:
        archivo.seek(pos)
        archivo.write(apellido.ljust(LENGTH_APELLIDO).encode("utf-8"))
        archivo.write(nombre.ljust(LENGTH_NOMBRE).encode("utf-8"))
        archivo.write(codigo.ljust(LENGTH_CODIGO).encode("utf-8"))
    # tene cuidado con el tema del overflow aca chequealo 

def writeOverflow(apellido,nombre,codigo):
    with open(PATH_ARCHIVO,'a') as archivo:
        archivo.write(apellido.ljust(LENGTH_APELLIDO))
        archivo.write(nombre.ljust(LENGTH_NOMBRE))
        archivo.write(codigo.ljust(LENGTH_CODIGO))

def insert(new_apellido,new_nombre,new_codigo):
    writeByPK(new_apellido,new_nombre,new_codigo)

def delete (codigo):
    registro= readByPK(codigo)
    if registro is not None:
        pos= (hashFunction(codigo)-1)* LENGTH_DATO
        with open(PATH_ARCHIVO,"r+b") as archivo:
            archivo.seek(-LENGTH_DATO,2)
            ultimo_registro = archivo.read()
            archivo.seek(pos)
            archivo.write(ultimo_registro)
            archivo.seek(-LENGTH_DATO,2)
            archivo.truncate()
    else:
        registro= readOverflow(codigo)
        if registro is not None:
            

    # IF ESTA EN EL HASH LO BORRO SINO BUSCO EN OVERFLOW




    
    


    







