import ejercicio3

def mostrarMenu():
    print("ABM de Archivo de Metadata\n")
    print("1 - Generar archivo nuevo \n" +
          "2 - Mostrar archivo\n" +
          "3 - Alta\n" + 
          "4 - Modificacion\n" +
          "5 - Baja\n" + 
          "6 - Compactar \n" +
          "7 - Salir\n")

def main():
    mostrarMenu()
    accion= input()

    while(accion != '7'):
        if accion == '1':
            try:
                ejercicio3.generarArchivo()
                print("Archivo generado exitosamente.")
            except Exception as e:
                print(f"Error al generar archivo: {e}")
        elif accion == '2':
            try:
                ejercicio3.mostrarArchivo()
            except Exception as e:
                print(f"Error al mostrar archivo: {e}")
        elif accion == '3':
            try:
                ejercicio3.alta()
                print("Alta generada exitosamente.")
            except Exception as e:
                print(f"Error al dar de alta: {e}")
        mostrarMenu()
        accion=input()

main()