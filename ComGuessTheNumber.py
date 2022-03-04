import random


def computer_guess(x):
    guess = 0
    low = 1
    high = x 
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # "guess = high" could also work b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'{guess} is correct!!')

computer_guess(54)

