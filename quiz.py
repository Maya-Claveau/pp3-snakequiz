# this is the quiz part of the game, with score and final message at the bottom


def play_quiz():
    """
    all the quiz of the game, if the player get it right, the score
    will be increased by 1. There is one interesting fact displayed
    after each question, regardless of the player's answer for educational
    purposes.
    """
    score = 0

    # question 1
    while True:
        print("How many hearts does a snake have?")
        answer1 = input("A. 2 \nB. 3 \nC. 1\nAnswer: \n").strip()
        if answer1.upper() == "B":
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
    print("and one ventricle.\n")

    # question 2
    while True:
        answer2 = input("Do snakes have bones? Y/N \n").strip()
        if answer2.upper() == "Y":
            print("Correct!\n")
            score += 1
            break
        elif answer2.upper() == "N":
            print("Incorrect!\n")
            break
        else:
            print("Invalid input! Please choose between 'Y' and 'N'!\n")

    print("Interesting facts: ")
    print("As snakes are so flexible, it may be tempting to think that snakes")
    print("have no bones. However, snakes do indeed have bones. In fact, they")
    print("have hundreds, even more than us humans.\n")

    # question 3
    while True:
        answer3 = input("Do all snakes lay eggs? Y/N \n").strip()
        if answer3.upper() == "N":
            print("Correct!\n")
            score += 1
            break
        elif answer3.upper() == "Y":
            print("Incorrect!\n")
            break
        else:
            print("Invalid input! Please choose between 'Y' and 'N'!\n")

        print("Interesting facts: ")
        print("Most snakes lay eggs, but some species, like sea snakes, give")
        print("live birth to young.\n")

    # question 4
    while True:
        print("How many species of Snakes there are?")
        answer4 = input("A 600 \nB 1500 \nC 3000+ \nAnswer: \n").strip()
        if answer4.upper() == "C":
            print("Correct!\n")
            score += 1
            break
        elif answer4.upper() == "A" or answer4.upper() == "B":
            print("Incorrect!\n")
            break
        else:
            print("Invalid input!! Please choose between 'A' 'B' or 'C'\n")

    print("Interesting facts: ")
    print("There are more than 3,000 species of snakes on the planet and they")
    print("are found everywhere except in Antarctica, Iceland, Ireland,")
    print("Greenland, and New Zealand.\n")

    # question 5
    while True:
        print("Out of 3000 + species, how many are venomous?")
        answer5 = input("A 600 \nB 1500 \nC 3000+ \nAnswer: \n").strip()
        if answer5.upper() == "A":
            print("Correct!\n")
            score += 1
            break
        elif answer5.upper() == "C" or answer5.upper() == "B":
            print("Incorrect!\n")
            break
        else:
            print("Invalid input!! Please choose between 'A' 'B' or 'C'\n")

    print("Interesting facts: ")
    print("According to the World Health Organization (WHO), out of 600 +")
    print("venomous species, over 200 are considered to be medically")
    print("important.\n")

    # question 6
    while True:
        answer6 = input("Are sea snakes venomous? Y/N \n").strip()
        if answer6.upper() == "Y":
            print("Correct!\n")
            score += 1
            break
        elif answer6.upper() == "N":
            print("Incorrect!\n")
            break
        else:
            print("Invalid input! Please choose between 'Y' and 'N'!\n")

    print("Did you know that ")
    print("Sea snakes are some of the most venomous snakes that exist,")
    print("but they pose little threat to humans because they are shy,")
    print("gentle, and their fangs are too short to do much damage.\n")

    # question 7
    while True:
        print("Why do snakes poke out their tongue?")
        answer7 = input(
            "A too hot \nB too cold \nC sense direction \nAnswer: \n"
            ).strip()
        if answer7.upper() == "C":
            print("Correct!\n")
            score += 1
            break
        elif answer7.upper() == "A" or answer7.upper() == "B":
            print("Incorrect!\n")
            break
        else:
            print("Invalid input!! Please choose between 'A' 'B' or 'C'\n")

    print("Interesting facts: ")
    print("They use their tongues to smell the air, which helps them")
    print("navigate. This is called chemoreception, which literally means")
    print("the receiving (reception) of chemicals (chemo). Airborne")
    print("chemicals stick to the snake its tongue when it is poking out,")
    print("and the snake can identify the particles thanks to a special organ")
    print("called the vomeronasal (or Jacobson's) organ.\n")

    # question 8
    while True:
        print("Where is the vomeronasal (or Jacobson’s) organ located?")
        answer8 = input(
            "A in its mouth \nB in its chest \nC in its tail \nAnswer: \n"
            ).strip()
        if answer8.upper() == "A":
            print("Correct!\n")
            score += 1
            break
        elif answer8.upper() == "C" or answer8.upper() == "B":
            print("Incorrect!\n")
            break
        else:
            print("Invalid input!! Please choose between 'A' 'B' or 'C'\n")

    print("Interesting facts: ")
    print("The vomeronasal organ is located in the roof of a snake’s mouth,")
    print("and there are two small entry holes that lead to it – like")
    print("nostrils, but on the inside of the mouth.\n")

    # question 9
    while True:
        print("Which snake with the world’s deadliest venom?")
        answer9 = input(
            "A king cobra \nB python \nC inland taipan \nAnswer: \n"
            ).strip()
        if answer9.upper() == "C":
            print("Correct!\n")
            score += 1
            break
        elif answer9.upper() == "A" or answer9.upper() == "B":
            print("Incorrect!\n")
            break
        else:
            print("Invalid input!! Please choose between 'A' 'B' or 'C'\n")

    print("Interesting facts: ")
    print("The bite of an inland or western taipan delivers a veritable")
    print("witch’s brew of toxins. The venom consists of taipoxin, a")
    print("complex mix of neurotoxins, procoagulants, and myotoxins that")
    print("paralyze muscles, inhibit breathing, cause hemorrhaging in blood")
    print("vessels and tissues, and damage muscles.\n")

    # question 10
    while True:
        print("What is the longest venomous snake in the world?")
        answer10 = input(
            "A king cobra \nB python \nC inland taipan \nAnswer: \n"
            ).strip()
        if answer10.upper() == "A":
            print("Correct!\n")
            score += 1
            break
        elif answer10.upper() == "C" or answer10.upper() == "B":
            print("Incorrect!\n")
            break
        else:
            print("Invalid input!! Please choose between 'A' 'B' or 'C'\n")

    print("Interesting facts: ")
    print("The longest species of venomous snake is the king cobra or")
    print("hamadryad Ophiophagus hannah. Native to India and southeast")
    print("Asia, it averages 3-4m in length, but according to the")
    print("Guinness World Record, one King Cobra that was captured in")
    print("April 1937 near Port Dickson in Negeri Sembilan, Malaysia,")
    print("had attained a length of 5.71m by autumn 1939.\n")

    # final message with score
    # Display the final score to the player

    print("You got " + str(score) + " out of 10 correct!\n")

    if score <= 4:
        print("You could do better, try again!\n")
        return score
    elif score > 4 and score <= 7:
        print("You did great!\n")
        return score
    else:
        print("You did awesome job!\n")
        return score
