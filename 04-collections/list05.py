nameList = [
    ['Dorota', 'Wellman','dziennikarka'],
    ['Adam', 'Małysz', 'sportowie'],
    ['Robert', 'Lewandowski', 'piłkarz'],
    ['Krystyna', 'Janda', 'aktorka']
]
for row in nameList:
    for name in row:
        print(name, end=", ")
    print()
