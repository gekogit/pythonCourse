"""
Hangman Computer random word comes from list. On the screen comes shadowed ( ----).
User can guess whole word or gives a letter. If letter is in the word show up with the comment “ Letter in the word”
if not “Not in the word”. After certain attempts game finished.
"""
import random


def word_random():
    words_base = ['Sarah', 'Anna', 'Julia', 'Laura', 'Lena', 'Hannah', 'Lisa', 'Katharina', 'Leonie', 'Vanessa']
    return words_base[random.randrange(0, len(words_base))]


repeat_number = 10

computer_words = word_random()
print('for those who likes to cheat:', computer_words)
user_shadow_word = '-' * len(computer_words)
print('\n\n\nGuess the word (ps.cap letter sensitive, max 10 attempts):')
print(user_shadow_word)
for n in range(repeat_number):
    user_letter = input('Your letter:')
    if user_letter == computer_words:
        print('Well done')
        break
    letter_in_word = False
    for letter_index in range(len(computer_words)):
        if computer_words[letter_index] == user_letter:
            user_shadow_word = user_shadow_word[:letter_index] + user_letter + user_shadow_word[letter_index + 1:]
            letter_in_word = True
    if letter_in_word:
        print(f'Bravo {user_letter} is in the word.')
    print(user_shadow_word)
    if user_shadow_word == computer_words:
        print('Well done')
        break
    if n+1 == repeat_number:
        print('Ups... Try again next time.')
