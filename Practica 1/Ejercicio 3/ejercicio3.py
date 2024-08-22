lengthColumnas = 2
lengthNombreColumna = 16
lengthDatos = 4

lengthLinea=32
lengthColumna = 20 # tamaño de columna

def generarArchivo():
    cantColumnas=input("Ingrese la cantidad de columnas")
    with open('nombrearchivo.txt','w') as archivo:
        archivo.write(cantColumnas.ljust(lengthColumnas))
        for i in range(int(cantColumnas)):
            archivo.write(input(f"inserte el titulo de la columna numero {i}: ").ljust(lengthNombreColumna))
            archivo.write(input(f"inserte la cantidad de caracteres utilizados por dato en la columna numero {i}: ").ljust(lengthDatos))
       


def mostrarArchivo():
    with open('nombrearchivo.txt','r') as archivo:
        print("-----------------------------\n")
        print(f"Cantidad de columnas: {archivo.read(lengthColumnas)} \n")
        print(f'Espacio que ocupa el nombre de columna: {lengthNombreColumna}\n')
        print(f'Espacio que ocupa el dato de la columna: {lengthDatos}\n')
        print("-----------------------------\n")
        archivo.seek(lengthLinea);
        for i in range(0,2):
            mostrar=archivo.read(lengthLinea)
            print(mostrar + "\n")
#esta mal 