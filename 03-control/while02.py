"""
Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5).
Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.
"""
secretNum = 5
print("\nGuess secret number (0-20)")
while secretNum != int(input("Type your choice:..")):
    print("Try again.")
print(" You guessed it.")
