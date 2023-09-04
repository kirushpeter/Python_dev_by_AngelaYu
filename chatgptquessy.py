import random

# Define constants for difficulty levels
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    else:
        print(f"You got it! The answer was {answer}")
    return turns - 1

def game():
    print("Welcome to the Number Guessing Game")
    print("I am thinking of a number between 1 and 100")
    
    answer = random.randint(1, 100)
    
    # Set difficulty level
    turns = set_difficulty()
    
    guess = 0
    
    while guess != answer and turns > 0:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
    
    if guess != answer:
        print("Sorry, you've run out of attempts. The correct answer was", answer)
    
game()
