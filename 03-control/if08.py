"""
Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.

"""
numberList = [0, 0, 0]
for i in range(len(numberList)):
    numberList[i] = int(input("Write number:.."))
numberList.sort()
print('\nMaximum number:', max(numberList))
for x in range(1, len(numberList)+1):
    print(numberList[-x], " ", end="")
