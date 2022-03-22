"""
Stwórz moduł, który dla dowolnej wartości n, zwróci ciąg fibonnaciego.
"""


def fibbo(n):
    f_numbers = [1, 1]
    for i in range(n-2):
        f_numbers.append(f_numbers[i]+f_numbers[i+1])
    return f_numbers


def print_list_elements(f_list):
    for el in f_list:
        print(el, end=' ')


def take_number():
    nb = int(input("\nType numer to see its Fibonacii string."))
    return nb


def main():
    n = take_number()
    f_numbers = fibbo(n)
    print_list_elements(f_numbers)


if __name__ == '__main__':
    main()
