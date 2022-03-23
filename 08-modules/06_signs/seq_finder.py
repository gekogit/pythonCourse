"""
Stwórz program, który dla dowolnego ciągu znajduje najdłuższą sekwencję takich samych znaków oraz jej długość np.
Wejście:
var = ‘banannnnannnnnnnnnanananananaaaana’
Wyjście
‘nnnnnnnnn’, 9
"""


def print_intro():
    print('Input string. Program is finding the longest sequence.')


def take_input():
    txt = input("Write some text:.")
    to_list = list(txt)
    return to_list


def finder_seq(data_list):
    prev_letter = data_list[0]
    letter_counter = 1
    winners = {}
    seq_flag = False
    for x in range(1, len(data_list)):
        if prev_letter == data_list[x]:
            letter_counter += 1
            winners[prev_letter] = letter_counter
            seq_flag = True
        else:
            letter_counter = 1
        prev_letter = data_list[x]
    if seq_flag:
        return winners
    else:
        return {"0" : 0}


def dict_max_value(dict_in):
    max_value = max(dict_in.values())
    max_value_key = max(dict_in, key=dict_in.get)
    winner = [max_value_key, max_value]
    return winner


def main():
    print_intro()
    data = take_input()
    sequences = finder_seq(data)
    winner = dict_max_value(sequences)
    print(f'Longest seq {winner[0] * winner[1]} --> {winner[1]} ')


if __name__ == '__main__':
    main()
