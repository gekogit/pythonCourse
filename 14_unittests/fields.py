"""
5▹ Stwórz moduł obliczający pola różnych figur.
 W nowym pliku utwórz skrypt, który na podstawie podanych składowych kształtów pomieszczeń oraz ich
 wymiarów zwraca powierzchnię budynku.
"""
import math


def triangle(a, h):
    return a*h/2


def square(a):
    return a*a


def wheel(r):
    return math.pi()*r*r


def rectangle(a, b):
    return a*b


def trapezoid(a, b, h):
    return (a+b) * h / 2



