"""
Do zmiennej quote przypisz zdanie:
„Honesty is the first chapter in the book of wisdom.”, a następnie:
Policz wszystkie znaki w napisie
Nie modyfikując zmiennej wyświetl słowo wisdom
Wyświetl tylko pierwszą połowę tekstu
Wyświetl tylko kropkę
Wyświetl od połowy tylko co trzecią literę cytatu
Wyświetl ‘Hnsyi h is hpe ntebo fwso.’
Wyświetl cały cytat odwrotnie
Zamień wisdom na słowo friendship
"""
quote = "Honesty is the first chapter in the book of wisdom."
print(f'\nString: {quote}')
print(f'Length:{len(quote)}')
print(f'print wisdom: {quote[-7:-1]}')
print(f'first half: {quote[:(len(quote))//2]}')
print(f'point: {quote[len(quote)-1]}')
print(f'second half with step 3: {quote[len(quote)//2-1::3]}')
print(f'print Hnsyi h is hpe ntebo fwso. :{quote[::2]}')
print(f'reversed: {"".join(reversed(quote))}')
"""
print("reverse: ", end='')
for i in range(1, len(quote)+1):
    print(quote[-i], end='')
"""
print(f'\nreplace wisdom to friendship: {quote.replace("wisdom","friendship")}')
