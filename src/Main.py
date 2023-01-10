from application import CalculateRankings, UserInterface

def main():
    leagueScores = CalculateRankings.CalculateRankings()

    print("Welcome to Calculate Rankings!\n")
    while(True):
        inputType = UserInterface.chooseInputType()

        if(inputType == 1):
            UserInterface.manualInput(leagueScores)
        elif(inputType == 2):
            UserInterface.fileInput(leagueScores)
        elif(inputType == 3):
            UserInterface.printRankings(leagueScores)

        print("")

if __name__ == "__main__":
    main()

