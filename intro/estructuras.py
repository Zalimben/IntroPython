
# Listas
def operacionesListas():
    """
        Operaciones básicas sobre listas
    """
    bicycles = ['trek', 'cannondale', 'redline', 'specialized']
    motorcycles = ['honda', 'yamaha', 'suzuki']

    print(bicycles)
    print(motorcycles)

    # Operaciones sobre listas

    print('\nAccediendo elementos por el índice')
    print(bicycles[0])
    print(bicycles[-1])

    print('\nTamaño')
    print(f'El tamaño de bicycles es {len(bicycles)}')
    print(f'El tamaño de motorcycles es {len(motorcycles)}')

    print('\nActualización')
    motorcycles[0] = 'ducati'
    print(motorcycles)

    print('\nInserción')
    motorcycles.append('honda')
    print(motorcycles)
    motorcycles.insert(2, 'bmw')
    print(motorcycles)

    print('\nEliminación: Índice')
    del motorcycles[0]
    print(motorcycles)
    del motorcycles[2]
    print(motorcycles)
    del motorcycles[-1]
    print(motorcycles)

    print('\nEliminación: Pop')
    motorcycles = ['honda', 'yamaha', 'suzuki']
    popped_motorcycle = motorcycles.pop()
    print(motorcycles)
    print(popped_motorcycle)
    popped_motorcycle = motorcycles.pop(0)
    print(motorcycles)
    print(popped_motorcycle)

    print('\nEliminación: Remove')
    motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
    print(motorcycles)
    too_expensive = 'suzuki'
    motorcycles.remove(too_expensive)
    print(motorcycles)

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
