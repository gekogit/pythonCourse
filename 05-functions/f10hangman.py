"""
Stwórz grę wisielec “bez wisielca”.
    Komputer losuje wyraz z dostępnej w programie listy wyrazów.
    Wyświetla zamaskowany wyraz z widoczną liczbą znaków (np. ‘- - - - - - -‘)
    Użykownik podaje literę.
    Sprawdź, czy litera istnieje w wyrazie. Jeśli tak, wyświetl mu komunikat:
            “Trafione!” oraz napis ze znanymi literami.
    W przeciwnym wpadku pokaż komunikat:
            “Nie trafione, spróbuj jeszcze raz!”.
    Możesz ograniczyć liczbę prób do np. 10.
"""
import random

def word_random():
    words_base = ['Sarah', 'Anna', 'Julia', 'Laura', 'Lena', 'Hannah', 'Lisa', 'Katharina', 'Leonie', 'Vanessa']
    return words_base[random.randrange(0, len(words_base))]

def print_blanks(word):
    return '-'*len(word)


repeat_number = 5
for n in range(repeat_number):
    computer_words = word_random()
    user_shadow_words = '-' * len(computer_words)
    print(computer_words)
    print(user_shadow_words)
    print('Words to guess: ', print_blanks(computer_words))
    user_letter = input('Type your letter or whole word:')
    if user_letter == computer_words:
        print('Well done')
        break
    for letter_index in range(len(computer_words)):
        if computer_words[letter_index] == user_letter:
            user_shadow_words[letter_index] = user_letter
    print(user_shadow_words)

    if n == repeat_number:
        print('Ups... Try again next time.')