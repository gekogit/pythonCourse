"""
Poproś użytkownika o podanie liczby. Sprawdź czy liczba podana przez użytkownika jest podzielna przez 3 bez reszty
i wyświetl komunikat “Twoja liczba jest podzielna przez 3”.
"""

yourDigit = int(input("Write your number:.."))
print(f'{yourDigit} is 3 divisible. ') if (yourDigit%3 == 0) else print(f'{yourDigit} is not 3 divisible. ')