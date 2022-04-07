"""
5▹ Stwórz abstrakcyjną klasę Pojazdy. Utwórz potomne klasy pojazdy np. Samochód, Rower, Autobus, Ciężarówki.
 Dodaj opisy zgodne z tym jak te pojazdy są klasyfikowane. Jaki rodzaj dokumentu jest potrzebny, by kierować poszczegolnym pojazdem.
"""


from abc import ABC, abstractmethod


class Vehicles(ABC):
    @abstractmethod
    def txt(self):
        pass

    @abstractmethod
    def doc(self):
        pass


class Car(Vehicles):
    def txt(self):
        return "The fastest vehicle"

    def doc(self):
        return "driving licence B needed"


class Bike(Vehicles):
    def txt(self):
        return "Small vehicle"

    def doc(self):
        return "no driving licence needed"


class Bus(Vehicles):
    def txt(self):
        return "Big vehicle to transport people"

    def doc(self):
        return "driving licence D needed"


class Truck(Vehicles):
    def txt(self):
        return "Big vehicle to transport things"

    def doc(self):
        return "driving licence C needed"


def print_check(veh):
    print(f' {veh.txt()}  {veh.doc()} to use.')


def main():
    b1 = Bike()
    c1 = Car()
    bus1 = Bus()
    t1 = Truck()
    print_check(b1)
    print_check(c1)
    print_check(bus1)
    print_check(t1)


if __name__ == '__main__':
    main()
