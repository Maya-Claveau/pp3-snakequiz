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
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")
    print("Interesting facts: ")
    print("Snakes and other reptiles have a three-chambered heart that controls the circulatory system via the left and right atrium, and one ventricle.\n")

    answer = input("Do snakes have bones? Y/N ")
    if answer.upper() == "Y":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")
    print("Interesting facts: ")
    print("As snakes are so flexible, it may be tempting to think that snakes have no bones. However, snakes do indeed have bones. In fact, they have hundreds, even more than us humans.\n") 

    answer = input("Do all snakes lay eggs? Y/N ")
    if answer.upper() == "N":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")
    print("Interesting facts: ")
    print("Most snakes lay eggs, but some species—like sea snakes—give live birth to young.\n")

    answer = input("How many species of Snakes there are? A 600; B 1500; C >3000 ")
    if answer.upper() == "C":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")
    print("Interesting facts: ")
    print("There are more than 3,000 species of snakes on the planet and they are found everywhere except in Antarctica, Iceland, Ireland, Greenland, and New Zealand.\n")

    answer = input("Out of 3000 + species, how many are venomous? A 600; B 1500; C 3000+ ")
    if answer.upper() == "A":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")
    print("Interesting facts: ")
    print("According to the World Health Organization (WHO), out of 600 + venomous species, over 200 are considered to be medically important.\n")

    answer = input("Are sea snakes venomous? Y/N ")
    if answer.upper() == "Y":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")
    print("Did you know that ")
    print("Sea snakes are some of the most venomous snakes that exist, but they pose little threat to humans because they are shy, gentle, and their fangs are too short to do much damage.\n")

    answer = input("Why do snakes poke out their tongue? A too hot; B too cold; C sense direction ")
    if answer.upper() == "C":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")
    print("Interesting facts: ")
    print("They use their tongues to smell the air, which helps them navigate. This is called chemoreception, which literally means the receiving (reception) of chemicals (chemo). Airborne chemicals stick to the snake its tongue when it is poking out, and the snake can identify the particles thanks to a special organ called the vomeronasal (or Jacobson's) organ.\n")

    answer = input("Where is the vomeronasal (or Jacobson’s) organ located? A in its mouth; B in its chest; C in its tail ")
    if answer.upper() == "A":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")
    print("Interesting facts: ")
    print("The vomeronasal organ is located in the roof of a snake’s mouth, and there are two small entry holes that lead to it – like nostrils, but on the inside of the mouth.\n")

    answer = input("Which snake with the world’s deadliest venom? A king cobra; B python; C inland taipan ")
    if answer.upper() == "C":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")
    print("Interesting facts: ")
    print("The bite of an inland or western taipan delivers a veritable witch’s brew of toxins. The venom consists of taipoxin, a complex mix of neurotoxins, procoagulants, and myotoxins that paralyze muscles, inhibit breathing, cause hemorrhaging in blood vessels and tissues, and damage muscles.\n")

    answer = input("What is the longest venomous snake in the world? A king cobra; B python; C inland taipan ")
    if answer.upper() == "A":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")
    print("Interesting facts: ")
    print("The longest species of venomous snake is the king cobra or hamadryad Ophiophagus hannah. Native to India and southeast Asia, it averages 3-4m in length, but according to the Guinness World Record, one King Cobra that was captured in April 1937 near Port Dickson in Negeri Sembilan, Malaysia, had attained a length of 5.71m by autumn 1939.\n") 

    print("You got " + str((score / 10) * 100) + "% correct!\n")

invite_to_play()
get_player_name()
play_quiz()