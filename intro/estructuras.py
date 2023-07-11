
# Listas
def operacionesListas():
    """
        Operaciones básicas sobre listas
    """
    bicicletas = ['trek', 'cannondale', 'redline', 'specialized']
    motos = ['honda', 'yamaha', 'suzuki']

    print(bicicletas)
    print(motos)

    # Operaciones sobre listas
    print('\nAccediendo elementos por el índice')
    print(bicicletas[0])
    print(bicicletas[1])
    print(bicicletas[-1])

    print('\nTamaño')
    print(f'El tamaño de bicicletas es {len(bicicletas)}')
    print(f'El tamaño de motos es {len(motos)}')

    print('\nActualización')
    motos[0] = 'ducati'
    print(motos)

    print('\nInserción')
    motos.append('honda')
    print(motos)
    motos.insert(2, 'bmw')
    print(motos)

    print('\nEliminación: Índice')
    del motos[0]
    print(motos)
    del motos[2]
    print(motos)
    del motos[-1]
    print(motos)

    print('\nEliminación: Pop')
    motos = ['honda', 'yamaha', 'suzuki']
    popped_motorcycle = motos.pop()
    print(motos)
    print(popped_motorcycle)
    popped_motorcycle = motos.pop(0)
    print(motos)
    print(popped_motorcycle)

    print('\nEliminación: Remove')
    motos = ['honda', 'yamaha', 'suzuki', 'ducati']
    print(motos)
    too_expensive = 'suzuki'
    motos.remove(too_expensive)
    print(motos)

    print('\nOrdenación')
    cars = ['bmw', 'audi', 'toyota', 'subaru']
    print(cars)
    cars.sort()
    print(cars)
    cars.sort(reverse=True)
    print(cars)

    print('\nImpresión')
    print(cars)
    cars.reverse()
    print(cars)
