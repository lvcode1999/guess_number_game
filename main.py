import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    i=0
    while guess != random_number:
        i += 1
        guess = int(input(f'Guess a no. between 1 and {x}: '))
        if guess < random_number :
            if guess+6 > random_number:
                print('you\'re close slightly low')
            else:
              print("Sorry, guess again. Too low!")
        elif guess > random_number :
            if guess-6 < random_number:
                print("you're close slightly high")
            else:
                print("Sorry, guess again. Too high!")

    print(f'Yo! You got that right at {i}th attempt.')
    
def computer_guess():
    low = 1
    high = 100
    feedback = ''
    i=0
    while feedback != 3:
        i+=1
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = int(input(f'Is {guess} 1. High \
                          2.low \
                           3.correct'))
        if feedback == 1:
            high = guess-1
        elif feedback == 2:
            low = guess+1
    print('Yay! my sixth sense is so powerful ;)')
    print(f'no. of guesses {i}')

print("1. Guess \
       2. be guessed")
choice = int(input())
if choice == 1:
    guess(100)
elif choice == 2:
   computer_guess()

