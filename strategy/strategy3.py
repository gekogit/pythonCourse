class Warrior:
    def __repr__(self):
        return f'Warrior, {self.__class__.__name__}: hp={self.__life}, exp={self.__experience}'

    def march(self, distance):
        print(f'Warrior, {self.__class__.__name__}: Marched {distance}m')
        self.__experience += 0.02 * distance

    def __init__(self):
        self.experience = 0


class Knight(Warrior):
    def __init__(self, life=60, experience=0):
        self.__life = life
        self.__experience = experience

    def __repr__(self):
        return f'Knight: hp = {self.__life}, exp = {self.__experience}'

    def march(self, distance):
        print(f'Knight: Marched {distance} m.')
        self.__experience += 0.2 * distance

    def attack(self):
        print("Knight: I've waved my sword.")
        self.__experience += 0.3


class Archer(Warrior):
    def __init__(self, life=40, experience=0):
        self.__life = life
        self.__experience = experience

    def __repr__(self):
        return f'Archer: hp = {self.__life}, exp = {self.__experience}'

    def march(self, distance):
        print(f'Archer: Marched {distance} m.')
        self.__experience += 0.2 * distance

    def attack(self):
        print("Archer: I've released the arrow.")
        self.__experience += 0.4


def main():
    gienek = Knight()
    elza = Archer()
    for warrior in (gienek, elza):
        warrior.march(100)
        warrior.attack()
        print(warrior)
        print('**********')


if __name__ == '__main__':
    main()
