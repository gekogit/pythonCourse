"""
 Wisielec. Utwórz plik zawierający listę słów wg. kategorii np. zwierzęta, owoce etc. Poproś użytkownika
o podanie kategorii przed rozpoczęciemy gry. Następny wczytaj listę haseł do programu, wylosuj jedno
hasło z listy. Rozgrywka powinna być maksymalnie intuicyjna.

"""
import random


def import_words(cat):
    with open('hangman_words.txt') as words_bank:
        lines = words_bank.readlines()
        for el in lines:
            if el.find(cat) != -1:
                el = el.replace(cat, '')
                el = el.replace(':', '')
                el = el.replace('\n', '')
                el = el.split(',')
                return el


def word_random(words):
    return words[random.randrange(0, len(words))]


def cat_selection():
    selection_flag = False
    while not selection_flag:
        user_choice = input("Type n for names, f for fruits.:")
        match user_choice:
            case 'n':
                selection_flag = True
                return 'names'
            case 'f':
                selection_flag = True
                return 'fruits'
            case _:
                print(f'{user_choice}  - not recognised category.')


def play_game(w):
    repeat_number = 10
    print('for those who likes to cheat:', w)
    user_shadow_word = '-' * len(w)
    print('\n\n\nGuess the word (ps.cap letter sensitive):')
    print(user_shadow_word)
    for n in range(repeat_number):
        user_letter = input('Your letter:')
        if user_letter == w:
            print('Well done, you are MAGIC!')
            break
        letter_in_word = False
        for letter_index in range(len(w)):
            if w[letter_index] == user_letter:
                user_shadow_word = user_shadow_word[:letter_index] + user_letter + user_shadow_word[letter_index + 1:]
                letter_in_word = True
        if letter_in_word:
            print(f'Bravo {user_letter} is in the word.')
        print(user_shadow_word)
        if user_shadow_word == w:
            print('Well done, you are the MASTER.')
            break
        if n+1 == repeat_number:
            print('Ups... Try again next time.')


#main
print('\nHangman game. Two categories: names and fruits. ')
while True:
    words_container = import_words(cat_selection())
    selected_word = word_random(words_container)
    play_game(selected_word)
    if input("Next game? Yes type y, no type n:.") != 'y':
        break

