from poo.animales.gato import Gato
from poo.animales.perro import Perro
from poo.animales.vaca import Vaca
from poo.controlRemoto.ControlLG import ControlLG
from poo.controlRemoto.controlSamsung import ControlSamsung
from poo.jugadores.arqueroVolante import ArqueroVolante
from poo.pelotas.Futbol import Futbol
from poo.pelotas.Golf import Golf

if __name__ == '__main__':
    print("\nAnimales")
    venom = Perro('Venom', 2, "Caniche")
    print("Mi perro se llama " + venom.name.title() + ".")
    print("Mi perro tiene " + str(venom.age) + " años.")
    venom.sentado()
    venom.recuperar_especie_completa()

    print()
    dante = Perro('Dante', 1, "Mestizo")
    dante.describeme()
    print("Mi perro se llama " + dante.name.title() + ".")
    print("Mi perro tiene " + str(dante.age) + " años.")
    dante.hablar()

    michi = Gato("Michi", "Egipcio")

    print()
    for animal in venom, dante, michi, Vaca("Lechera"):
        animal.describeme()
        animal.hablar()
        animal.sentado()

    print()
    vaca = Vaca("Lechera")
    vaca.describeme()
    vaca.hablar()

    print("\nHerencia Múltiple")
    volante = ArqueroVolante("Messi", "10")
    volante.atajar()
    volante.centro()

    print("\nControl Remoto")
    control = ControlSamsung()
    control.siguiente_canal()
    control.siguiente_canal()
    control.bajar_volumen()

    controlLg = ControlLG()
    controlLg.bajar_volumen()
    controlLg.bajar_volumen()

    pelotaGolf = Golf("3", "Plástico")
    pelotaFutbol = Futbol("18", "Cuero")
    pelotaGolf.description()
    pelotaFutbol.description()
