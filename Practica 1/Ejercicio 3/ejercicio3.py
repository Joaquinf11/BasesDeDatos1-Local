LENGTH_CANT_COLUMNAS = 2
LENGTH_NOMBRE_COLUMNA = 16
LENGTH_CARACTERES = 4

LENGTH_COLUMNA = LENGTH_NOMBRE_COLUMNA + LENGTH_CARACTERES  # tamaño de columna

PADDING=" "
ESTADO_LONGITUD=1
ESTADO_ACTIVA="A"
ESTADO_BAJA="B"
TITULOS=0
CARACTERES=1

PATH_ARCHIVO= 'nombrearchivo.txt'

class Metadata:
    def __init__(self):
        self.cantidad_columnas= 1
        self.titulos= ["Estado".ljust(LENGTH_NOMBRE_COLUMNA)]
        self.caracteres=[ESTADO_LONGITUD]
        self.size_data= ESTADO_LONGITUD #HAY QUE INICIARLO CON ESTADO_LONGITUD
        self.size_head=0

METADATA = Metadata()

def generarArchivo():
    cantidad_columnas=input("Ingrese la cantidad de columnas: ")
    with open(PATH_ARCHIVO,'w') as archivo:
        archivo.write(cantidad_columnas.ljust(LENGTH_CANT_COLUMNAS,PADDING))
        for i in range(int(cantidad_columnas)):
            archivo.write(input(f"inserte el titulo de la columna numero {i}: ").ljust(LENGTH_NOMBRE_COLUMNA,PADDING))
            archivo.write(input(f"inserte la cantidad de caracteres utilizados por dato en la columna numero {i}: ").ljust(LENGTH_CARACTERES,PADDING))

def readHead(): 
    with open(PATH_ARCHIVO,'r') as archivo:
        cantidad_columnas=int(archivo.read(LENGTH_CANT_COLUMNAS))
        METADATA.cantidad_columnas=cantidad_columnas + 1 # mas uno por agregar ESTADO
        METADATA.size_head= LENGTH_CANT_COLUMNAS + (LENGTH_COLUMNA * (int(cantidad_columnas)))
        for i in range(0,cantidad_columnas):
            METADATA.titulos.append(archivo.read(LENGTH_NOMBRE_COLUMNA))
            caracteres=int(archivo.read(LENGTH_CARACTERES))
            METADATA.caracteres.append(caracteres)
            METADATA.size_data +=  caracteres

def getOffset(index):
    pos= METADATA.size_head + (METADATA.size_data * ((int(index))-1))
    return pos


def readByPK(index):
    pos= getOffset(index)
    return readByOffset(pos)

def readByOffset(pos):
    datos=[]
    with open(PATH_ARCHIVO,'r') as archivo:
        archivo.seek(pos)
        for i in range(0,METADATA.cantidad_columnas):
            datos.append(archivo.read(METADATA.caracteres[i]))
    return datos

def writeByPK(index,datos):
    if index is not None:
        pos = getOffset(index)
    else:
        pos = None
    writeByOffset(pos,datos)
    

def writeByOffset(pos,datos):
    with open(PATH_ARCHIVO,'r+b') as archivo:
        if pos is None:
            archivo.seek(0,2)
        else:
            archivo.seek(pos)
        archivo.write(ESTADO_ACTIVA.encode("utf-8"))
        for i in range(0, METADATA.cantidad_columnas-1):
            archivo.write(datos[i].ljust(METADATA.caracteres[i+1],PADDING).encode("utf-8"))
    

def insert(index,datos):
    writeByPK(index,datos)

def delete(index):
    pos=getOffset(index)
    with open(PATH_ARCHIVO,'r+') as archivo:
       archivo.seek(pos)
       archivo.write(ESTADO_BAJA)


def update(index,new_datos):
    old_datos = readByPK(index)
    if old_datos[0] == "B":
        print("No se encuentra cargado el registro")
        return
    for i in range(0,METADATA.cantidad_columnas-1):
        if new_datos[i].isspace():
            new_datos[i]= old_datos[i+1]
    writeByPK(index,new_datos)

def mostrarArchivo():
    print("----------------------------------Head------------------------------\n")
    for i in range(1,METADATA.cantidad_columnas):
        print(f"Columna {i}: {METADATA.titulos[i]}  || Longitud: {METADATA.caracteres[i]}") 
    print("----------------------------------------------------------------------\n")

    index=1
    while True:
        datos=readByPK(index)
        if datos[0] == "":
            break
        elif datos[0] == "B":
            index +=1
        else:
            print("-----------------------------")
            for i in range(1,METADATA.cantidad_columnas):
                    print(f"{METADATA.titulos[i].strip()}: {datos[i]}")
            index+=1
            print("-----------------------------\n")

def ingresarDatos():
    datos = []
    for i in range(1,METADATA.cantidad_columnas):
        datos.append(input(f"{METADATA.titulos[i].strip()}: ").ljust(METADATA.caracteres[i],PADDING))
    return datos