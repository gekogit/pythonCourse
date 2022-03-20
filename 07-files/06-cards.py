"""
 Rozpoznawanie kart. Utwórz plik zawierający numery kart kredytowych. Sprawdź dla każdej kart jej
typ. Podziel kart do plików wg typów np. visa.txt, mastercard.txt, americanexpress.txt.
"""
import os


def is_visa(card):
    card_list = list(card)
    first_dig = card_list[0]
    if (len(card_list) == 16 or len(card_list) == 13) and int(first_dig) == 4:
        return True
    else:
        return False


def is_master(card):
    two_firs_nb = card[:2]
    four_first_nb = card[:4]
    if len(card) == 16 and (51 <= int(two_firs_nb) <= 55 or 2221 <= int(four_first_nb) <= 2720):
        return True
    else:
        return False


def is_american(card):
    two_firs_nb = card[:2]
    if len(card) == 15 and 34 <= int(two_firs_nb) <= 37:
        return True
    else:
        return False


def load_from_file(filename):
    with open(filename) as f:
        all_lines = f.readlines()
        for x in range(len(all_lines)):
            all_lines[x] = all_lines[x].rstrip()
    return all_lines


def add_to_card_file(new_nb, filename):
    with open(filename, 'a') as temp_file:
        temp_file.write(new_nb)
        temp_file.write('\n')


def sort_and_save(cont):
    for el in cont:
        if is_visa(el):
            add_to_card_file(el, 'visa.txt')
        elif is_master(el):
            add_to_card_file(el, 'master.txt')
        elif is_american(el):
            add_to_card_file(el, 'american.txt')
        else:
            print(f'Card number {el} is not; visa,master,american')


def clean_up():
    os.remove('visa.txt')
    os.remove('master.txt')
    os.remove('american.txt')


#main
card_container = load_from_file('cards_list.txt')
sort_and_save(card_container)
input("\nThe job is done. Check files, press enter to clean up. ")
clean_up()
