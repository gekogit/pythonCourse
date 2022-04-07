"""
2▹ Do klasy człowiek dodaj metodę super() tak, aby móc wyświetlić opis dostępny gdziekolwiek w klasie ssaki.
"""
"""
1▹ Korzystając z wikipedii utwórz klasy - Kot, Pies, Człowiek. Każda z nich powinna dziedziczyć z nadrzędnej klasy
Ssaki. Klasa Ssaki powinna dziedziczyć z klasy Zwierzęta. Utwórz obiekty klas - kot, pies i człowiek, udowodnij,
 że rzeczywiście korzystają z klas rodziców.
"""


class Animals:
    blood_color = 'red'

    def i_am(self):
        print("I am an animal.")


class Mammal(Animals):
    born_alive = True

    def __init__(self, kind, row, temperature):
        self.kind = kind
        self.row = row
        self.temperature = temperature

    def __repr__(self):
        return f'{self.kind} -- {self.row} -- {self.temperature}'

    def i_am(self):
        print("I am a mammal.")


class Cat(Mammal):

    def __init__(self, name, color, year):
        self.name = name
        self.color = color
        self.year = year

    def grind(self):
        print('miau miau')

    def i_am(self):
        print("I am a cat.")


class Dog(Mammal):

    def __init__(self, name, color, year):
        self.name = name
        self.color = color
        self.year = year

    def bark(self):
        print('hau hau')

    def is_older(self, age):
        return True if self.year > age else False

    def i_am(self):
        print("I am a dog.")


class Man(Mammal):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def i_am(self):
        super().i_am()
        print("I am a man.")


def print_check(creature):
    print(f' {creature.name} has from animal blood color: {creature.blood_color}'
          f' and as mammals was born alive :{creature.born_alive}')


def main():
    m1 = Man("Tom", 25)
    d1 = Dog("Ricky", 'white', 4)
    c1 = Cat("Catty", "black", 3)
    print('\nWhat can say the Man: ')
    m1.i_am()


if __name__ == '__main__':
    main()
