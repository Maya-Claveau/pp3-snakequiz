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


def get_player_name():
    """
    Get player to enter their name
    """
    print("Next please enter your name! It should be madeup by two letters.")
    print("For example: mk, js, sm\n")

    player_name = input("Please enter your name: ").strip()  # need to validate name
    print(f"Hi {player_name}, let's begin the quiz!!\n")


def play_quiz():
    """
    all the quiz of the game, if the player get it right, the score
    will be increased by 1. There is one interesting fact displayed
    after each question, regardless of the player's answer for educational
    purposes.
    """

    score = 0

# question 1
answered = False
while (not answered):
    answer1 = input(
        "How many hearts does a snake have?\nA. 2 \nB. 3 \nC. 1\nAnswer: "
        ).strip()
    if answer1.upper() == "B" or answer1.upper() == "THREE" or answer1 == "3":
        print("Correct!\n")
        score += 1
        break
    elif answer1.upper() == "A" or answer1.upper() == "C":
        print("Incorrect!\n")
        break
    else:
        print("Invalid input!! Please choose between 'A' 'B' or 'C'\n")

    print("Interesting facts: ")
    print("Snakes and other reptiles have a three-chambered heart that ")
    print("controls the circulatory system via the left and right atrium,")
    print(" and one ventricle.\n")

    # question 2
    answer = input("Do snakes have bones? Y/N ")
    if answer.upper() == "Y":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")
    print("Interesting facts: ")
    print("As snakes are so flexible, it may be tempting to think that snakes have no bones. However, snakes do indeed have bones. In fact, they have hundreds, even more than us humans.\n")

    # question 3
    answer = input("Do all snakes lay eggs? Y/N ")
    if answer.upper() == "N":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")
    print("Interesting facts: ")
    print("Most snakes lay eggs, but some species—like sea snakes—give live birth to young.\n")

    # question 4
    answer = input("How many species of Snakes there are? A 600; B 1500; C >3000 ")
    if answer.upper() == "C":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")
    print("Interesting facts: ")
    print("There are more than 3,000 species of snakes on the planet and they are found everywhere except in Antarctica, Iceland, Ireland, Greenland, and New Zealand.\n")

    # question 5
    answer = input("Out of 3000 + species, how many are venomous? A 600; B 1500; C 3000+ ")
    if answer.upper() == "A":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")
    print("Interesting facts: ")
    print("According to the World Health Organization (WHO), out of 600 + venomous species, over 200 are considered to be medically important.\n")

    # question 6
    answer = input("Are sea snakes venomous? Y/N ")
    if answer.upper() == "Y":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")
    print("Did you know that ")
    print("Sea snakes are some of the most venomous snakes that exist, but they pose little threat to humans because they are shy, gentle, and their fangs are too short to do much damage.\n")

    # question 7
    answer = input("Why do snakes poke out their tongue? A too hot; B too cold; C sense direction ")
    if answer.upper() == "C":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")
    print("Interesting facts: ")
    print("They use their tongues to smell the air, which helps them navigate. This is called chemoreception, which literally means the receiving (reception) of chemicals (chemo). Airborne chemicals stick to the snake its tongue when it is poking out, and the snake can identify the particles thanks to a special organ called the vomeronasal (or Jacobson's) organ.\n")

    # question 8
    answer = input("Where is the vomeronasal (or Jacobson’s) organ located? A in its mouth; B in its chest; C in its tail ")
    if answer.upper() == "A":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")
    print("Interesting facts: ")
    print("The vomeronasal organ is located in the roof of a snake’s mouth, and there are two small entry holes that lead to it – like nostrils, but on the inside of the mouth.\n")

    # question 9
    answer = input("Which snake with the world’s deadliest venom? A king cobra; B python; C inland taipan ")
    if answer.upper() == "C":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")
    print("Interesting facts: ")
    print("The bite of an inland or western taipan delivers a veritable witch’s brew of toxins. The venom consists of taipoxin, a complex mix of neurotoxins, procoagulants, and myotoxins that paralyze muscles, inhibit breathing, cause hemorrhaging in blood vessels and tissues, and damage muscles.\n")

    # question 10
    answer = input("What is the longest venomous snake in the world? A king cobra; B python; C inland taipan ")
    if answer.upper() == "A":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")
    print("Interesting facts: ")
    print("The longest species of venomous snake is the king cobra or hamadryad Ophiophagus hannah. Native to India and southeast Asia, it averages 3-4m in length, but according to the Guinness World Record, one King Cobra that was captured in April 1937 near Port Dickson in Negeri Sembilan, Malaysia, had attained a length of 5.71m by autumn 1939.\n")

    # final message with score
    print("You got " + str((score / 10) * 100) + "% correct!\n")
    if score < 4:
        print("You could do better, try again!")
    elif score >= 4 < 7:
        print("You did great!")
    else:
        print("You did awesome job!")


invite_to_play()
get_player_name()
play_quiz()
