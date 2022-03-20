import os


def print_board(board):
    for row in board:
        for col in row:
            print(col, end=" ")
        print()


def put_user1_to_bord(position):
    temp = list(position)
    game_board[int(temp[0]) - 1][int(temp[1]) - 1] = '0'


def put_user2_to_bord(position):
    temp = list(position)
    game_board[int(temp[0]) - 1][int(temp[1]) - 1] = 'X'


def check_free_position(xy):
    temp = list(xy)
    if game_board[int(temp[0]) - 1][int(temp[1]) - 1] == '-':
        return True
    else:
        return False


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


game_board_intro = [
 [' ', '1', '2', '3'],
 ['1', '-', '-', '-'],
 ['2', '-', '-', '-'],
 ['3', '-', '-', '-']
 ]

game_board = [
 ['-', '-', '-'],
 ['-', '-', '-'],
 ['-', '-', '-']
 ]

print('\n Circle cross game. Two players. Selection by index (11,12..) ')
print_board(game_board_intro)

user1_name = input('Write first player name:')
user2_name = input('Write second player name:')

print_board(game_board)
while True:
    user1 = input(f'{user1_name} put 0 in position:..')
    print()
    if check_free_position(user1):
        put_user1_to_bord(user1)
        print_board(game_board)
        if sign_win('0'):
            print(f'{user1_name} WIN')
            break
    else:
        print('Place already used, you miss your chance!')
    user2 = input(f'{user2_name} put X in position:..')
    print()
    if check_free_position(user2):
        put_user2_to_bord(user2)
        print_board(game_board)
        if sign_win('X'):
            print(f'{user2_name} WIN')
            break
    else:
        print('Place already used, you miss your chance!')

    if draw():
        print('DRAW')
        break


