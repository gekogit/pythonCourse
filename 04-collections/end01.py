"""
Utwórz listę lists_to_dict zawierającą listy 2 elementowe. Przekształć ją w słownik dict_from_list.
"""
listToDict = [["one", 1], ["two", 2]]
dictFromList = dict(listToDict)
print(dictFromList)
for k, v in dictFromList.items():
    print(k, "--->", v)
