"""
 Stwórz krotkę liczb całkowitych. Poproś użytkownika o podanie dowolnej liczby.
 Jeśli liczba znajduje się na krotce wyswietl jej indeks.
"""
realTuple = (1, 2, 3, 5, 8, 10, 15)
print('\nTuple:', realTuple)
userNumber = int(input('\nType your number:...'))
for x in range(len(realTuple)):
    if realTuple[x] == userNumber:
        print('This numer has index: ', x)
print('Your number is not on the list. ')


