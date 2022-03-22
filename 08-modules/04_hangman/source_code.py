"""
4▹ Zmodyfikuj swoją grę wisielec tak, aby w dowolny uzasadniony sposób wykorzystać moduł lub moduły.
"""

import random


def word_random(words_list):
    return words_list[random.randrange(0, len(words_list))]


def init_game(word):
    print('for those who likes to cheat:', word)
    shadow_word = '-' * len(word)
    print('\n\n\nGuess the word (ps.cap letter sensitive):')
    print(shadow_word)
    return shadow_word


def play_hangman(rep_nb, comp_word):
    sh_word = init_game(comp_word)
    for n in range(rep_nb):
        user_letter = input('Your letter:')
        if user_letter == comp_word:
            print('Well done')
            break
        letter_in_word = False
        for letter_index in range(len(comp_word)):
            if comp_word[letter_index] == user_letter:
                sh_word = sh_word[:letter_index] + user_letter + sh_word[letter_index + 1:]
                letter_in_word = True
        if letter_in_word:
            print(f'Bravo {user_letter} is in the word.')
        print(sh_word)
        if sh_word == comp_word:
            print('Well done')
            break
        if n + 1 == rep_nb:
            print('Ups... Try again next time.')


def main():
    repeat_number = 10
    words_base = ['Sarah', 'Anna', 'Julia', 'Laura', 'Lena', 'Hannah', 'Lisa', 'Katharina', 'Leonie', 'Vanessa']
    computer_word = word_random(words_base)
    play_hangman(repeat_number, computer_word)


if __name__ == '__main__':
    main()

