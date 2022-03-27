import os


def print_board(board):
    for row in board:
        for col in row:
            print(col, end=" ")
        print()


def put_to_bord(position, sign):
    game_board[position[0] - 1][position[1] - 1] = sign


def check_free_position(xy):
    return game_board[xy[0] - 1][xy[1] - 1] == '-'


def sign_win(sign):
    col = []
    dia1 = []
    dia2 = []
    for row in game_board:
        if row.count(sign) == 3:
            return True

    for x in range(3):
        col += game_board[x][0]
        dia1 += game_board[x][x]
        dia2 += game_board[2 - x][x]
    if col.count(sign) == 3 or dia1.count(sign) == 3 or dia2.count(sign) == 3:
        return True


def draw():
    full_table = True
    for row in game_board:
        for col in row:
            if col == '-':
                full_table = False
    return full_table


def take_names():
    name1 = input('Write first player name:')
    name2 = input('Write second player name:')
    return name1, name2


def pars_letter(letter):
    match letter:
        case 'A':
            return 1
        case 'a':
            return 1
        case 'B':
            return 2
        case 'b':
            return 2
        case 'C':
            return 3
        case 'c':
            return 3
        case _:
            return letter


def take_user_choice(name, sign):
    while True:
        user_choice = input(f'{name} puts {sign} in position:..')
        user_choice = user_choice.replace(',', '')
        user_choice = user_choice.replace(' ', '')
        user_choice = user_choice.replace('.', '')
        user_choice = list(user_choice)
        try:
            if len(user_choice) == 2:

                user_int = [int(user_choice[0]), pars_letter(user_choice[1])]
                if(user_int[0] in range(1, 4)) and (user_int[1] in range(1, 4)):
                    break
            print("Bord position; not recognised.")
        except ValueError:
            print("Bord position; not recognised.")
    return user_int


def log_game(data):
    with open('game_log.txt', 'a') as f:
        f.write(data)


game_board_intro = [
 [' ', 'A', 'B', 'C'],
 ['1', '-', '-', '-'],
 ['2', '-', '-', '-'],
 ['3', '-', '-', '-']
 ]

game_board = [
 ['-', '-', '-'],
 ['-', '-', '-'],
 ['-', '-', '-']
 ]


def main():
    print('\n Circle cross game. Two players. Selection by index (11,12..) ')
    print_board(game_board_intro)
    user1_name, user2_name = take_names()
    print_board(game_board)

    while True:
        user1 = take_user_choice(user1_name, 'O')
        print()
        if check_free_position(user1):
            put_to_bord(user1, 'O')
            print_board(game_board)
            if sign_win('O'):
                print(f'{user1_name} WIN')
                log_game(f'{user1_name} WON against {user2_name}\n')
                break
        else:
            print('Place already used, you miss your chance!')
        user2 = take_user_choice(user2_name, "X")
        print()
        if check_free_position(user2):
            put_to_bord(user2, 'X')
            print_board(game_board)
            if sign_win('X'):
                print(f'{user2_name} WIN')
                log_game(f'{user2_name} WON against {user1_name}\n')
                break
        else:
            print('Place already used, you miss your chance!')

        if draw():
            print('DRAW')
            log_game(" DRAW\n")
            break


if __name__ == "__main__":
    main()
