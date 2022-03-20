"""
Korzystając z Google dowiedz się więcej o kodowaniu ASCII. Utwórz plik, który tworzy prostą zaszyfrowaną wiadomość.
Każdą literę tekstu zapisuje za pomocą dziesiętnych wartości kodów ASCII. Przykładowo literze A odpowiada numer 65.
Zapoznaj się z metodami ord() oraz char(). Pamiętaj o dodaniu
znaku podziału. Utwórz drugi skrypt, który rozszyfruje wiadomość.
"""


def take_massage():
    txt = input('Write you message(without polish signs):')
    return txt


def to_ASCII(sentence):
    for letter in sentence:
        with open("send.txt", 'a', encoding='utf-8') as sender:
            sender.write(hex(ord(letter)))


#main
legacy_message = take_massage()
to_ASCII(legacy_message)
