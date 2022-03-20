"""
Utwórz generator dowolnego typu np. generator zdań, tweetów czy konferencji. Dane wejściowe
pobierz z pliku csv (plik csv możesz traktować jako plik txt ze znanym znakiem podziału), który będzie
przechowywał dane potrzebne do generowania.
Przykład z generatora konferencji: http://generatorkonferencji.pl (niektóre potrafią wyjść zabawne).
Wygenerujcie kilka. Czy widzicie wzorzec?
Przykład generatora cytatów: http://wisdomofchopra.com/ (Można wykorzystać istniejące dane wejściowe json, lub przepisać na własny format danych).

"""
import json
import random


def json_to_dict():
    with open('words_source.json') as temp_dict:
        words_base = json.load(temp_dict)
    return words_base

#main
my_dict = json_to_dict()
print('\nSentence generator:\n')
for x in range(3):
    for el in my_dict['pattern']:
        print(random.choice(my_dict[el]), end=' ')
    print()
