"""
5 użytkowników poproś o podanie 4 przedmiotów szkolnych, sprawdź czy przedmioty powtarzają się na listach.
 Wyświetl najpopularniejszy przedmiot. (Uwzględnij fakt, że użytkownicy mogą zapisać przedmioty małymi,
drukowanymi lub zaczynając od dużej litery)
"""


userNumber = 5
subjects = 4

print(f'\n{userNumber} users types {subjects} subjects.')

usersSubjects = [[" "] * subjects]* userNumber

for user in range(1, userNumber+1):
    print(f'User {user}')
    for subject in range(1, subjects+1):
        tempString = input("Subject:...")
        tempString = tempString.lower()
        #cap tempString = tempString.
        usersSubjects[user-1][subject-1] = tempString


print(usersSubjects)

