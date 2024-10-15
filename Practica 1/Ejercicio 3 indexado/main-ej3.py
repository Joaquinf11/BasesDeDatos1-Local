import ej3
from ej3 import *


def mostrarMenu():
    print("\n ABM de Archivo de METADATA \n")
    print("0- Salir\n" +
          "1 - Mostrar archivo\n" +
          "2 - Alta\n" + 
          "3 - Modificacion\n" +
          "4 - Baja\n")


def main():
    print("Bienvenido al Sistema\n     Altas/Bajas/Modificaciones J.N.E\n")
    
    print("0- Salir\n" +
        "1 - Generar archivo nuevo \n" +
        "2 - Manipular archivo existente\n")
    
    accion=input("Elija una opcion:"  )
    if accion == '0':
        return
    if accion == '1':
            ej3.ingresarNombreArchivo()
            ej3.generarArchivo()
            print("Archivo generado exitosamente.")
    if accion == '2':
        ej3.ingresarNombreArchivo()
        ej3.readHead()
    
    mostrarMenu()
    accion= input("Ingrese una opcion: ")
    while(accion != '0'):
        if accion == '1':
           
                ej3.mostrarArchivo()
            
        elif accion == '2':
           
                print("Ingrese los datos")
                datos= ej3.ingresarDatos()
                ej3.alta(datos)
                print("Alta generada exitosamente.")
            
                
        elif accion == '3':
           
                pk=input("Ingrese la pk que desea modificar: ")
                print("Ingrese los datos")
                datos= ej3.ingresarDatos()
                ej3.update(pk, datos)
                print("Modificacion generada exitosamente.")
           
                
        elif accion == '4':
                pk=input("Ingrese la pk que desea eliminar: ")
                ej3.delete(pk)
                print("Registro eliminado exitosamente.")
    
        mostrarMenu()
        accion=input("Ingrese una opcion:")

main()




