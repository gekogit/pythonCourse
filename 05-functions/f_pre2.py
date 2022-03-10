"""
Napisać funkcję, która sprawdza czy liczba jest parzysta.
"""


def iseven(x):
    if x%2 == 0:
        return True
    else:
        return False


userNumber = int(input('Write number:..'))
print(f' Your number is even? {iseven(userNumber)}')