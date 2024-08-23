lengthColumnas = 2
lengthNombreColumna = 16
lengthCaracteres = 4

lengthLinea=32
lengthColumna = 20 # tamaño de columna

def generarArchivo():
    cantColumnas=input("Ingrese la cantidad de columnas: ")
    with open('nombrearchivo.txt','w') as archivo:
        archivo.write(cantColumnas.ljust(lengthColumnas))
        for i in range(int(cantColumnas)):
            archivo.write(input(f"inserte el titulo de la columna numero {i}: ").ljust(lengthNombreColumna))
            archivo.write(input(f"inserte la cantidad de caracteres utilizados por dato en la columna numero {i}: ").ljust(lengthCaracteres))
       

def leerHeader():
    titulos=[]
    caracteres=[]
    with open('nombrearchivo.txt','r') as archivo:
        cantColumnas=int(archivo.read(lengthColumnas))
        for i in range(0,cantColumnas):
            titulos.append(archivo.read(lengthNombreColumna))
            caracteres.append(int(archivo.read(lengthCaracteres)))
    return titulos,caracteres


def mostrarArchivo():
    print("---------Info Header--------------------\n")
    with open('nombrearchivo.txt','r') as archivo:
        print(f"Cantidad de columnas: {archivo.read(lengthColumnas)} \n")
        print(f'Espacio que ocupa el nombre de columna: {lengthNombreColumna}\n')
        print(f'Espacio que ocupa el dato de la columna: {lengthCaracteres}\n')
        
        
        titulos,caracteres=leerHeader()
        print("-----------Columnas----------\n")
        for i in range(0,len(caracteres)):
            print(titulos[i].ljust(caracteres),end="")
        print("")
        print("-----------------------------\n")
        
        # archivo.seek(lengthLinea);
        # for i in range(0,2):
        #     mostrar=archivo.read(lengthLinea)
        #     print(mostrar + "\n")
#esta mal 