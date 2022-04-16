"""
Utwórz dekorator @uppercase_decorator, który przyjmuje dowolną funkcję zawracającą łańcuch znaków i zwracający ten
sam tekst zmieniony na wielkie litery.
"""
def uppercase_decorator(fun):
    def up():
        txt = fun()
        txt = txt.upper()
        return txt

    return up

@uppercase_decorator
def some_function():
    txt = "bleee"
    return txt


print(some_function())



