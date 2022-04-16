class Knight:
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


def main():
    gienek = Knight()
    gienek.march(100)
    gienek.attack()
    print(gienek)



if __name__ == '__main__':
    main()
