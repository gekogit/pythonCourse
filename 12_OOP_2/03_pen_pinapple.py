"""
3▹ Zadanie inspirowane popkulturą: https://www.youtube.com/watch?v=Ct6BUPvE2sM

Stwórz klasę PenPinapple, która dziedziczy z klas Pen oraz Pinapple. Logiki to nie ma, więc dodaj wg uznania.
"""


class Pen:
    def __init__(self):
        print("I am a Pen")


class Pinapple:
    def __init__(self):
        print("I am a Pinapple")


class PenPinapple(Pen, Pinapple):
    def __init__(self):
        print("I am a PenPinapple")
        super().__init__()
        super(Pen, self).__init__()


def main():
    p = PenPinapple()


if __name__ == '__main__':
    main()

