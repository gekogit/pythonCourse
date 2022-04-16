from units.knight import Knight
from units.archer import Archer


def main():
    knights_army = []
    for knight in range(4):
        knights_army.append(Knight())
    knights_army.append(Knight())
    for warrior in knights_army:
        warrior.march(2000)
        warrior.attack()
        print(warrior)
        print('**********')


if __name__ == '__main__':
    main()
