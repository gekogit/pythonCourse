"""
 Napisz grę kamień-papier-nożyce tak, aby korzystać z funkcji.
"""


def rock_paper_scissors(user1_name, user1_type, user2_name, user2_type):
    true_table = [
        [0, 2, 1],
        [2, 0, 3],
        [1, 3, 0]]
    score = true_table[user1_type-1][user2_type-1]
    if score == 0:
        return'Draw'
    if score == 1:
        return user1_name if score == user1_type else user2name
    if score == 2:
        return user1_name if score == user1_type else user2name
    if score == 3:
        return user1_name if score == user1_type else user2name


def pars_letter_to_dig(letter):
    match letter:
        case 'r':
            return 0
        case 'p':
            return 1
        case 's':
            return 2


print('\nRock paper scissors game. 2 Users ')
#print("\nType: \n1 --- rock\n2 --- paper\n3 --- scissors")
print("\nType: \nr --- rock\np --- paper\ns --- scissors")

user1name = input("\nUser 1 name is :")
user2name = input("User 2 name is :")


while True:
    user1 = input(f'\n {user1name} your type is: ')
    user2 = input(f' {user2name} your type is: ')
    print('Who won?:', rock_paper_scissors(user1name, pars_letter_to_dig(user1), user2name, pars_letter_to_dig(user2)))
    print('\nNext game? Press Y')
    if input() != 'y':
        break
