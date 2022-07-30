import random

playersName = ["Ian Anderson", "Jesse Chavez", "Jesus Cruz",  # Array for the player's name
               "Max Fried", "Kenley Jansen", "Dylan Lee",  # |||||||||||||||||||||||||||
               "A.J Minter", "Charlie Morton",  # |||||||||||||||||||||||||||
               "Darren O'Day", "Will Smith",  # |||||||||||||||||||||||||||
               "Jackson Stephens", "Spencer Strider",  # |||||||||||||||||||||||||||
               "Jacob Webb", "Kyle Wright",  # |||||||||||||||||||||||||||
               "William Contrearas", "Travis d'Arnaud",  # |||||||||||||||||||||||||||
               "Ozzie Albies", "Orlando Arcia",  # |||||||||||||||||||||||||||
               "Matt Olsen", "Austin Riley",  # |||||||||||||||||||||||||||
               "Dansby Swanson",  # |||||||||||||||||||||||||||
               "Ronald Acuna Jr.", "Adam Duvall",  # |||||||||||||||||||||||||||
               "Michael Harris II", "Guillermo Heredia",  # |||||||||||||||||||||||||||
               "Marcell Ozuna"]  # |||||||||||||||||||||||||||

playersAge = [24, 38, 27, 28, 34,  # Array for the player's age
              27, 28, 38, 39, 32, 28,  # ||||||||||||||||||||||||||
              23, 28, 26, 24, 33, 25,  # ||||||||||||||||||||||||||
              27, 28, 25, 28, 24, 33,  # ||||||||||||||||||||||||||
              21, 31, 31]  # ||||||||||||||||||||||||||

playersLeague = "National League East"  # Array for the player's League

playersHeight = [75, 73, 73, 76, 77,  # Array for the player's Height
                 75, 72, 77, 76, 77,  # |||||||||||||||||||||||||||||
                 74, 72, 74, 76, 72,  # |||||||||||||||||||||||||||||
                 74, 68, 72, 77, 75,  # |||||||||||||||||||||||||||||
                 73, 72, 73, 72, 70, 73]  # |||||||||||||||||||||||||||||

playersCountry = ["US", "US", "Mexico", "US",  # Array for the player's Nationality
                  "Curaco", "US", "US", "US",  # ||||||||||||||||||||||||||||||||||
                  "US", "US", "US", "US", "US",  # ||||||||||||||||||||||||||||||||||
                  "US", "Venezuela", "US", "Curaco",  # ||||||||||||||||||||||||||||||||||
                  "Venezuela",  # ||||||||||||||||||||||||||||||||||
                  "US", "US", "US", "Venezuela",  # ||||||||||||||||||||||||||||||||||
                  "US", "US", "Cuba",  # ||||||||||||||||||||||||||||||||||
                  "Dominican Republic"]  # ||||||||||||||||||||||||||||||||||

playersPos = ["SP", "RP", "RP", "SP", "RP",  # Array for the player's Position
              "RP", "RP", "SP", "RP", "RP",  # |||||||||||||||||||||||||||||||
              "RP", "SP", "RP", "SP",  # |||||||||||||||||||||||||||||||
              "C", "C", "2B", "SS", "1B",  # |||||||||||||||||||||||||||||||
              "3B", "SS", "RF", "RF", "CF",  # |||||||||||||||||||||||||||||||
              "CF", "LF"]  # |||||||||||||||||||||||||||||||

playerThrow = ["R", "R", "R", "L", "R", "L",  # Array for the player's throwing arm
               "L", "R", "R", "L", "R", "R", "R",  # |||||||||||||||||||||||||||||||||||
               "R", "R", "R", "R", "R", "R", "R",  # |||||||||||||||||||||||||||||||||||
               "R", "R", "R", "L", "L", "R"]  # |||||||||||||||||||||||||||||||||||

playerBat = ["R", "R", "R", "L", "S", "L", "L",  # Array for the player's bat
             "R", "R", "R", "R", "R", "R", "R",  # ||||||||||||||||||||||||||
             "R", "R", "S", "R", "L", "R", "R",  # ||||||||||||||||||||||||||
             "R", "R", "L", "R", "R"]  # ||||||||||||||||||||||||||

player = random.randint(1, 26)

print("Welcome to the ATL Braves Wordle. We have a secret player in mind from the active ATL Braves Roster. \n"
      "Let's see if your Braves Knowledge can help you guess them."
      "And let's see if you're really a Braves fan! \n")


def guessAge(nameGuess):
    for i in range(26):
        age = playersName[i]
        if nameGuess == age:
            return playersAge[i]


def guessHeight(nameGuess):
    for i in range(26):
        height = playersName[i]
        if nameGuess == height:
            return playersHeight[i]


def guessCountry(nameGuess):
    for i in range(26):
        country = playersName[i]
        if nameGuess == country:
            return playersCountry[i]


def guessPos(nameGuess):
    for i in range(26):
        pos = playersName[i]
        if nameGuess == pos:
            return playersPos[i]


def guessThrow(nameGuess):
    for i in range(26):
        throw = playersName[i]
        if nameGuess == throw:
            return playerThrow[i]


def guessBat(nameGuess):
    for i in range(26):
        bat = playersName[i]
        if nameGuess == bat:
            return playerBat[i]


rightPlayer = playersName[player]
rightAge = playersAge[player]
rightHeight = playersHeight[player]
rightCountry = playersCountry[player]
rightPos = playersPos[player]
rightHand = playerThrow[player]
rightBat = playerBat[player]

for attempts in range(7):
    attemptedGuess = input("Guess a player on the Braves! ")

    # Conditional to see if they got the right player
    if attemptedGuess == rightPlayer:
        print("You got it! You are truly a ATL Braves Fan \n")
        attempts = attempts + 7
        print("Congrats On getting it right \n")
    elif attemptedGuess in playersName:
        # Conditional to check the proper age

        if guessAge(attemptedGuess) == rightAge:
            print("Our player is " + str(rightAge) + " . ")
        else:
            print("Our player is not " + str(guessAge(attemptedGuess)) + " . ")

        # Conditional for checking the height

        if guessHeight(attemptedGuess) == rightHeight:
            print("You got the right height! He is " + str(rightHeight) + " \n")
        else:
            print(str(guessHeight(attemptedGuess)) + " is not the quite height we're looking for \n")

        # Conditional to check player's nationality

        if guessCountry(attemptedGuess) == rightCountry:
            print("Our player is from " + str(rightCountry) + " ! \n")
        else:
            print("Sorry but he is not from " + str(guessCountry(attemptedGuess)) + " \n")

        # Conditional to check player's fielding position

        if guessPos(attemptedGuess) == rightPos:
            print("Our player plays " + str(rightPos) + "! \n")
        else:
            print("Sorry but he does not play " + str(guessPos(attemptedGuess)) + " \n")

        # Conditional to check player's throwing arm

        if guessThrow(attemptedGuess) == rightHand:
            print("Our player throws with thier " + str(rightHand) + " hand! \n")
        else:
            print("Sorry but he doesn't throw with thier " + str(guessThrow(attemptedGuess)) + " hand \n")

        # Conditional to check player's batting position

        if guessBat(attemptedGuess) == rightBat:
            print("Our player does bat " + rightBat + "! \n")
        elif guessBat(attemptedGuess) == "S":
            print("He bats either lefty or righty. Not both \n")
        elif guessBat(attemptedGuess) == "L" or guessBat(attemptedGuess) == "R" and rightBat == "S":
            print("He may bat " + str(guessBat(attemptedGuess)) + " but he also bats another way which means he is a switch hitter \n")
    else:
        print(attemptedGuess + " either does not play for the Braves anymore or is not currently on thier active roster")
print("The Correct Player was... " + str(rightPlayer) + " . Thanks for player ATL Braves Wordle")
