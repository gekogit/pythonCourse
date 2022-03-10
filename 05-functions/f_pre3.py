"""
Napisać funkcję, która przyjmuje listę liczb i zwraca sumę wszystki elementów na liście.
"""


def sumListEl(temp):
    sum = 0
    for el in temp:
        sum += el
    return sum


userList = [1, 2, 4, 5]
print(userList)
print('Sum of the list is:', sum(userList))
