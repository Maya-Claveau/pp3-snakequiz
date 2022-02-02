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
    
    play_option = input("Would you like to play? Y for Yes, and N for No. ")
    if play_option.upper() != "Y":
        print("GG. See you next time!")
        quit()
    print("Great!\n")


def get_player_name():
    """
    Get player to enter their name
    """
    print("Next please enter your name! It should be madeup by two letters.")
    print("For example: mk, js, sm, etc\n")

    player_name = input("Please enter your name: ")
    print(f"Hi {player_name}, let's begin the quiz!!")

def play_quiz():
    """
    all the quiz of the game, if the player get it right, the score
    will be increased by 1
    """

    score = 0

    answer = input("How many hearts does a snake have? A two; B three; C one ")
    if answer.upper() == "B":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    

    print("You got " + str(score) + " questions correct!")
    print("You got " + str((score / 10) * 100) + "%.")


invite_to_play()
get_player_name()
play_quiz()