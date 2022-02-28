"""
1.Czy 23 + 3 będzie się równać 15 + 12 ?
2.Czy dzielenie 29 przez 7 bez reszty wynosi 5?
3.Czy 27 podzielone przez 8 daje resztę 3?
4.Wyświetl True, jeżeli liczba jest parzysta.
5.Czy 43 - 13 będzie się równać 11 + 12 ?
6.Czy dzielenie 129 przez 17 bez reszty wynosi 3?
7.Czy 247 podzielone przez 5 daje resztę 2?
"""

print()
print(f'1:{(23+3) == (15+12)}')
print(f'2:{(29//7) == 5}')
print(f'3:{(27 % 8) == 3}')
number = int(input("Write some number:.."))
print(f'4:{(number % 2) == 0}')
print(f'5:{(43-13) == (11+12)}')
print(f'6:{129/17 == 3}')
print(f'7:{247 % 5 == 2}')
