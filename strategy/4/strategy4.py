from knight import Knight
from archer import Archer


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
