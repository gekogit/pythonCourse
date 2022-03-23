"""
Zmodyfikuj generator tak, by oczekiwał znaków podanych przez użytkownika np. użytkownik podaje 4 znaki:
 ‘a’, ‘b’, ‘c’, ‘*’.
"""
import random
import seq_finder


def make_random_text_contain_0_9(length, user_signs):
    text = ''
    for x in range(random.randrange(2, length)):
        text += user_signs[random.randrange(0, len(user_signs))]
    return text


def isseq_min2(txt):
    winners = seq_finder.finder_seq(list(txt))
    winner = seq_finder.dict_max_value(winners)
    return winner[1] > 1


def user_input_signs():
    user_txt = input("Write your signs: ")
    user_txt = user_txt.replace(" ", '')
    user_txt = user_txt.replace(",", '')
    return list(user_txt)


def gen_form_user():
    max_word_length = 50
    test_text = make_random_text_contain_0_9(max_word_length, user_input_signs())
    while not isseq_min2(test_text):
        test_text = make_random_text_contain_0_9(max_word_length)
    return test_text


def main():
    max_word_length = 50
    test_text = make_random_text_contain_0_9(max_word_length, user_input_signs())
    while not isseq_min2(test_text):
        test_text = make_random_text_contain_0_9(max_word_length)
    print(test_text)


if __name__ == '__main__':
    main()

