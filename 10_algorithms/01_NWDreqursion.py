"""
1▹ Znajdź największa wspólny dzielnik (NWD) dwóch liczby. Wykorzystaj algorytm Euklidesa.
"""


def take_numbers():
    while True:
        try:
            x = int(input('First number:'))
            y = int(input('Second number:'))
            break
        except Exception:
            print('Wrong number')
    return x, y


def nwd_finder(a, b):
    if a == b:
        return a
    elif a > b:
        return nwd_finder((a-b), b)
    elif b > a:
        return nwd_finder(a, (b - a))


def main():
    print("\nNWD for two int numbers.")
    nb1, nb2 = take_numbers()
    nwd = nwd_finder(nb1, nb2)
    print('NWD = ', nwd)


if __name__ == '__main__':
    main()
