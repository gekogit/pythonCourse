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
    'year': 2020
}
print_dict(car_dict)
if (today_year - car_dict['year']) > 25:
    print('Car has more then 25 years.')
else:
    print('Your car', car_dict['brand'], 'is quite young.')
