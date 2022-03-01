"""
Stwórz zmienną password. Hasło powinno składać z liter i cyfr,
zwierać conajmniej 1 dużą literę i mieć długość conajmniej 8 znaków.
Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne. Wyświetl różne komunikaty w zależności od rodzaju błędu.
"""
password = input("Write password:..")
if len(password) < 8:
    print("Your password is too short.")
elif password.isalpha() or password.isdigit():
    print("Please use combination of digit and letter.")
elif password.islower() or password.isupper():
    print("Please use combination of lower and upper letter.")
elif password.isalnum():
    print("Please use extra signs.")
else:
    print("Your password looks good")
