"""
 Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą, MasterCard, a może AmericanExpress.
Co wiemy o tych numerach tych kart?
    All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
    MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720.
     All have 16 digits.
    American Express card numbers start with 34 or 37 and have 15 digits.
"""


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


user_card = input('Write your card number: ')
print(f'Your card:\n- is Visa: {is_visa(user_card)}\n- is MasterCard:{is_master(user_card)}\n-is American Express:\
{is_american(user_card)}')
