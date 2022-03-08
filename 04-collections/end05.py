poem = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

print("\nPoem:\n",poem)
poem = poem.replace(",", "")
poem = poem.lower()
poemList = poem.split()
countWordsDict = {}
for element in poemList:
    if element in countWordsDict:
        countWordsDict[element] += 1
    else:
        countWordsDict[element] = 1
print("\nCounted words:")
for key, value in countWordsDict.items():
    print(f'{key} -----> {value}')



