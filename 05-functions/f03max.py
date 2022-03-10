"""
Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c).
"""


def maxOf(a, b, c):
    max = a
    if max < b:
        max = b
    if max < c:
        max = c
    return max


number1 = 43
number2 = 53
number3 = 76

print(f'\nNb1: {number1} Nb2: {number2} Nb3: {number3}')
print(f'Max is: {maxOf(number3, number2, number1)}')