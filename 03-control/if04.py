"""
Utwórz zmienną przechowującą dowolny ciąg znaków. Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy
zawiera literę a. Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.
"""
txt = "sdagfsjklfasd"
print("My string:", txt)
print("String length > 5") if len(txt) > 5 else print("String length > 5")
if txt.rfind('a') > 0:
    print("String contains 'a'")
    print(f'a replaced by z: {txt.replace("a", "z")}')
