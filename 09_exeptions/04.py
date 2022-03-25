"""
Oblicz średnią arymetyczną z kilku liczb. Liczby będą podane przez użytkownika po przecinku. Napisz funkcję,
która przyjmie wartości i wyświetli średnią. Program powinen być odporny na błędy użytkownika.
Błędów nie wyświetlaj, ale rodzaj błędu zapisz do pliku.
"""
import statistics


def take_numbers():
    while True:
        try:
            user_txt = input("Write numbers, comma separated:..")
            user_txt = user_txt.replace(" ", '')
            user_list = user_txt.split(',')
            numbers = []
            for el in user_list:
                numbers.append(int(el))
            return numbers
            break
        except ValueError:
            print("Try again more carefully.")


def calculate_mean(data_list):
    return statistics.mean(data_list)


def main():
    print("\nWrite numbers to calculate means.")
    print('Mean = ', round(calculate_mean(take_numbers())))



if __name__ == "__main__":
    main()

