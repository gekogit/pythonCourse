import random
computer = random.randrange(0, 100)
user = 0
steps = 6
print("\nGame - guess number 0-100 max in 6 steps!")
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
