"""
7▹ Wróć do pierwszego zadania z lekcji o plikach, zmodyfikuj go tak, aby to użytkownik podawał nazwę pliku z cytatami.
 Pamiętaj, by użytkownik po wykonaniu błędnej akcji (np. literówki w nazwie pliku) miał możliwość poprawić swój błąd.
"""
import random
#cytaty.txt


def print_out(quote):
    width = len(quote[0]) * 2
    print('Quote of the day: \n')
    print(width * '*')
    print(quote[0].center(width))
    print(quote[1].rjust(width))
    print(width * '*')


def day_thought(content):
    day_quotes = random.choice(content).strip()
    day_quotes = day_quotes.split('Autor:')
    return day_quotes


def user_quote_file_name():
    while True:
        try:
            file_name = input('Type file name to open quotes (cytaty.txt):')
            with open(file_name, encoding='utf-8') as f:
                text = f.readlines()
            break
        except FileNotFoundError:
            print("Wrong file name.")
    return text


def main():
    txt = user_quote_file_name()
    quote = day_thought(txt)
    print_out(quote)


if __name__ == '__main__':
    main()
