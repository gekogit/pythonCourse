"""
Napisać funkcję, która wypisze wszystkie parzyste z przekazanej listy elementów (wykorzystać funkcje z pkt 2)
"""


def iseven(x):
    for el in x:
        if el % 2 == 0:
            print(el)


userList = [1, 2, 4, 5]
print("\nYour list:", userList)
print("Even numbers:")
iseven(userList)
