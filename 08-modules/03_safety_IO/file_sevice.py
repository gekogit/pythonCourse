"""
 Stwórz moduł, który zajmuje się jedynie otwieraniem plików - oferuje bezpieczny sposób odczytu oraz bezpieczny zapis.
Funkcja czytająca pliki sprawdza najpierw czy dany plik istnieje oraz czy jest niepusty.
Funkcja zapisująca do pliku chroni przed nadpisaniem istniejącego pliku.
"""
import os


def read_file(filename):
    if os.path.exists(filename):
        if os.path.getsize(filename) > 0:
            with open(filename) as f:
                content = f.read()
                return content
    else:
        print(f'Can not read from {filename}.')


def write_file(filename, data):
    if os.path.exists(filename):
        print("File already exist/not empty!")
    else:
        with open(filename, 'w') as f:
            f.write(data)
