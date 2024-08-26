LENGTH_DATO = 10
datos = "          "  # 10 espacios en blanco

if datos == "".ljust(LENGTH_DATO):
    print("La variable datos está vacía o contiene solo espacios.")
else:
    print("La variable datos contiene otros caracteres.")