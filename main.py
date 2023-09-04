from random import randint


def check_answer(guess, answer):

    if guess > answer:

        print("too high.")

    elif guess < answer:
        print("too low")

    else:

        print(f"you got it! The answer was {answer}")

    
#make function to set difficulty.


def set_difficulty():

    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if level == "easy":

        




