"""
 W podanym przez użytkownika ciągu wejściowym policz wszystkie małe litery, wielkie litery, cyfry i znaki specjalne.
"""
txt = input("\nWrite some text:...")
lowLettersNumber = 0
upperLettersNumber = 0
digitsNumber = 0
extraLettersNumber = 0
for letter in txt:
    if letter.islower():
        lowLettersNumber += 1
    elif letter.isupper():
        upperLettersNumber += 1
    elif letter.isdigit():
        digitsNumber += 1
    elif not letter.isalnum():
        extraLettersNumber += 1

print(f'Number of lower letters: {lowLettersNumber}')
print(f'Number of upper letters: {upperLettersNumber}')
print(f'Number of digits: {digitsNumber}')
print(f'Number of extra signs: {extraLettersNumber}')

