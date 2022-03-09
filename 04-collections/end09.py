"""
5 użytkowników poproś o podanie 4 przedmiotów szkolnych, sprawdź czy przedmioty powtarzają się na listach.
 Wyświetl najpopularniejszy przedmiot. (Uwzględnij fakt, że użytkownicy mogą zapisać przedmioty małymi,
drukowanymi lub zaczynając od dużej litery)
"""
userNumber = 5
subjects = 4

print(f'\nGive info from {userNumber} users about favorite {subjects} subjects.')

usersSubjects = [["-" for x in range(subjects)] for y in range(userNumber)]
allSubList = []

for user in range(1, userNumber+1):
    print(f'User {user}')
    for subject in range(1, subjects+1):
        tempString = input(f'Subject {subject}:...')
        tempString = tempString.lower()
        usersSubjects[user-1][subject-1] = tempString
for user in usersSubjects:
    for subject in user:
        allSubList.append(subject)
subjectDict = {}
for element in allSubList:
    if element in subjectDict:
        subjectDict[element] += 1
    else:
        subjectDict[element] = 1
print("\nSubject highscores:")
for key, value in subjectDict.items():
    print(f' {key} ----- {value}')
if max(subjectDict.values()) > 1:
    keyList = list(subjectDict.keys())
    valList = list(subjectDict.values())
    print("The most popular: ")
    for i in range(len(valList)):
        if valList[i] == max(valList):
            print(keyList[i])
else:
    print("Subjects do not repeat.")
