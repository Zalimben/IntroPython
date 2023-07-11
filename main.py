# This is a sample Python script.
from intro.condicionales import operacionesCondicionales
from intro.diccionario import operacionesDiccionario
from intro.entrada import operacionesEntrada
from intro.estructuras import operacionesListas
from intro.iteracion import operacionesIteracion
from intro.misc import make_pizza
from intro.tiposDeDatos import operacionesCadenas, operacionesNumeros

if __name__ == '__main__':
    operacionesCadenas("Python interpreter!")
    operacionesNumeros(3, 8)
    operacionesListas()
    operacionesIteracion()
    operacionesCondicionales()
    operacionesDiccionario()
    operacionesEntrada()
    make_pizza('pepperoni')
    make_pizza('mushrooms', 'green peppers', 'extra cheese')
