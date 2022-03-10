"""
▹ Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.
"""
n = 10
tempList = []
for x in range(n):
    tempList.append(int(input(f'Write {x+1} number:.. ')))
print('Even numbers from your input:..')
for element in tempList:
    if element % 2 == 0:
        print(element)
