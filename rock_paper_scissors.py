import random
from random import randint

choices_meanings = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
computer_choice_meanings = {0:'Rock', 1:'Paper', 2:'Scissors'}

user_input = input('Choose R, P or S')

def user_conversion(user_input):
    if user_input == choices_meanings['R']:
        return 'Rock'
    elif user_input == choices_meanings['P']:
        return 'Paper'
    elif user_input == choices_meanings['S']:
        return 'Scissors'
    else:
        return 'Invalid answer'

computer_choice = randint(0,2)
print(computer_choice)
def computer_input(computer_choice):
    if computer_choice == computer_choice_meanings[0]:
        return 'Rock'
    elif computer_choice == computer_choice_meanings[1]:
        return 'Paper'
    else:
        return 'Scissors'

def deciding_winner(user_input, computer_choice):
    winning_combinations = {'Rock': 'Scissors', 'Paper': "Rock", 'Scissors': 'Paper' }
    if user_input == computer_choice:
        return "It's a draw"
    elif winning_combinations[user_input] == computer_choice:
        return 'User wins'
    else:
        return 'Computer wins'


def rps_game():
    global user_input, computer_choice
    user_input = input('Choose R, P or S')
    print(user_conversion(user_input))
    computer_choice = randint(0, 2)
    print(computer_input(computer_choice))
    print(deciding_winner(user_input, computer_choice))


rps_game()