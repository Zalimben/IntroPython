

def operacionesDiccionario():
    """
        Operaciones básicas sobre diccionarios
    """
    print('\nCreación')

    dic = {
        "Nombre": "Sara",
        "Edad": 27,
        "Documento": 1003882
    }
    print(dic)

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
    print(dic['Nombre'])  # Sara
    print(dic.get('Nombre'))  # Sara

    dic['Nombre'] = "Laura"
    print(dic)

    print('\nIterar diccionario')
    for x in dic:
        print(x)

    print('')
    for x in dic:
        print(dic[x])

    print('')
    for x, y in dic.items():
        print(x, y)

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

