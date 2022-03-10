"""
Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je.
"""
testTuple = ('lion', 'giraffe', 'cat', 'elephant', 'monkey', 'cat', 'dog', 'hamster')
repeat = []
for element in testTuple:
    if testTuple.count(element) > 1:
        repeat.append(element)
print('Repeated elements: ')
for ele in set(repeat):
    print(ele)
