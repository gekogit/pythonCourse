listToDict = [["one", 1], ["two", 2]]
dictFromList = dict(listToDict)
print(dictFromList)
for k, v in dictFromList.items():
    print(k, "--->", v)
