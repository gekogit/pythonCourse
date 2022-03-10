"""
Napisać funkcję, która oblicza pole koła na podstawie zadanego promienia.
"""
import math


def caclCircleField(r):
    return math.pi*r**2


userCircle = int(input('Write circle:..'))
area = round(caclCircleField(userCircle),2)
print('Field = ', area)
