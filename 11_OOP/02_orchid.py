"""
2▹ Utwórz klasę dla storczyków. Storczyki z zasady mają różne kolory, pory kwitnienia, gatunki.
Utwórz dowolne atrybuty i metody. Dodaj atrybut wspólny dla wszystkich storczyków - królestwo roślin.
Utwórz kilka storczyków z różnymi parametrami.
"""
import datetime


class Orchid:
    common_type = 'plant'

    def __init__(self, color, flowering_time, genre):
        self.color = color
        self.flowering_time = flowering_time
        self.genre = genre

    def is_flowering_time(self):
        now = datetime.datetime.now()
        print("Today is : ", now.date())
        if now.month == self.flowering_time:
            print(f' Is is flowering time for {self.genre}.')
        else:
            print(f'{self.genre} is not flowering now.')


def main():
    st_in_living_room = Orchid('blue', 5, 'Dendrobium')
    st_in_bed_room = Orchid('white', 7, 'Vanda')
    st_in_kids_room = Orchid('yellow', 7, 'Phalaenopsis')
    st_in_kids_room.is_flowering_time()


if __name__ == '__main__':
    main()
