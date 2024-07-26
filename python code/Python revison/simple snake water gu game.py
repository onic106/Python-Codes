import random

print("Snake - Water - Gun")
n = int(input("Enter the number of rounds: "))
options = ['s', 'w', 'g']
rounds = 1
comp_win = 0
user_win = 0

while rounds <= n:
    print(f"Round {rounds}:\nSnake - 's'\nWater - 'w'\nGun - 'g'")
    try:
        player = input("Choose your option: ")
    except EOFError as e:
        print(e)
        continue

    if player not in options:
        print("Invalid input, try again.\n")
        continue

    computer = random.choice(options)

    if computer == 's':
        if player == 'w':
            comp_win += 1
        elif player == 'g':
            user_win += 1
    elif computer == 'w':
        if player == 'g':
            comp_win += 1
        elif player == 's':
            user_win += 1
    elif computer == 'g':
        if player == 's':
            comp_win += 1
        elif player == 'w':
            user_win += 1

    rounds += 1

if user_win > comp_win:
    print("Congratulations! You won.")
elif comp_win > user_win:
    print("Computer won.")
else:
    print("It's a draw!")


