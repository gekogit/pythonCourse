"""
 Usuń duplikat z podanej list i utwórz na jej bazie krotkę. Znajdź minimalną i maksymalną liczbę w krotce.

 example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]
"""
example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]
exTuple = tuple(set(example_list))
print(f'\nTuple:{exTuple}, max number:{max(exTuple)}, min number:{min(exTuple)}')
