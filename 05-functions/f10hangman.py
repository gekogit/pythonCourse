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


repeat_number = 10

computer_words = word_random()
print('for those who likes to cheat:', computer_words)
user_shadow_word = '-' * len(computer_words)
print('\n\n\nGuess the word (ps.cap letter sensitive):')
print(user_shadow_word)
for n in range(repeat_number):
    user_letter = input('Your letter:')
    if user_letter == computer_words:
        print('Well done')
        break
    for letter_index in range(len(computer_words)):
        letter_in_word = False
        if computer_words[letter_index] == user_letter:
            user_shadow_word = user_shadow_word[:letter_index] + user_letter + user_shadow_word[letter_index + 1:]
            letter_in_word = True
    if letter_in_word:
        print(f'Bravo {user_letter} is in the word.')
    print(user_shadow_word)
    if user_shadow_word == computer_words:
        print('Well done')
        break
    if n == repeat_number:
        print('Ups... Try again next time.')
