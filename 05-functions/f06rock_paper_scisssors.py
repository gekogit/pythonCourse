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
        return user1_name if score == user1_type else user2_name
    if score == 2:
        return user1_name if score == user1_type else user2_name
    if score == 3:
        return user1_name if score == user1_type else user2_name


print('\nRock paper scissors game. 2 Users ')
print("\nType: \n1 --- rock\n2 --- paper\n3 --- scissors")

user1name = input("\nUser 1 name is :")
user2name = input("User 2 name is :")
user1 = int(input(f'\n {user1name} your type is: ')) - 1
user2 = int(input(f' {user2name} your type is: ')) - 1
print('Who won?:', rock_paper_scissors(user1name, user1, user2name, user2))
