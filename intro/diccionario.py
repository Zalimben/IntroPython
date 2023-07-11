

def operacionesDiccionario():
    """
        Operaciones básicas sobre diccionarios
    """
    print('\nCreación')

    cedula = {
        "Nombre": "Sara",
        "Apellido": "Lopez",
        "Edad": 27,
        "Documento": 1003882
    }
    print(cedula)

    dic2 = dict([
        ('Nombre', 'Sara'),
        ('Edad', 27),
        ('Documento', 1003882),
    ])
    print(dic2)

    anidado1 = {"a": 1, "b": 2}
    anidado2 = {"a": 1, "b": 2}
    d = {
        "anidado1": anidado1,
        "anidado2": anidado2
    }
    print(d)

    print('\nAcceder y modificar elementos')
    print(cedula['Nombre'])  # Sara
    print(cedula.get('Nombre'))  # Sara

    cedula['Nombre'] = "Laura"
    print(cedula)

    print('\nIterar diccionario')
    for ced in cedula:
        print(ced)

    print('')
    for x in cedula:
        print(cedula[x])

    print('')
    for clave, valor in cedula.items():
        print(clave, valor)

    print('\nMétodos diccionarios Python')
    d = {'a': 1, 'b': 2}
    d.clear()
    print(d)
    print('')

    d = {'a': 1, 'b': 2}
    print(d.get('a'))  # 1
    print(d.get('z', 'No encontrado'))  # No encontrado
    print('')

    d = {'a': 1, 'b': 2}
    it = d.items()
    print(it)  # dict_items([('a', 1), ('b', 2)])
    print(list(it))  # [('a', 1), ('b', 2)]
    print(list(it)[0][0])  # a
    print('')

    d = {'a': 1, 'b': 2}
    k = d.keys()
    print(k)  # dict_keys(['a', 'b'])
    print(list(k))  # ['a', 'b']
    print('')

    d = {'a': 1, 'b': 2}
    print(list(d.values()))  # [1, 2]

