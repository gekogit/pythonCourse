"""
Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych.
Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).
"""
txt = input("\nWrite some text:...")
print("Every second signs:\nUsing 'for'....")
for i in range(1, len(txt), 2):
    print(f'{txt[i]}', end="")
print(f'\nUsing slicing...\n{txt[1::2]}')
