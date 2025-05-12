import os
import random


VALID_CHOICES = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

def prompt(message):
    print(f"==> {message}")

def player_choice_input():
    while True:
        prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
        choice = input()
        title_choice = choice.title()

        if title_choice not in VALID_CHOICES:
            os.system('clear')
            prompt(f"Invalid choice: {choice}")
        else:
            return title_choice

def display_winner(both_choices_argument):

    os.system('clear')

    prompt(f"You chose {both_choices_argument[0]}, computer chose "
           f"{both_choices_argument[1]}")

    match both_choices_argument:

        case (("Paper", "Rock") | ("Spock", "Rock") | ("Lizard", "Paper") |
             ("Scissors", "Paper") | ("Rock", "Scissors") |
             ("Spock", "Scissors") | ("Lizard", "Spock") | ("Paper", "Spock") |
             ("Scissors", "Lizard") | ("Rock" , "Lizard")):

            prompt("You win!\n")

        case (("Rock", "Paper") | ("Rock", "Spock") | ("Paper", "Lizard") |
             ("Paper", "Scissors") | ("Scissors", "Rock") |
             ("Scissors", "Spock") | ("Spock", "Lizard") | ("Spock", "Paper") |
             ("Lizard", "Scissors") | ("Lizard", "Rock")):

            prompt("Computer wins!\n")

        case _:
            prompt("It's a tie!\n")

def play_again_input():
    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input()
        answer_lower = answer.lower()

        os.system('clear')

        if answer_lower.startswith('n'):
            prompt('Thanks for playing! Goodbye for now.\n')
            return False
        if answer_lower.startswith('y'):
            return True

        prompt(f"Invalid choice: {answer}")


os.system('clear')

prompt(f'Welcome to the {", ".join(VALID_CHOICES)} program!')
prompt('Game on!\n')

play_again = 'set to arbitrary truthy value for initial while loop entry'

while play_again:

    player_choice = player_choice_input()

    computer_choice = random.choice(VALID_CHOICES)

    both_choices = (player_choice, computer_choice)

    display_winner(both_choices)

    play_again = play_again_input()