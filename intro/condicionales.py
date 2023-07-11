
def operacionesCondicionales():
    """
        Operaciones básicas con condicionales
    """
    print('\nCondicionales')
    cars = ['audi', 'bmw', 'subaru', 'toyota']
    for car in cars:
        if car == 'bmw':
            print(car.upper())
        else:
            print(car.title())

    print('\nEvaluación')
    car = 'bmw'
    print(car == 'bmw')
    print(car == 'audi')

    requested_topping = 'mushrooms'
    if requested_topping != 'anchovies':
        print("Hold the anchovies!")

    print('\nOperadores Lógicos')
    age_0 = 22
    age_1 = 18
    print(age_0 >= 21 and age_1 >= 21)
    print(age_0 >= 21 or age_1 >= 21)
    print(age_0 == 22 or age_1 == 18)

    print('\nCondicionales en Listas')
    requested_toppings = ['mushrooms', 'onions', 'pineapple']
    print('mushrooms' in requested_toppings)

    requested_toppings = []
    if requested_toppings:
        for requested_topping in requested_toppings:
            print("Adding " + requested_topping + ".")
        print("\nFinished making your pizza!")
    else:
        print("Are you sure you want a plain pizza?")

    banned_users = ['andrew', 'carolina', 'david']
    user = 'marie'
    if user not in banned_users:
        print(user.title() + ", you can post a response if you wish.")

    requested_toppings = ['mushrooms', 'extra cheese']
    if 'mushrooms' in requested_toppings:
        print("Adding mushrooms.")
    if 'pepperoni' in requested_toppings:
        print("Adding pepperoni.")
    if 'extra cheese' in requested_toppings:
        print("Adding extra cheese.")
    print("\nFinished making your pizza!")


    print('\nClaúsulas if-else')
    age = 12
    if age < 4:
        print("Your admission cost is $0.")
    elif age < 18:
        print("Your admission cost is $5.")
    else:
        print("Your admission cost is $10.")
