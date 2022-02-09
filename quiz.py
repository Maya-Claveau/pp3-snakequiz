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
    answered = False
    while (not answered):
        print("How many hearts does a snake have?")
        answer1 = input("A. 2 \nB. 3 \nC. 1\nAnswer: ").strip()
        if answer1.upper() == "B" or answer1.upper() == "THREE" or answer1 == "3":  # need to make it shorter
            print("Correct!\n")
            score += 1
            break
        elif answer1.upper() == "A" or "2" or answer1.upper() == "C" or "1":
            print("Incorrect!\n")
            break
        else:
            print("Invalid input!! Please choose between 'A' 'B' or 'C'\n")

    print("Interesting facts: ")
    print("Snakes and other reptiles have a three-chambered heart that ")
    print("controls the circulatory system via the left and right atrium,")
    print("and one ventricle.\n")

    # question 2
    answer2 = input("Do snakes have bones? Y/N ").strip()
    if answer2.upper() == "Y":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")

    print("Interesting facts: ")
    print("As snakes are so flexible, it may be tempting to think that snakes")
    print("have no bones. However, snakes do indeed have bones. In fact, they")
    print("have hundreds, even more than us humans.\n")

    # question 3
    answer3 = input("Do all snakes lay eggs? Y/N ").strip()
    if answer3.upper() == "N":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")

    print("Interesting facts: ")
    print("Most snakes lay eggs, but some species - like sea snakes — give")
    print("live birth to young.\n")

    # question 4
    print("How many species of Snakes there are?")
    answer4 = input("A 600 \nB 1500 \nC 3000+ \nAnswer: ").strip()
    if answer4.upper() == "C":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")

    print("Interesting facts: ")
    print("There are more than 3,000 species of snakes on the planet and they")
    print("are found everywhere except in Antarctica, Iceland, Ireland,")
    print("Greenland, and New Zealand.\n")

    # question 5
    print("Out of 3000 + species, how many are venomous?")
    answer5 = input("A 600 \nB 1500 \nC 3000+ \nAnswer: ").strip()
    if answer5.upper() == "A":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")

    print("Interesting facts: ")
    print("According to the World Health Organization (WHO), out of 600 +")
    print("venomous species, over 200 are considered to be medically")
    print("important.\n")

    # question 6
    answer6 = input("Are sea snakes venomous? Y/N ").strip()
    if answer6.upper() == "Y":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")

    print("Did you know that ")
    print("Sea snakes are some of the most venomous snakes that exist,")
    print("but they pose little threat to humans because they are shy,")
    print("gentle, and their fangs are too short to do much damage.\n")

    # question 7
    print("Why do snakes poke out their tongue?")
    answer7 = input(
        "A too hot \nB too cold \nC sense direction \nAnswer: "
        ).strip()
    if answer7.upper() == "C":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")

    print("Interesting facts: ")
    print("They use their tongues to smell the air, which helps them")
    print("navigate. This is called chemoreception, which literally means")
    print("the receiving (reception) of chemicals (chemo). Airborne")
    print("chemicals stick to the snake its tongue when it is poking out,")
    print("and the snake can identify the particles thanks to a special organ")
    print("called the vomeronasal (or Jacobson's) organ.\n")

    # question 8
    print("Where is the vomeronasal (or Jacobson’s) organ located?")
    answer8 = input(
        "A in its mouth \nB in its chest \nC in its tail \nAnswer: "
        ).strip()
    if answer8.upper() == "A":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")

    print("Interesting facts: ")
    print("The vomeronasal organ is located in the roof of a snake’s mouth,")
    print("and there are two small entry holes that lead to it – like")
    print("nostrils, but on the inside of the mouth.\n")

    # question 9
    print("Which snake with the world’s deadliest venom?")
    answer9 = input(
        "A king cobra \nB python \nC inland taipan \nAnswer: "
        ).strip()
    if answer9.upper() == "C":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")

    print("Interesting facts: ")
    print("The bite of an inland or western taipan delivers a veritable")
    print("witch’s brew of toxins. The venom consists of taipoxin, a")
    print("complex mix of neurotoxins, procoagulants, and myotoxins that")
    print("paralyze muscles, inhibit breathing, cause hemorrhaging in blood")
    print("vessels and tissues, and damage muscles.\n")

    # question 10
    print("What is the longest venomous snake in the world?")
    answer10 = input(
        "A king cobra \nB python \nC inland taipan \nAnswer: "
        ).strip()
    if answer10.upper() == "A":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")

    print("Interesting facts: ")
    print("The longest species of venomous snake is the king cobra or")
    print("hamadryad Ophiophagus hannah. Native to India and southeast")
    print("Asia, it averages 3-4m in length, but according to the")
    print("Guinness World Record, one King Cobra that was captured in")
    print("April 1937 near Port Dickson in Negeri Sembilan, Malaysia,")
    print("had attained a length of 5.71m by autumn 1939.\n")

    # final message with score
    # Display the final score in % to the player

    print("You got " + str((score / 10) * 100) + "% correct!\n")
    if score <= 4:
        print("You could do better, try again!\n")
        return score
    elif score > 4 <= 7:
        print("You did great!\n")
        return score
    else: # why is this part of the code doesn't work
        print("You did awesome job!\n")
        return score
