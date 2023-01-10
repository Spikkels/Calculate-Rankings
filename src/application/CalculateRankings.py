import re

class CalculateRankings:
    """ 
    Add Score to team 
        
    :param gameWinScore: (Optional) Score that should be rewarded to team if the game is won
    :param gameLoseScore: (Optional) Score that should be rewarded to team if the game is lost
    :param gameTieScore: (Optional) Score that should be rewarded to team if the game is a tie
    """
    def __init__(self, gameWinScore = 3, gameLoseScore = 0, gameTieScore = 1):
        self.rankings = dict()
        self.backupRankings = dict()

        self.gameWinScore = gameWinScore
        self.gameLoseScore = gameLoseScore
        self.gameTieScore = gameTieScore        


    def __addTeamScore(self, teamName: str, score: int):
        """ 
        Add score to team 
        
        :param teamName: The team Name
        :param score: Score that should be added to League score
        """
        if teamName in self.rankings.keys():
            currentScore = self.rankings.get(teamName)
            self.rankings.update({teamName: currentScore + score})
        else:
            self.rankings[teamName] = score


    def __addGameLeagueScore(self, teamName1: str, teamScore1: int, teamName2: str, teamScore2: int):
        """ 
        Adds score to the league total. This is determined by game win, lose or ties.

        :param teamName1: The name of the first team in the game
        :param teamScore1: Score of the first team of the played game
        :param teamName2: The name of the second team in the game
        :param teamScore2: Score of the second team of the played game
        """     
        if (teamScore1 == teamScore2):
            self.__addTeamScore(teamName1, self.gameTieScore)
            self.__addTeamScore(teamName2, self.gameTieScore)
        elif (teamScore1 > teamScore2):
            self.__addTeamScore(teamName1, self.gameWinScore)
            self.__addTeamScore(teamName2, self.gameLoseScore)
        elif (teamScore1 < teamScore2):
            self.__addTeamScore(teamName1, self.gameLoseScore)
            self.__addTeamScore(teamName2, self.gameWinScore)


    def calculateRankings(self):
        """ 
        Calculate league score sorted by the winners from top to bottom and when there is a tie the teams will have the same ranking.

        Output Example:
        1. England: 4 pts
        2. France: 3 pts
        2. Turkey: 3 pts
        4. Spain: 1 pts

        :return: Literal string with output
        """
        # Sort the dictionary by value and then by key
        sortedByWinners = sorted(self.rankings.items(), key=lambda item: (-item[1], item[0]))

        # Initialize a counter variable
        counter = 1

        output_list = []

        # Iterate over the sorted dictionary
        for i, (key, value) in enumerate(sortedByWinners):
            # If the value is not the same as the previous value, reset the counter
            if i > 0 and value != sortedByWinners[i-1][1]:
                counter = i + 1
            # Append the formatted string to the list
            output_list.append(f"{counter}. {key}: {value} pts")

        # Join the strings in the list with newlines
        output_string = '\n'.join(output_list)

        return output_string


    def __getGameResults(self, line):
        """ 
        Validates the the String data
        
        :param teamName: The team Name
        :return: Tuple with four variables. The team names and scores.  If the validation is successfully True returned.
        """
        try:
            split = line.strip().split(",")

            GameResultsTeam1 = split[0].split(" ")
            GameResultsTeam2 = split[1].split(" ")

            teamScore1: int = int(GameResultsTeam1.pop())
            teamScore2: int = int(GameResultsTeam2.pop())

            teamName1 = ' '.join(GameResultsTeam1).strip()
            teamName2 = ' '.join(GameResultsTeam2).strip()

            if (teamName1 == teamName2):
                return (f"Error: Teams cannot have the same name. {line}", False)

            return (teamName1, teamScore1, teamName2, teamScore2), True
        except ValueError:
            return (f"Error: The game score was not available in the line. {line}", False)
        except IndexError:
            return (f"Error: The line is not in the correct format. {line}", False)    
            

    def inputGameResultsFromFile(self, fileName: str):
        """ 
        Creates a backup of current league rankings.
        Reads a file with league results
        Processes each line and and add results to game league
        The entire file will be processed but if there is a error processing of results stop
        Only errors will be printed after this point
        The Backup will be restored after lines has been read and all errors are displayed
        
        :param fileName: The team Name
        """
        
        self.__backupRankings()
        errorFound = False

        with open(fileName, "r") as file:
            for line in file:       
                result, success = self.__getGameResults(line)
                if success:
                    if(errorFound == False):
                        (team1, score1, team2, score2) = result
                        self.__addGameLeagueScore(team1, score1, team2, score2)
                else:
                    errorFound = True
                    print(result.strip())

        file.close()

        if errorFound:
            self.__restoreRankings() 
            return False
        else:
            return True          


    def inputGameResultsFromInput(self, lines: list[str]):
        """ 
        Creates a backup of current league rankings.
        Processes each line and and add results to game league
        The entire file will be process but if there is a error processing of results stop
        Only errors will be printed after this point
        The Backup will be restored after lines has been read and all errors are displayed

        :return: True when there are no errors and process was successful
        """
        self.__backupRankings()
        errorFound = False

        for line in lines:
            result, success = self.__getGameResults(line)
            if success:
                if(errorFound == False):
                    (team1, score1, team2, score2) = result
                    self.__addGameLeagueScore(team1, score1, team2, score2)
            else:
                errorFound = True
                print(result.strip())
        
        if errorFound:
            self.__restoreRankings() 
            return False
        else:
            return True
            

    def isResultsAvailable(self):
        """ 
        Check if there are any results available 

        :return: True if results are available and false if empty
        """
        if self.rankings:
            return True
        else:
            return False

    
    def __backupRankings(self):
        """
        Backup existing rankings       
        """
        self.backupRankings = self.rankings.copy()


    def __restoreRankings(self):
        """
        Restore ranking with stored backup
        """
        self.rankings = self.backupRankings.copy()


 