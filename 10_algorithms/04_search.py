"""
4▹ Napisz funkcję przeszukiwania połówkowego (binarenego), która przyjmuje dwa parametry - szukany element oraz listę
 elementów. Zwraca informację czy element jest obecny na liście, albo nie.

Wejście:

data = [3, 15, 45, 2, 6, 12, 44, 34, 21, 56, 7, 3, 12]
elem = 21
Wyjście:

“Number 21 is on the list”
"""


def take_numbers():
    while True:
        try:
            x = int(input('Check number in the list:'))
            break
        except Exception:
            print('Wrong number')
    return x


class Node:
    def __init__(self, value):
        self.value = value



def main():
    data = [3, 15, 45, 2, 6, 12, 44, 34, 21, 56, 7, 3, 12]
    print('Binary searching.')
    print("List :", data)
    root = Node(data[0])
    if data[1] > data[0]:
        root.right = Node(data[1])
    else:
        root.left = Node(data[1])


if __name__ == '__main__':
    main()
