"""
Utwórz generator instancji testowych, który wygeneruje losowe ciągi znaków składające się z jedynie z cyfr od 0-9.
Upewnij się, że conajmniej 2 takie same znaki znajdą się w sekwencji.
"""
import random
import seq_finder


def make_random_text_contain_0_9(length):
    text = ''
    for x in range(random.randrange(2, length)):
        text += chr(random.randrange(48, 57))
    return text


def isseq_min2(txt):
    winners = seq_finder.finder_seq(list(txt))
    winner = seq_finder.dict_max_value(winners)
    return winner[1] > 1
    

def main():
    max_word_length = 50
    test_text = make_random_text_contain_0_9(max_word_length)
    while not isseq_min2(test_text):
        test_text = make_random_text_contain_0_9(max_word_length)
    print(test_text)



if __name__ == '__main__':
    main()

