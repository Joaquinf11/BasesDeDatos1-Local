class Registro:
    
    def __init__(registro,apellido,nombre,codigo):
        registro.apellido=apellido
        registro.nombre= nombre
        registro.codigo= codigo
        Registro.lista_registros.append(registro)
    def __repr__(registro):
        return f"{registro.nombre} {registro.apellido}  {registro.codigo}\n"
# ejemplo1= Registro("Joaquin","Falco","213")
# ejemplo2= Registro("julia","Falco","23")
# ejemplo3= Registro("clara","saliche","213")


class Tabla:
    def __init__(tabla,codigo) :
        tabla.hashing= codigo % 697
        tabla.lista_colisiones
        tabla.lista_registros

    def hashing(codigo):
        resultado=codigo % 697
        return resultado
    
resultado=Tabla(123)

print(resultado)

    

