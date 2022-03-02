"""
Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem
(np.jako jeden string rozdzielonych przecinkiem lub białym znakiem). Następnie powitaj każdą osobę na liście.
"""
names = input("Write a few names (separated by comma fg. Anna, Eva):..")
namesList = names.split(", ")
for name in namesList:
    print("Hello ", name)