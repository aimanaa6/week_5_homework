import random

def user_conversion(user_response):
    """
    This function converts the letter inputted by the user
    :param user_response:
    :return: converted response
    """
    if user_response == "R":
        return "Rock"
    elif user_response == "S":
        return "Scissors"
    elif user_response == "P":
        return "Paper"
    else:
        return "Invalid answer"

def computer_conversion(computer_choice):
    """
    This function uses a conditional statement to convert the randomised integer into a string
    :param computer_choice:
    :return: converted computer response
    """
    if computer_choice == 0:
        return "Rock"
    elif computer_choice == 1:
        return "Paper"
    else:
        return "Scissors"


def determine_winner(user_response, computer_choice):
    """
    This function uses a dictionary and conditional statement to determine the winner
    :param user_response:
    :param computer_choice:
    :return: results
    """
    outcomes = {
        "Rock": "Scissors",
        "Paper": "Rock" ,
        "Scissors": "Paper"
    }
    # dictionary lists the different outcomes
    # keys = user choice/value = what option can the user beat?

    if user_response == computer_choice:
        return "It's a draw!"
    # if both values are equal to each other (equality operator)
    if outcomes[user_response] == computer_choice:
        return "You win!"
    # [] looks up the key in the dictionary, if the value is = to the computer's choice, the user wins
    # if the key does not match up to the computer's choice, the user loses
    else:
        return "You lose!"


def rock_paper_scissors():
    # opening command
    print("Rock,Paper or Scissors?")
    # prompt for user
    user_response = input("Please select R, P or S: ")
    # f string including variable with conversion function
    print(f"You have selected {user_conversion(user_response)}")
    # computer generates random number between both integers
    computer_choice = random.randint(0, 2)
    # prints the computer's choice (converted from integer)
    print(f"The computer has chosen {computer_conversion(computer_choice)}")
    # applies function and compares both responses to determine the winner
    print(determine_winner(user_conversion(user_response), computer_conversion(computer_choice)))

# rock_paper_scissors()

if __name__ == "__rock_paper_scissors__":
    rock_paper_scissors()