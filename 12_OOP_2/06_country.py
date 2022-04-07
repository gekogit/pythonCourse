"""
6▹ Utworz klasę Kraj, która zawiera informację o powierzchni. ludności, jaki język jest urzędowy,
jakie miasto jest stolicą. Utwórz klika obiektów klasy Kraj, stwórz listę obiektów klasy kraj,
 wyświetl elementy na liście krajów.
"""

class Country:
    def __init__(self,name, area, citizens, language, capital):
        self.name = name
        self.area = area
        self.citizens = citizens
        self. language = language
        self.capital = capital


def print_check(land):
    print(f'\nCountry {land.name} has:\n* area\t\t{land.area}\n* citizens\t{land.citizens}\n* language\t{land.language}'
          f'\n* capital\t{land.capital}')


def main():
    album = [
        Country('Lunaria',     232432, 23,     'lunarianski',  'Luna'),
        Country('Gila',        432,    53265,  'gilianski',    'Alig'),
        Country("Fabilia",      3224,  3,      'elianowy',     'Ailibaf')]
    for country in album:
        print_check(country)


if __name__ == '__main__':
    main()
