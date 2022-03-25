"""
 Stwórz listę 10 elementową (różne typy!). Pozwól użytkownikowi podać dowolny index.
  Podziel 1 przez liczbę pod indexem wybranym przez użytkownika. Obsłuż błędy.
"""
import sys

my_list = [13, 'zoo', 3.45, 0, True, range(10), (2, 3), {'key': 122}]
print('Result = 1/List[user id]')
while True:
    print("List; ", my_list)
    try:
        user_id = int(input("Your id:"))
        result = 1 / my_list[user_id]
        print(f'{result}')
    except (TypeError, ZeroDivisionError):
        print('Error , try again')
    except (ValueError, IndexError):
        print('Wrong value, index')
