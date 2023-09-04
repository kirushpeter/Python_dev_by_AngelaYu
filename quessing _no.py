
from random import randint

EASY_LEVEL_TURNS = 10


HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):

    """Checks answer against guess, returns the number of turns remaining"""

    if guess > answer:

        print("Too high.")

        return turns - 1

    elif guess < answer:

        print("Too low")

        return turns - 1

    else:

       print(f"You got it! The answer was {answer}.")

def set_difficulty():

    level = input("Choose a difficulty.Type 'easy' or 'hard': ")

    if level == 'easy':

       return EASY_LEVEL_TURNS

    else:

        return HARD_LEVEL_TURNS


#choosing a random number between 1 and 100
def game():
        
    print("Welcome to the Number Guessing Number")

    print('I am thinking of a number between 1 and 100')

    answer = randint(1, 100)

    print(f"Psst the correct answe is {answer}")

    

    #Make function to set difficulty.

    turns = set_difficulty()

    

    #repeat the guessing functionality if they get it wrong

    guess = 0

    while guess != answer:

        print(f"You have {turns} attempts remaining to guess the number")
    #turns reduce by 1 if they get it wrong.

        guess = int(input("Make a guess: "))

    #Repeat the guessing functionality if they get it wrong.
    
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You have run out of guesses, you lose.")

            return
        
        elif guess != answer:

            print("Guess again.")

game()

