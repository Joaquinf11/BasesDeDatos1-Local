from ej3bitless import * 


def generarArchivo():
    global PATH
    PATH= input("Ingrese el nombre del archivo: ") + ".txt"
    cantidad_columnas = input("numero de columnas: ")
    with open(PATH,"wt") as archivo:
        archivo.write(cantidad_columnas.ljust(LENGTH_CANT_COLUMNAS,PADDING))
        for i in range(int(cantidad_columnas)):
            archivo.write(input(f"inserte el titulo de la columna numero {i + 1}: ").ljust(LENGTH_TITULO,PADDING))
            archivo.write(input(f"inserte la cantidad de caracteres utilizados por dato en la columna numero {i + 1}: ").ljust(LENGTH_CARACTERES,PADDING))