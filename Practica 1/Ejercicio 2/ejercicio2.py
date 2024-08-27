PATH_ARCHIVO= 'nombrearchivo.txt'

LENGTH_APELLIDO = 16
LENGTH_NOMBRE = 16
LENGTH_CODIGO = 4
LENGTH_DATO= LENGTH_APELLIDO + LENGTH_NOMBRE + LENGTH_CODIGO

HASH=701
LENGTH_HASH= HASH * LENGTH_DATO
OVERFLOW= HASH * LENGTH_DATO

def inicarArchivo():
    with open(PATH_ARCHIVO,'w') as archivo:
       archivo.write( "".ljust(LENGTH_HASH))

def hashFunction(codigo):
    codigo= int(codigo)
    return codigo % HASH
 

def readByPK(codigo):
    pos= (hashFunction(codigo)-1)*LENGTH_DATO
    registro=readByOffset(pos)
    if registro.isspace() or registro[2] != codigo:
        registro=readOverflowByPK(codigo)
    return registro

def readByOffset(pos):
    with open(PATH_ARCHIVO,'r') as archivo:
        archivo.seek(pos)
        apellido = archivo.read(LENGTH_APELLIDO)
        nombre = archivo.read(LENGTH_NOMBRE)
        codigo = archivo.read(LENGTH_CODIGO)
        return apellido,nombre,codigo

def readOverflowByPK(codigo): 
    pos=offsetOverflow(codigo)
    with open(PATH_ARCHIVO,'r') as archivo:
        archivo.seek(pos)
        apellido = archivo.read(LENGTH_APELLIDO) 
        nombre = archivo.read(LENGTH_NOMBRE)
        codigo = archivo.read(LENGTH_CODIGO)
    return apellido,nombre,codigo
        
def offsetOverflow(codigo):
    pos= OVERFLOW
    with open(PATH_ARCHIVO,'r') as archivo:
        archivo.seek(pos)
        registro= archivo.read(LENGTH_DATO)
        while (registro[2] != codigo and registro[2] != "".ljust(LENGTH_CODIGO)):
            pos+=LENGTH_DATO
            registro= archivo.read(LENGTH_DATO)
    return pos

def readOverflowByOffset(pos):
    with open(PATH_ARCHIVO,'r') as archivo:
        archivo.seek(pos)
        apellido = archivo.read(LENGTH_APELLIDO)
        nombre = archivo.read(LENGTH_NOMBRE)
        codigo = archivo.read(LENGTH_CODIGO)
    return apellido,nombre,codigo


def writeByPK(apellido,nombre,codigo):
    datos= readByPK(codigo)
    if (datos[0] == "".ljust(LENGTH_APELLIDO)):
        pos= (hashFunction(codigo)-1)*LENGTH_DATO
        writeByOffset(pos,apellido,nombre,codigo)
    else:
        writeOverflow(apellido,nombre,codigo)

    
def writeByOffset(pos,apellido,nombre,codigo):
    with open(PATH_ARCHIVO,'r+b') as archivo:
        archivo.seek(pos)
        archivo.write(apellido.ljust(LENGTH_APELLIDO).encode("utf-8"))
        archivo.write(nombre.ljust(LENGTH_NOMBRE).encode("utf-8"))
        archivo.write(codigo.ljust(LENGTH_CODIGO).encode("utf-8"))

def writeOverflow(apellido,nombre,codigo):
    with open(PATH_ARCHIVO,'a') as archivo:
        archivo.write(apellido.ljust(LENGTH_APELLIDO))
        archivo.write(nombre.ljust(LENGTH_NOMBRE))
        archivo.write(codigo.ljust(LENGTH_CODIGO))


def insert(new_apellido,new_nombre,new_codigo):
    writeByPK(new_apellido,new_nombre,new_codigo)

#no se si sirve primero leer el overflow pero no se me ocurre otra forma ya que el readbypk pasa por el overflow y aca no los puedo diferenciar
def delete (codigo):
    registro= readOverflowByPK(codigo)
    pos=offsetOverflow(codigo)
    with open(PATH_ARCHIVO,"r+b") as archivo:
        if registro is not None:
                archivo.seek(-LENGTH_DATO,2)
                ultimo_registro = archivo.read()
                archivo.seek(pos)
                archivo.write(ultimo_registro)
                archivo.seek(-LENGTH_DATO,2)
                archivo.truncate()
        else:
            registro=readByPK(codigo)
            pos= (hashFunction(codigo)-1)* LENGTH_DATO
            archivo.seek(pos)
            archivo.write("".ljust(LENGTH_DATO).encode("utf-8"))
       
                
def update(old_codigo,new_apellido,new_nombre,new_codigo):
    old_registro=readByPK(old_codigo)
    if old_registro is not None:
        if new_apellido is None:
            new_apellido = old_registro[0]

        if new_nombre is None:
            new_nombre = old_registro[1]

        if new_codigo is None:
            new_codigo = old_registro[2]
        writeByPK(new_apellido,new_nombre,new_codigo)
    

def mostrarArchivo():
    index = 1
    
    while index != 700:
        apellido,nombre,codigo = readByOffset(index)
        if apellido == "".ljust(LENGTH_APELLIDO):
            index+=1
        else:
            print("----------------------")
            print("Cliente ", index)
            print("Apellido: ", apellido)
            print("Nombre: ", nombre)
            print("Código: ", codigo)
            print("----------------------")
            index += 1
    #leer overflow
    print("|||||||||OVERFLOW||||||||||")
    index=1
    while True:
        registro=readOverflowByOffset(index)
        if registro is None:
            break
        print("----------------------")
        print("Cliente ", index)
        print("Apellido: ", registro[0])
        print("Nombre: ", registro[1])
        print("Código: ", registro[2])
        print("----------------------")
        index += 1

    
    
    


    







