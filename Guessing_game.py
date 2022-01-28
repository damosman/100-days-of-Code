from random import randint
from GuessArt import logo

# global variable for number of turns
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

print(logo)

# Checking answers
def check_answer(user_guess, num_guess, turns):

    if user_guess > num_guess:
        print("Too high.Try again")
        return turns - 1
    elif user_guess < num_guess:
        print("Too low.Try again")
        return turns - 1
    else:
        print(f"Congrats!🙂, You are correct, the actual number is {num_guess}")


# set the difficulty
def set_difficulty():
    level = input("Choose difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    # Choose a number
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    num_guess = randint(1, 100)

    # Selected number of turns
    turns = set_difficulty()

    # Repeating a guess if wrong
    user_guess = 0
    while user_guess != num_guess:
        print(f"You have {turns} attempts remaining to guess the number.")
        if turns == 0:
            print("You have run out of guess, You lose.")
            return
        elif user_guess != num_guess:
            print("Guess again.")

        # User Guesses a number
        user_guess = int(input("Make a guess: "))
        turns = check_answer(user_guess, num_guess, turns)

game()