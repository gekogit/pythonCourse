"""
Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej np.: Kobyła ma mały bok.
Pozwól użytkownikowi wprowadzić dowolne zdanie. Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.
"""
polindrome = input("Type polindrome:...")
polindrome = polindrome.lower().replace(' ', '')
reversedString = ''.join(reversed(polindrome))
print(f'Is right polindrome? {polindrome == reversedString}')

