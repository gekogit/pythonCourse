"""
Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.
Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.
"""


def min_of(a, b):
    min_value = a
    if min_value > b:
        min_value = b
    return min_value

def max_of(a, b):
    max = a
    if max < b:
        max = b
    return max


def is_in_range(a, b, num):
    if num > min_of(a, b) and num < max_of(a, b):
        print("YES, number is in range")
    else:
        print("NO, out of range")


user_range_from = float(input("Write your range, from:.."))
user_range_to = float(input("Write your range, to:.."))
user_number = float(input("Write your number:.."))

is_in_range(user_range_from, user_range_to, user_number)
