import random

def user_guess(x):
    random_num = random.randint(1,x)
    guess = 0
    while guess != random_num:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_num:
            print('Try again, too low')
        elif guess > random_num:
            print('Try again, too high')
    print(f'Woohoo! {random_num} was the right number. ')


def computer_guess(x):
    low = 1
    high = x
    hint = ''
    while hint != 'correct' :
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        guess = random.randint(low, high)
        hint = input(f'Is {guess} too high, too low, or correct? ')

        if hint == 'high':
            high = guess -1

        elif hint == 'low':
            low = guess+1

    print(f'Yay! Number {guess} guessed correctly.')

computer_guess(10)
