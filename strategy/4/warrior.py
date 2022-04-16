class Warrior:
    def __repr__(self):
        return f'Warrior, {self.__class__.__name__}: hp={self.__life}, exp={self.__experience}'

    def march(self, distance):
        print(f'Warrior, {self.__class__.__name__}: Marched {distance}m')
        self.__experience += 0.02 * distance

    def __init__(self):
        self.experience = 0
