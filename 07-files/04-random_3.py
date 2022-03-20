"""
 Wyświetl 3 losowe cytaty
"""

import random
filename = 'cytaty.txt'


def print_out(quote):
    width = len(quote[0]) * 2
    print('\n\nQuote: \n')
    print(width * '*')
    print(quote[0].center(width))
    print(quote[1].rjust(width))
    print(width * '*')


def day_thought(file):
    with open(file, encoding='utf-8') as f:
        content = f.readlines()
        day_quotes = random.choice(content).strip()
        day_quotes = day_quotes.split('Autor:')
    print_out(day_quotes)


#main
for x in range(3):
    day_thought(filename)

