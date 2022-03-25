"""
Utwórz dowolną krotkę zawierającą kilka wartości np. 10.
Pozwól użytkownikowi podać dowolny index oraz wartość. Spróbuj w krotce podmienić wartość na zadanym indeksie.
Obsłuż błąd
"""

test_t = (3, 4, 5, 6, 3, 43, 3432, 43, 2, 32)
print("\nTuple:", test_t)
print('Try to change value.')
while True:
    try:
        user_id = int(input('Your id:'))
        user_val = int(input('Your value:'))
        break
    except ValueError:
        print('Write one more time, more carefully.')
if user_id <= len(test_t):
    try:
        test_t[user_id] = user_val
    except TypeError:
        print('It is tuple, you can not change the value')
    except IndexError:
        print(f'Index is out of range 0-{len(test_t)}')

else:
    print("Index out of range.")