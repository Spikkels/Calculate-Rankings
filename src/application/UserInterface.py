import sys
import os.path
from application.CalculateRankings import CalculateRankings


def chooseInputType():
    """
    Determine what type of input the user will use manual or import file.
    """
    print("********************* MAIN MENU ***********************")
    print("Press 1 to insert scores manually <ctrl-d> to end input")
    print("Press 2 read file in directory")
    print("Press 3 to get league results")
    print("Press 0 to exit")
    print("")
    while True:
        try:
            print("Please choose a option: ")
            inputInt = int(input())

            if(inputInt == 1 or inputInt == 2 or inputInt == 3):
                return inputInt
            elif(inputInt == 0):
                exit()
            else:
                continue
        except ValueError:
            print("ERROR: Value must be a 1, 2, 3 or 0")
            continue


def manualInput(leagueScores: CalculateRankings):
    print("")
    print("Enter league games results")
    print("Multiple results can be inserted")
    print("Example of input:  Tarantulas 1, FC Awesome 1")
    print("Press <ctrl-d> to end input")
    print("")

    gameResults = sys.stdin.readlines()
    success = leagueScores.inputGameResultsFromInput(gameResults)

    if (success):
        printRankings(leagueScores)


def fileInput(leagueScores: CalculateRankings):
    print("")
    print("Type in the file name that contains the league games results?")
    gameResults = input()

    if (os.path.isfile(gameResults)):
        success = leagueScores.inputGameResultsFromFile(gameResults)

        if (success):
            printRankings(leagueScores)
            return True

    else:
        print("")
        print("ERROR: File name does not exist in directory.")
        return False
        

def printRankings(leagueScores: CalculateRankings):
    if (leagueScores.isResultsAvailable()):
        print("")
        print("The Ranking table the league are:")
        print("")
        print(leagueScores.calculateRankings())        
    else:
        print("No Results are available")
