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


class player():
    """
    Create a player object according to player's input
    """

    def _init_(self):
        self.player_name = self.get_player_name()

    def get_player_name():
        """
        Get player to enter their chosen name. Letters
        and numbers are valid, with max length of 8
        characters. The request will only ends when a valid
        input is received.
        """
        while True:
            print("Next please enter your name!\n")
            print("Characters A-Z, a-z, and 0-9 are permitted.")
            print("Maximum of 8 characters.")
            print("Any white space will be removed.\n")

            player_name = input("Please enter your name: ")

            if self.check_player_name(player_name):
                break
                print("\n")
                print(f"Hi {player_name}, let's begin the quiz!!\n")

        return player_name.strip()

    def check_player_name(self, player_name_str):
        """
        Validate user's input if the username is valid
        """
        self.player_name_str = str
        try:
            if not player_name_str:
                raise ValueError("Please enter a player name")
            if len(player_name_str) > 8:
                raise ValueError("Player name too long")

        except ValueError as e:
                print(f"Invalid data: {e}, please try again.\n")
                return False

        return True

invite_to_play()
player()
