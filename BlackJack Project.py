
############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

# This is a Blackjack Game
# To start the game Enter 'y'(yes)

import random
from blackjack_logo import logo


print(logo)
def play_game():
    game_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if game_start == 'y':
      cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
      user = random.sample(cards, 2)
      user_score = user[0] + user[1]
      print(f"Your cards: {user}, current score: {user_score}")
      computer = random.choices(cards, k=2)
      computer_score = computer[0] + computer[1]
      print(f"Computer's first card: {computer[0]}")
      if computer_score == 21:
        print("You went over. You lose 😭")

      card_draw = (input("Type 'y' to get another card, type 'n' to pass: "))
      if card_draw == 'n':
        print(f"Computer cards: {computer}, current score: {computer_score}")
        if user_score > computer_score:
          print("You Win 🙂")
        elif computer_score > user_score:
          print("You lose 😭")
        elif computer_score == user_score:
          print("It's a tie")

      if card_draw == 'y':
        new_user = random.sample(cards, 1)
        new_user = user + new_user
        new_user_score = user_score + new_user[2]
        print(f"Your cards: {new_user}, current score: {new_user_score}")
        new_computer = random.sample(cards, 1)
        new_computer = computer + new_computer
        new_computer_score = computer_score + new_computer[2]
        print(f"Computer's first card: {computer[0]}")
        print(f"Your final hand: {new_user}, final score: {new_user_score}")
        print(f"Computer's final hand: {new_computer}, final score: {new_computer_score}")

        def compare():
          if 21 < new_user_score > new_computer_score :
            return "You went over. You lose 😭"
          elif 21 < new_computer_score > new_user_score:
            return "You Win 🙂"
          elif new_computer_score == new_user_score:
            return "It's a tie"
        compare()

    if game_start == 'n':
      return "Restart Game"
play_game()