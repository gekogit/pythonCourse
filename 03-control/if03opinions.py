"""
Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce. Oblicz średnią opinię o książce.
W zależności od wyniku dodaj komunikaty. Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.

"""
opinion1 = int(input("Write your opinion (1-10):.."))
opinion2 = int(input("Next:.."))
opinion3 = int(input("Next:.."))

opinionsMean = (opinion1 + opinion2 + opinion3) / 3
if opinionsMean > 7:
    print("Super >7")
elif opinionsMean >= 5:
    print("So So")
else:
    print("Bad")
