from warrior import Warrior


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