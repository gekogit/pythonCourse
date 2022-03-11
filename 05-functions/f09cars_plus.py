"""
Kolejnym warunkiem, aby dostać “żółte tablice”, jest to, aby samochód posiadał co najmniej 75% oryginalnych części.
W naszym zadaniu zakładamy, że rzeczoznawca określił jego oryginalność w kategorii tak/nie.
Poniżej stworzenia i wyświetlenia słownika w zadaniu powyżej (f09):
dopisz do słownika nowy klucz czy_oryginalny i ustaw jego wartość (typ: bool) wedle uznania.
            ponownie wyświetl zmieniony słownik
    Zmodyfikuj program tak, aby uwzględnił decyzję o możliwości zarejestrowania samochodu również od jego oryginalności.
     Dopisz odpowiednie komunikaty.
"""
"""
Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.
Program zacznie ze stworzonym słownikiem o trzech kluczach:
            marka (str)
            model (str)
            rocznik (int)
Wypisze ten słownik na ekran (bez żadnego formatowania)
Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat:
“Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”
 Jeśli nie spełnia powyższego warunku, wypisze komunikat:
 “Twój samochód (tutaj_marka) jest jeszcze zbyt młody.”
    Gdy program będzie poprawnie działał, pozmieniaj wartości słownika (ale nie klucze!), aby zobaczyć, czy progam również zmienia swoje zachowanie.
"""


def print_dict(dictionary):
    print(dictionary)


today_year = 2022
car_dict = {
    'brand': 'Audi',
    'model': 'A4',
    'year': 1990
}

car_dict['original_parts'] = True
print()
print_dict(car_dict)
if (today_year - car_dict['year']) > 25 and car_dict['original_parts'] is True:
    print('Your car', car_dict['brand'], 'can be on yellow plates.')
else:
    print('Your car', car_dict['brand'], 'can not be on yellow plates.')
