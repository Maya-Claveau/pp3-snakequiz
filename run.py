# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
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
    Give player the option to play or not to play the game
    """
    print("Welcome to Snakequiz")
    print("Would you like to play? Y for Yes, and N for No\n")

    play_option = input("Enter your answer here: ")
    print(f"You answered {play_option}\n")


def get_player_name():
    """
    Get player to enter their name
    """
    print("Next please enter your name!")
    print("IT should be madeup by two letters.")
    print("For example: mk, js, sm, etc\n")

    player_name = input("Please enter your name: ")
    print(f"Hi {player_name}, let's begin the quiz!!")

invite_to_play()
get_player_name()