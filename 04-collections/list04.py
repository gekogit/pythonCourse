"""
 Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.
"""

userList = (input('\nWrite even elements (numbers) space separated: '))
temp = userList.split()
while len(temp) % 2 != 0:
    userList = (input('Write EVEN!!! elements (numbers) space separated: '))
    temp = userList.split()
print(f'Middle left {temp[int((len(temp)/2))-1]}, Middle right {temp[int((len(temp)/2))]}')
