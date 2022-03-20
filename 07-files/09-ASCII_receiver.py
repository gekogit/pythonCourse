"""
Korzystając z Google dowiedz się więcej o kodowaniu ASCII. Utwórz plik, który tworzy prostą zaszyfrowaną wiadomość.
Każdą literę tekstu zapisuje za pomocą dziesiętnych wartości kodów ASCII. Przykładowo literze A odpowiada numer 65.
Zapoznaj się z metodami ord() oraz char(). Pamiętaj o dodaniu
znaku podziału. Utwórz drugi skrypt, który rozszyfruje wiadomość.
"""
import os


def to_text():
    with open('send.txt', encoding='utf-8') as crypto_file:
        crypto_message = crypto_file.readline()
        for letter in range(0, int(len(crypto_message)), 4):
            print(chr(int(crypto_message[letter:letter+4], 16)), end='')


def clean_up():
    os.remove('send.txt')


#main
print('\nDecoded message:')
to_text()
clean_up()
