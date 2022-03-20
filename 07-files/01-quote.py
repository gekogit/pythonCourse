import random
filename = 'C:\\Users\\agrebowiec\Desktop\cytaty.txt'


def print_out(quote):
    width = len(quote[0]) * 2
    print('Quote of the day: \n')
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

def user_quote_file_name():
    print('\nSystem path:C:\\Users\\agrebowiec\Desktop\cytaty.txt')
    user_file = input("Type file name to open quotes:")
    return user_file


day_thought(user_quote_file_name())


