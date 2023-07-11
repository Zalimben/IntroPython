
def operacionesCadenas(name):
    """
        Operaciones básicas con cadenas
    """
    print(f'Hola, {name}')

    # Operaciones con Cadena
    name = "ada lovelace"
    print("Hello,", name.title())
    print("Hello,", name.lower())
    print("Hello,", name.upper())

    first_name = "Alan"
    last_name = "Turing"
    full_name = first_name + " " + last_name
    print("Hello, " + full_name.title() + "!")


def operacionesNumeros(nro1, nro2):
    """
       Operaciones básicas con números
    """
    print(f'Suma: {nro1 + nro2}')
    print(f'resta: {nro2 - nro1}')
    print(f'resta: {nro1 - nro2}')
    print(f'Multiplicación: {nro1 * nro2}')
    print(f'División: {nro1 / nro2}')
    print(f'División: {nro2 / nro1}')
    print(f'Exponente: {nro2 ** nro1}')
    print(f'Exponente: {nro1 ** nro2}')
    print(f'Punto Flotante: {0.2 + 0.1}')
    suma = nro1 + nro2
    print("La suma es: " + str(suma) + "!")

