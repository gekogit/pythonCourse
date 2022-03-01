"""
Utwórz listę, która zawiera składniki na ulubione danie. Wyświetl komunikaty co należy pokolei dodać.
Poza pętlą umieść pozostałe instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”.
"""
productsList = ["water", "sugar", "yeast"]
print("\nTo make wodka add to the boiler:")
for product in productsList:
    print("- ", product)
print("Mix, distillate and enjoy... ")
