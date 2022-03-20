"""
Cards war game: Traditional rules. Two players. Random cards for each player in the beginning.
After battle cards are coming back to the winner. Checking hazard rules after certain number of games.
"""

import random
import statistics


def shuffle_cards(input_cards):
    random.shuffle(input_cards)
    return input_cards


def replace_card_nb_to_fig(power):
    match power:
        case 11:
            return "Jack"
        case 12:
            return "Queen"
        case 13:
            return "King"
        case 14:
            return "Ace"
        case _:
            return power


def print_battle(user1name, user1, user2name, user2):
    if user1 > 10:
        user1 = replace_card_nb_to_fig(user1)
    if user2 > 10:
        user2 = replace_card_nb_to_fig(user2)
    print(f'{user1name}: {user1} <-----> {user2} :{user2name}')


decks = 4
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print('\nCards war game. Two players.')
user1_name = input('Write first player name:')
user2_name = input('Write second player name:')
print()

games = int(input('How many games do you want to watch?:'))
auto_game = input('Auto game of round by round? Type a for auto, m for manual:')

user1_win_games_counter = 0
user2_win_games_counter = 0
draw_counter = 0
games_mean_rounds = []
for game in range(games):
    game_round = 1
    deck_of_cards = cards * decks
    deck_of_cards_shuffled = shuffle_cards(deck_of_cards)

    user1_cards = deck_of_cards_shuffled[::2]
    user2_cards = deck_of_cards_shuffled[1::2]

    user1_win_game_counter = 0
    user2_win_game_counter = 0

    while len(user1_cards) > 0 and len(user2_cards) > 0:
        #    print(user1_cards)
        #    print(user2_cards)
        print('\nRound: ', game_round)
        print_battle(user1_name, user1_cards[0], user2_name, user2_cards[0])

        if user1_cards[0] > user2_cards[0]:
            user1_win_game_counter += 1
            user1_cards.append(user2_cards.pop(0))
            user1_cards.append(user1_cards.pop(0))
            print(f'{user1_name} won the battle.')

        elif user2_cards[0] > user1_cards[0]:
            user2_win_game_counter += 1
            user2_cards.append(user1_cards.pop(0))
            user2_cards.append(user2_cards.pop(0))
            print(f'{user2_name} won the battle.')

        elif user2_cards[0] == user1_cards[0]:
            war_end = False
            war_treasure = []
            while not war_end:
                print("WAR!")
                for give in range(2):
                    if len(user1_cards) > 1:
                        print('*', end='')
                        war_treasure.append(user1_cards.pop(0))
                    if len(user2_cards) > 1:
                        print('*', end='')
                        war_treasure.append(user2_cards.pop(0))
                print()
                print_battle(user1_name, user1_cards[0], user2_name, user2_cards[0])
                if user1_cards[0] > user2_cards[0]:
                    user1_win_game_counter += 1
                    war_end = True
                    print(f'{user1_name} WON the WAR')
                    print(f'War treasure:')
                    for el in range(len(war_treasure)):
                        print(str(replace_card_nb_to_fig(war_treasure[0])), end=' ')
                        user1_cards.append(war_treasure.pop(0))

                elif user2_cards[0] > user1_cards[0]:
                    user2_win_game_counter += 1
                    war_end = True
                    print(f'{user2_name} WON the WAR')
                    print(f'War treasure:')
                    for el in range(len(war_treasure)):
                        print(str(replace_card_nb_to_fig(war_treasure[0])), end=' ')
                        user2_cards.append(war_treasure.pop(0))
                elif len(user1_cards) == 1 and len(user2_cards) == 1 and user2_cards[0] == user1_cards[0]:
                    print('DRAW')
                    draw_counter += 1
                    war_end = True

        game_round += 1
        if auto_game == 'm':
            print(f'Next round press enter. ')
            input()

    if draw_counter > 0:
        print('\nEND GAME DRAW!')
    elif len(user1_cards) == 0:
        print(f'\nEND GAME {user2_name} WON!')
        user1_win_games_counter += 1

    elif len(user2_cards) == 0:
        print(f'\nEND GAME {user1_name} WON!')
        user2_win_games_counter += 1

    print(f'\nGame nb. {game +1} statistics: ')
    print('Rounds: ', game_round)
    print(f'{user1_name} wins: {user1_win_game_counter}.')
    print(f'{user2_name} wins: {user2_win_game_counter}.')
    games_mean_rounds.append(game_round)

if games > 1:
    print(f'\nAll games statistics: ')
    print('Mean rounds: ', statistics.mean(games_mean_rounds))
    print(f'{user1_name} wins: {user1_win_games_counter}.')
    print(f'{user2_name} wins: {user2_win_games_counter}.')
    print(f'Draws: {draw_counter}')

