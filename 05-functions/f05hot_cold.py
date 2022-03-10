"""
Napisz grę ciepło - zimno tak, aby korzystać z funkcji.
"""
import random


def generate_numer(num):
    number = random.randrange(0, num)
    return number


user = 0
steps = 6
print("\nGame - guess number 0-100 max in 6 steps!")
computer = generate_numer(100)
for i in range(steps):
    print(f'Attempt {i + 1}. ', end="")
    user = int(input("Type your number:.."))
    if user == computer:
        print("You win!")
        break
    else:
        print("Hot") if user < computer else print("Cold")
    if i == 5:
        print("You lose.")
