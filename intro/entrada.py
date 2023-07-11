
def operacionesEntrada():
    """
            Operaciones básicas de entrada de datos
    """
    print('\nLectura desde terminal')
    name = input("Ingrese su nombre: ")
    print("Hola, " + name + "!")

    number = input("Ingrese un nro: ")
    number = int(number)
    if number % 2 == 0:
        print("\nEl nro  " + str(number) + " es par.")
    else:
        print("\nEl nro " + str(number) + " es impar.")


