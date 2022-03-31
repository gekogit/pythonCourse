"""
1▹ Skorzystaj z wprowadzenia do OOP. Stwórz klasę Pies, która posiada wspomniane atrybuty oraz metodę.
atrybuty: imię, kolor sierści, rasę
metody: szczekaj, machaj ogonem
Utwórz kilka obiektów klasy Pies z różnymi parametrami.
"""


class Dog:
    def __init__(self, name, color, race):
        self.name = name
        self.color = color
        self.race = race

    def bark(self):
        print('Hau Hau')

    def swing_tail(self):
        print('Swing')


def main():
    my_dog = Dog('Misiek', 'white', 'amstaf')
    my_mum_dog = Dog('Żaba', 'braun', 'cur')
    print('My dog:', my_dog.__dict__)
    my_dog.bark()
    print('My mum dog:', my_mum_dog.__dict__)
    my_mum_dog.swing_tail()


if __name__ == '__main__':
    main()
