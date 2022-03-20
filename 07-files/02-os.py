"""
 Zapoznaj się z modułem os. Sprawdź rozmiar utworzonego przez siebie pliku.
"""
import os


def create_some_file(filename):
    print('\nTemporary file name: ', filename)
    content = 'There is something in the file, but no-one knows what.'
    with open(filename, 'x+') as temp_file:
        print(content, file=temp_file)


def print_file(filename):
    print("\nContent:")
    with open(filename) as temp_file:
        print(temp_file.read())


def print_statistics(filename):
    sts = os.stat(filename)
    print("\nStatistics:\n- file size:", sts.st_size, " bytes.")



def del_file(filename):
    os.remove(filename)


#main
create_some_file('t.txt')
print_file('t.txt')
print_statistics('t.txt')
del_file('t.txt')
