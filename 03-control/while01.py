"""
Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach. Program powinen wykonać się
w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.
C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit
Napisz rozwiązanie zarówno z użyciem pętli while jak i for.
"""
print("\nusing 'while'")
counter = 0
while counter < 201:
    C = round(5/9*(counter-32), 2)
    print(f' F {counter} =  {C} C')
    counter = counter + 20
print("\nusing 'for'")
for deg in range(0, 201, 20):
    C = round(5 / 9 * (deg - 32), 2)
    print(f' F {deg} =  {C} C')
