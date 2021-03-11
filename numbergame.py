import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between one and {x}: '))
        if guess < random_number:
            print('Sorry guess again! Too low!')
        elif guess > random_number:
            print('Sorry guess again! Too high!')

    print(f'Yay you did it! The number was indeed{random_number}')
