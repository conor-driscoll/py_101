import os
import random


VALID_CHOICES = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']


def prompt(message):
    print(f"==> {message}")

def player_choice_input():
    while True:
        prompt(f'Choose one: {", ".join(VALID_CHOICES)}\n')
        prompt('(feel free to abbreviate your choice, in which case the '
               'program will use the first letter of your entry to select a '
               'choice that begins with that same first letter)\n')
        choice = input()
        choice_upper = choice.upper()

        if choice.title() in VALID_CHOICES:
            return choice.title()

        os.system('clear')

        final_choice_or_none = check_1st_letter_match(choice, choice_upper)

        if final_choice_or_none:
            return final_choice_or_none

        os.system('clear')
        prompt(f"Invalid choice: '{choice}'")

def check_1st_letter_match(choice_argument, choice_upper_argument):
    valid_choice_matches = [valid_choice for valid_choice in VALID_CHOICES
                 if valid_choice.startswith(f'{choice_upper_argument[0]}')]

    qty_valid_choice_matches = len(valid_choice_matches)

    if qty_valid_choice_matches == 1:
        return valid_choice_matches[0]

    if qty_valid_choice_matches > 1:
        return choose_from_multiple_matches(valid_choice_matches,
                                            choice_argument)

def choose_from_multiple_matches(valid_choice_matches_argument,
                                 choice_argument):
    while True:
        prompt(f"The first letter of your initial entry, "
               f"'{choice_argument[0]}', matched the following choices: "
               f'{", ".join(valid_choice_matches_argument)}.\n')
        prompt("Please select '1' for the first option listed, '2' for the "
               "second, etc.\n")
        index_input = input()

        try:
            index_int = int(index_input)
        except ValueError:
            os.system('clear')
            prompt(f"Invalid selection: '{index_input}'. Please re-select.")
            continue
        else:
            if index_int < 1:
                os.system('clear')
                prompt(f"Invalid selection: '{index_input}'. "
                       "Please re-select.")
                continue

        try:
            return valid_choice_matches_argument[index_int - 1]
        except IndexError:
            os.system('clear')
            prompt(f"Invalid selection: '{index_input}'. Please re-select.")

def decide_game_winner(both_choices_argument):

    os.system('clear')

    prompt(f"You chose {both_choices_argument[0]}, computer chose "
           f"{both_choices_argument[1]}")

    match both_choices_argument:

        case (("Paper", "Rock") | ("Spock", "Rock") | ("Lizard", "Paper") |
             ("Scissors", "Paper") | ("Rock", "Scissors") |
             ("Spock", "Scissors") | ("Lizard", "Spock") | ("Paper", "Spock") |
             ("Scissors", "Lizard") | ("Rock" , "Lizard")):

            return "You win the game!"

        case (("Rock", "Paper") | ("Rock", "Spock") | ("Paper", "Lizard") |
             ("Paper", "Scissors") | ("Scissors", "Rock") |
             ("Scissors", "Spock") | ("Spock", "Lizard") | ("Spock", "Paper") |
             ("Lizard", "Scissors") | ("Lizard", "Rock")):

            return "Computer wins the game!"

        case _:
            return "It's a tie!"

def score_board(game_outcome_argument, player_score_argument,
              computer_score_argument):

    prompt(f"{game_outcome_argument}\n")
    prompt(f"Your score is: {player_score_argument} win(s).")
    prompt(f"The computer's score is: {computer_score_argument} win(s).\n")

    if player_score_argument == 3:
        prompt("You win the best of five series!\n")

    if computer_score_argument == 3:
        prompt("Computer wins the best of five series!")

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

        prompt(f"Invalid choice: '{answer}'")


os.system('clear')

prompt(f'Welcome to the {", ".join(VALID_CHOICES)}, best of 5 program!')
prompt('Game on!\n')

play_again = 'set to arbitrary truthy value for initial while loop entry'
player_score = 0
computer_score = 0

while play_again:

    player_choice = player_choice_input()

    computer_choice = random.choice(VALID_CHOICES)

    both_choices = (player_choice, computer_choice)

    game_outcome = decide_game_winner(both_choices)

    match game_outcome:
        case "You win the game!":
            player_score += 1
        case "Computer wins the game!":
            computer_score += 1

    score_board(game_outcome, player_score,
              computer_score)

    if player_score < 3 and computer_score < 3:
        continue

    play_again = play_again_input()


# Extra unused code below:
    # Doesn't work:
        # first_letter_match_counter = 0

        # for valid_choice in VALID_CHOICES:
        #     if valid_choice.startswith(f'{choice_upper[0]}'):
        #         selection = valid_choice
        #         first_letter_match_counter += 1

        # print(first_letter_match_counter)

        # if first_letter_match_counter == 1:
        #     return selection

        # if first_letter_match_counter == 2:
        #     for valid_choice in VALID_CHOICES:
        #         if valid_choice.startswith(f'{choice_upper[0:2]}'):
        #             return valid_choice

        # This works:
        # if choice_lower.startswith('r'):
        #     return 'Rock'
        # elif choice_lower.startswith('p'):
        #     return 'Paper'
        # elif choice_lower.startswith('l'):
        #     return 'Lizard'
        # elif choice_lower.startswith('sc'):
        #     return 'Scissors'
        # elif choice_lower.startswith('sp'):
        #     return 'Spock'
        # else:
        #     os.system('clear')
        #     prompt(f"Invalid choice: {choice}")
