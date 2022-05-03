import random

def player_guess(x):
    random_number = random.randint(1, x)
    guess = 0
    print(random_number)
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low')
        elif guess> random_number:
            print('Sorry, guess again. Too high')

    print(f'Yay, congrats. You hav eguessed the number {random_number} correctly')

#player_guess(10)

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:            
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f'Is {guess} toohigh (H), too low (L) or correct (C) ').lower()
        
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f'Yay! The computer has guessed your number, {guess}, correctly')

computer_guess(50)
    