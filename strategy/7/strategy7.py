from units.knight import Knight
from units.archer import Archer


def main():
    knights_army = []
    archer_army = []
    for knight in range(4):
        knights_army.append(Knight())
    for archer in range(3):
        archer_army.append(Archer())
    army = knights_army + archer_army

    for warrior in army:
        warrior.march(2000)
        warrior.attack()
        print(warrior)
        print('**********')


if __name__ == '__main__':
    main()
