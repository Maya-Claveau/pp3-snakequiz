# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from quiz import quiz
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('pp3-snakequiz')


def invite_to_play():
    """
    Give player the option to play or end the game
    """
    print("Welcome to Snakequiz!!!\n")
    while True:
        print("Enter Y for Yes, and N for No.")
        play_option = input("Would you like to play? ").strip()

        if play_option.upper() == "N":
            print("GG. See you next time!")
            quit()
        elif play_option.upper() == "Y":
            print("Great!\n")
            break
        else:
            print("Invalid input! Please enter 'Y' or 'N'!\n")


def get_player_name():
    """
    Get player to enter their name
    """
    print("Next please enter your name! It should be madeup by two letters.")
    print("For example: mk, js, sm\n")

    player_name = input("Please enter your name: ").strip()  # need to validate name
    print(f"Hi {player_name}, let's begin the quiz!!\n")


invite_to_play()
get_player_name()
play_quiz()

