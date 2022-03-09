"""Utwórz listę lub krotkę tuples_to_dict zawierającą krotki 2 elementowe.
 Przekształć ją w słownik dict_from_tuples."""

twoT = (("one", 1), ("two", 2))
print(twoT)
dictFromT = dict(twoT)
print(dictFromT)
for k, v in dictFromT.items():
    print(k, "--->", v)
