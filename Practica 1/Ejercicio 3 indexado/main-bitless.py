import ej3bitless
from ej3bitless import *
import generarArchivo

def mostrarMenu():
    print("\n ABM de Archivo de Metadata \n")
    print("0- Salir\n" +
          "1 - Mostrar archivo\n" +
          "2 - Alta\n" + 
          "3 - Modificacion\n" +
          "4 - Baja\n")

def ingresarDatos(pk = None):
    dato = Dato()
    j = 0
    if pk is not None:
        j = 1
        dato.datos.append(pk.ljust(metadata.caracteres_pk(),PADDING))
    for i in range(j,metadata.cantidadColumnas):
        dato.datos.append(input(f"{metadata.titulos[i].strip()}: ").ljust(metadata.caracteres[i],PADDING))
    return dato


def main():
    print("Bienvenido al Sistema\n     Altas/Bajas/Modificaciones J.N.E\n")
    
    print("0- Salir\n" +
        "1 - Generar archivo nuevo \n" +
        "2 - Manipular archivo existente\n")
    
    accion=input("Elija una opcion:"  )
    if accion == '0':
        return
    if accion == '1':
       
            generarArchivo.generarArchivo()
            print("Archivo generado exitosamente.")

    mostrarMenu()
    accion= input("Ingrese una opcion: ")

    

    while(accion != '0'):
        if accion == '1':
           
                ej3bitless.mostrarArchivo()
            
        elif accion == '2':
           
                print("Ingrese los datos")
                datos= ingresarDatos()
                ej3bitless.insert(None, datos)
                print("Alta generada exitosamente.")
            
                
        elif accion == '3':
           
                pk=input("Ingrese la pk que desea modificar: ")
                print("Ingrese los datos")
                datos= ingresarDatos()
                ej3bitless.update(pk, datos)
                print("Modificacion generada exitosamente.")
           
                
        elif accion == '4':
                pk=input("Ingrese la pk que desea eliminar: ")
                ej3bitless.delete(pk)
                print("Registro eliminado exitosamente.")
        
        
        mostrarMenu()
        accion=input("Ingrese una opcion:")

main()





def main():

    acantidadColumnasion = input("Ingrese una de las siguientes opciones: \n A(altas) | B(bajas) | M(modificaciones) | C(cerrar el programa) | S(mostrar la lista)\n").lower()
    if acantidadColumnasion == "a":
        alta()

    elif acantidadColumnasion == "b":
        baja()

    elif acantidadColumnasion == "m":
        pk = input("Ingrese la pk del cliente a modificar: ")
        update(pk)

    elif acantidadColumnasion == "s":
        mostrarlista()

    if acantidadColumnasion != "c":
        main()
