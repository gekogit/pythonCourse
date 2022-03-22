"""
Stwórz program, który dla dowolnego ciągu znajduje najdłuższą sekwencję takich samych znaków oraz jej długość np.
Wejście:
var = ‘banannnnannnnnnnnnanananananaaaana’
Wyjście
‘nnnnnnnnn’, 9
"""


def print_intro():
    print('Input string. Program is finding the longest sequence.')


def take_input():
    txt = input("Write some text:.")
    to_list = list(txt)
    return to_list


def finder_seq(data_list):
    letter_nb = 0
    for letter in data_list:
        print()


def main():
    print_intro()
    data = take_input()
    print(data)


if __name__ == '__main__':
    main()
