"""
Wywołaj błąd związany z otwarciem pliku.

Spróbuj odczytać plik, który nie istnieje.
Spróbuj odczytać wartość z pliku otwartym w trybie w
Spróbuj utworzyć plik, który już istnieje w trybie x
"""
import io
import os


def show_file_error():
    try:
        with open('blue.txt') as test:
            print(test.read())
    except FileNotFoundError as e:
        print(e)


def open_ghost():
    try:
        with open('blue.txt') as test:
            print(test.read())
    except FileNotFoundError as error:
        print(error, 'Empty file will be created instead.')
        f = open('blue.txt', 'w+')
        f.close()


def open_file_w():
    try:
        with open('blue.txt', 'w') as test:
            print(test.read())
    except io.UnsupportedOperation:
        print("Can not read this file (write attribute)")


def open_file_x():
    try:
        with open('blue.txt', 'x') as test:
            print(test.read())
    except FileExistsError:
        print("Can not read this file (creation attribute)")


def main():
    print("Exercises 6:")
    show_file_error()
    open_ghost()
    open_file_w()
    open_file_x()
    clean_up()


def clean_up():
    os.remove('blue.txt')


if __name__ == '__main__':
    main()


