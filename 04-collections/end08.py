"""
Utwórz słownik dla 10 krajów Europy zawierajacy listy 10 najpopularniejszych imion żeńskich.
Zapisz imiona w wersji anglojęzycznej. Dodaj wszystki listy razem. Nowa lista powinna zawierać 100 elementów.
Wyświetl tylko te imiona, które wystąpiły conajmniej w 3 krajach.
"""
popularNames = {'Austria': ['Sarah', 'Anna', 'Julia', 'Laura', 'Lena', 'Hannah', 'Lisa', 'Katharina', 'Leonie', 'Vanessa'],
                'Belgium': ['Emma', 'Marie', 'Laura', 'Julie', 'Sarah', 'Clara', 'Manon', 'Léa', 'Lisa', 'Camille'],
                'France': ['Lea', 'Manon', 'Emma', 'Chloé', 'Camille', 'Océane', 'Clara', 'Marie', 'Sarah', 'Inès'],
                'Italy': ['Giulia', 'Sara', 'Sofia', 'Martina', 'Chiara', 'Alessia', 'Giorgia', 'Aurora', 'Francesca', 'Giada'],
                'Poland': ['Anna', 'Maria', 'Katarzyna', 'Małgorzata', 'Agnieszka', 'Krystyna', 'Barbara', 'Ewa', 'Elżbieta','Zofia'],
                'Hungary': ['Anna', 'Viktória', 'Réka', 'Vivien', 'Zsófia', 'Petra', 'Dorina', 'Fanni', 'Boglárka', 'Eszter'],
                'Norway': ['Emma', 'Thea', 'Ida', 'Sara', 'Julie', 'Emilie', 'Hanna', 'Nora', 'Malin', 'Ingrid'],
                'Sweden': ['Emma','Maja', 'Julia', 'Alice', 'Ida', 'Linnéa', 'Elin', 'Alva', 'Hanna', 'Ella'],
                'Spain': ['Ane', 'Laia', 'June', 'Irati', 'Izaro', 'Nahia', 'Malen', 'Lucia', 'Nora', 'Uxue'],
                'Netherlands': ['Sanne', 'Emma', 'Anna', 'Iris', 'Anouk', 'Melissa', 'Eva', 'Julia', 'Lotte', 'Isa']}

popularNamesList = []
for key, value in popularNames.items():
    popularNamesList += value
print('\nPopular female names in 10 European Countries:\n', popularNamesList)
namesCountsDict = {}
for element in popularNamesList:
    if element in namesCountsDict:
        namesCountsDict[element] += 1
    else:
        namesCountsDict[element] = 1
print("\n Top names (>3):")
for key, value in namesCountsDict.items():
    if value > 3:
        print(f' {key}')


