import os
import random
import time


MAX_SERIES_LENGTH = 5

WINNING_MOVES = {
    'Rock': {
        'Scissors': ['crushes', 'crushed'],
        'Lizard':   ['crushes', 'crushed'],
        },
    'Paper': {
        'Spock':    ['disproves', 'disproved'],
        'Rock':     ['covers', 'covered'],
        },
    'Scissors': {
        'Paper':    ['cuts', 'cut'],
        'Lizard':   ['decapitates', 'decapitated'],
        },
    'Lizard': {
        'Spock':    ['poisons', 'poisoned'],
        'Paper':    ['eats', 'ate']
        },
    'Spock': {
        'Rock':     ['vaporizes', 'vaporized'],
        'Scissors': ['smashes', 'smashed'],
        },
}


def total_interface_clear():
    os.system('clear')
    os.system('clear')

def prompt(message):
    print(f"==> {message}")

def calculate_series_winning_number():
    return (MAX_SERIES_LENGTH // 2) + 1

def welcome_and_rules():

    series_winning_number = calculate_series_winning_number()

    prompt(f'Welcome to the {", ".join(WINNING_MOVES)}, best of '
           f'{MAX_SERIES_LENGTH} series against the computer!')
    prompt(f"(first to win {series_winning_number} games, wins the series)\n")

    prompt(f"You'll choose one of the {len(WINNING_MOVES)} characters, the "
        "computer will choose one randomly, and the game winner will be "
        "determined as follows:\n")

    for character1, dict2 in WINNING_MOVES.items():

        for index, (character2, action) in enumerate(dict2.items()):
            match index:
                case 0:
                    game_rule = f"* {character1} {action[0]} {character2} and"
                case 1:
                    game_rule = f"{game_rule} {action[0]} {character2}"

        prompt(game_rule)

    print()
    prompt("(if an abbreviation is entered, the program will attempt to "
           "match the first letter with a game character)\n")

def player_choice_input():
    while True:
        prompt(f'Choose one: {", ".join(WINNING_MOVES)}\n')
        initial_selection = input()
        choice_upper = initial_selection.upper()
        os.system('clear')

        if not choice_upper:
            prompt(f"Invalid choice: '{initial_selection}'")
            continue

        if initial_selection.title() in WINNING_MOVES:
            return initial_selection.title()

        final_choice_or_false = check_1st_letter_match(initial_selection,
                                                       choice_upper)

        if final_choice_or_false:
            return final_choice_or_false

        prompt(f"Invalid choice: '{initial_selection}'")

def check_1st_letter_match(initial_selection_argument, choice_upper_argument):
    valid_move_matches = [valid_move for valid_move in
                            WINNING_MOVES if
                       valid_move.startswith(f'{choice_upper_argument[0]}')]

    qty_valid_move_matches = len(valid_move_matches)

    if qty_valid_move_matches == 1:
        return valid_move_matches[0]

    if qty_valid_move_matches > 1:
        return choose_from_multiple_matches(valid_move_matches,
                                            initial_selection_argument)
    return False

def choose_from_multiple_matches(valid_move_matches_argument,
                                 initial_selection_argument):
    while True:
        prompt(f"The first letter of your initial entry, "
               f"'{initial_selection_argument[0]}', matched the following "
               f'choices: {", ".join(valid_move_matches_argument)}.\n')
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
            return valid_move_matches_argument[index_int - 1]
        except IndexError:
            os.system('clear')
            prompt(f"Invalid selection: '{index_input}'. Please re-select.")

def decide_game_winner(both_choices_argument):

    player, computer = both_choices_argument

    os.system('clear')
    time.sleep(1)

    if computer in WINNING_MOVES[player]:
        return (f"Your {player} {WINNING_MOVES[player][computer][1]} the "
                f"computer's {computer}.", "You win the game!")
    if player in WINNING_MOVES[computer]:
        return (f"The computer's {computer} "
                f"{WINNING_MOVES[computer][player][1]} your {player}.",
                "The computer wins the game!")

    return (f"Your {player} & the computer's {computer} struggled to a draw.",
             "It's a tie!")

def decide_series_winner(player_score_argument, computer_score_argument):

    series_winning_number = calculate_series_winning_number()

    if player_score_argument == series_winning_number:
        return 'You win'
    if computer_score_argument == series_winning_number:
        return 'Computer wins'

    return False

def score_board(game_recap_argument, game_outcome_argument,
                player_score_argument, computer_score_argument,
                series_outcome_argument):

    prompt(f"{game_recap_argument}")
    prompt(f"{game_outcome_argument}\n")
    prompt(f"Your score is: {player_score_argument} win(s).")
    prompt(f"The computer's score is: {computer_score_argument} win(s).\n")

    if series_outcome_argument:
        prompt(f"{series_outcome_argument} the best of {MAX_SERIES_LENGTH} "
                "series!\n")

def play_again_input():
    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input()
        answer_lower = answer.lower()
        os.system('clear')

        if not answer_lower:
            prompt(f"Invalid choice: '{answer}'")
            continue

        if answer_lower[0] == 'n':
            prompt('Thanks for playing! Goodbye for now.\n')
            return False
        if answer_lower[0] == 'y':
            return True

        prompt(f"Invalid choice: '{answer}'")

def rock_paper_scissors_game_with_bonus_features():

    total_interface_clear()

    welcome_and_rules()

    play_again = True
    player_score = 0
    computer_score = 0

    while play_again:

        player_choice = player_choice_input()

        computer_choice = random.choice(list(WINNING_MOVES))

        both_choices = player_choice, computer_choice

        game_recap, game_outcome = decide_game_winner(both_choices)

        match game_outcome:
            case "You win the game!":
                player_score += 1
            case "The computer wins the game!":
                computer_score += 1

        series_outcome = decide_series_winner(player_score, computer_score)

        score_board(game_recap, game_outcome, player_score,
                    computer_score, series_outcome)

        if not series_outcome:
            continue

        player_score = 0
        computer_score = 0

        play_again = play_again_input()


rock_paper_scissors_game_with_bonus_features()


# Extra unused code below:


    # Doesn't work:
        # first_letter_match_counter = 0

        # for valid_move in VALID_CHOICES:
        #     if valid_move.startswith(f'{choice_upper[0]}'):
        #         selection = valid_move
        #         first_letter_match_counter += 1

        # print(first_letter_match_counter)

        # if first_letter_match_counter == 1:
        #     return selection

        # if first_letter_match_counter == 2:
        #     for valid_move in VALID_CHOICES:
        #         if valid_move.startswith(f'{choice_upper[0:2]}'):
        #             return valid_move


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


    # This works:
    # match both_choices_argument:

    #     case (("Paper", "Rock") | ("Spock", "Rock") | ("Lizard", "Paper") |
    #          ("Scissors", "Paper") | ("Rock", "Scissors") |
    #      ("Spock", "Scissors") | ("Lizard", "Spock") | ("Paper", "Spock") |
    #          ("Scissors", "Lizard") | ("Rock" , "Lizard")):

    #         return "You win the game!"

    #     case (("Rock", "Paper") | ("Rock", "Spock") | ("Paper", "Lizard") |
    #          ("Paper", "Scissors") | ("Scissors", "Rock") |
    #      ("Scissors", "Spock") | ("Spock", "Lizard") | ("Spock", "Paper") |
    #          ("Lizard", "Scissors") | ("Lizard", "Rock")):

    #         return "Computer wins the game!"

    #     case _:
    #         return "It's a tie!"