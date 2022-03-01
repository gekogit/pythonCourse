"""
Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę. Jeśli suma jest większa niż 100,
wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.
"""
number1 = int(input("Write first number: .."))
number2 = int(input("Write second number: .."))
sumNumbers = number2 + number1
if sumNumbers > 100:
    print("Sum of numbers: ",sumNumbers)
else:
    print("End")
