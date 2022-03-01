"""
Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl
komunikat “gratulacje!”, w przeciwnym razie wyświetl “pudło!”.
"""
myNumber = 50
print("Lucky Man") if myNumber == int(input("Write number 1-100:..")) else print("Try one more time.")
