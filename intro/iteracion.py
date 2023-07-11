

def operacionesIteracion():
    """
        Operaciones básicas de flujo de control
    """
    print('\nIteración')
    magicians = ['alice', 'david', 'carolina']
    for magician in magicians:
        print(magician)

    for value in range(1, 5):
        print(value)

    x = 5
    while x > 0:
        x -= 1
        print(x)

    numbers = list(range(1, 6))
    print(numbers)

    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print(f'El min es: {min(digits)}')
    print(f'El max es: {max(digits)}')
    print(f'La suma es: {sum(digits)}')

    print('\nTuplas')
    dimensions = (200, 50)
    print(dimensions[0])
    print(dimensions[1])

    dimensions = (2, 5)
    print("Original dimensions:")
    for dimension in dimensions:
        print(dimension)
    dimensions = (4, 10)
    print("\nModified dimensions:")
    for dimension in dimensions:
        print(dimension)

    lista = [1, 2, 3, 'Hola Mundo', 4, 5, 6]
    print(lista)