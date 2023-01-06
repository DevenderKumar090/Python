import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 to {x}: "))
        if guess < random_number:
            print(' Sorry, guess again. Too Low')
        elif guess > random_number:
            print('Sorry, guess again. Too High')
    print(f'Yay, Congrats. You have guessed the number {random_number} Correctly!!!')
#guess(10)
def  computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback !='c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c low  - high
        feedback = input(f'Is {guess} too high (H), Too low (L), or correct(C)??  ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay, The computer guessed your number, {guess}, Correctly!!!')

computer_guess(10)


