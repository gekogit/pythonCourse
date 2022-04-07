"""
1▹ Korzystając z wikipedii utwórz klasy - Kot, Pies, Człowiek. Każda z nich powinna dziedziczyć z nadrzędnej klasy
Ssaki. Klasa Ssaki powinna dziedziczyć z klasy Zwierzęta. Utwórz obiekty klas - kot, pies i człowiek, udowodnij,
 że rzeczywiście korzystają z klas rodziców.
"""


class Animals:
    blood_color = 'red'

    def __init__(self):
        print("I am an animal")


class Mammal(Animals):
    born_alive = True

    def __init__(self, kind, row, temperature):
        self.kind = kind
        self.row = row
        self.temperature = temperature

    def __repr__(self):
        return f'{self.kind} -- {self.row} -- {self.temperature}'


class Cat(Mammal):

    def __init__(self, name, color, year):
        self.name = name
        self.color = color
        self.year = year

    def grind(self):
        print('miau miau')



class Dog(Mammal):

    def __init__(self, name, color, year):
        self.name = name
        self.color = color
        self.year = year

    def bark(self):
        print('hau hau')

    def is_older(self, age):
        return True if self.year > age else False


class Man(Mammal):

    def __init__(self, name, age):
        self.name = name
        self.age = age


def print_check(patient):
    print(f' {patient.name} has from animal blood color: {patient.blood_color} and as mammals was born alive :{patient.born_alive}')


def main():
    m1 = Man("Tom", 25)
    d1 = Dog("Ricky", 'white', 4)
    c1 = Cat("Catty", "black", 3)
    print_check(m1)
    print_check(d1)
    print_check(c1)


if __name__ == '__main__':
    main()
