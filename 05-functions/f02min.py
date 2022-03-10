"""
Nie korzystając z funkcji wbudowanej min(), napisz funkcję znajdującą minimalną wartość z 3 liczb. minimum_of(a, b, c).
"""


def min_of(a, b, c):
    min_value = a
    if min_value > b:
        min_value = b
    if min_value > c:
        min_value = c
    return min_value


number1 = 43
number2 = 53
number3 = 76

print(f'\nNb1: {number1} Nb2: {number2} Nb3: {number3}')
print(f'Max is: {min_of(number3, number2, number1)}')
