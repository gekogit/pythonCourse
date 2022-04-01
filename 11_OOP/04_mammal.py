"""
4▹ Pomyśl co sprawia, że ssak jest ssakiem? Utwórz klasę ssaki. Stwórz kilka obiektów klasy ssaki np. wilk, koń, ssaki.
"""


class Mammal:
    def __init__(self, kind, row, temperature):
        self.kind = kind
        self.row = row
        self.temperature = temperature

    def __repr__(self):
        return f'{self.kind} -- {self.row} -- {self.temperature}'


def main():
    mammal_zoo = [Mammal('Human', 'Primates', 36.6), Mammal('Holf', 'Carnivora', 37)]
    print('\nMammal ZOO has:\n[kind] -- [row] -- [body temperature]')
    for el in mammal_zoo:
        print(Mammal.__repr__(el))





if __name__ == '__main__':
    main()
