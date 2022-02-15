# My approach

# O(2n) Time | O(k) Space
def tournamentWinner(competitions, results):
	winCount = 0
	array = []
	for index, result in enumerate(results): 
		if result == 0:
			array.append(competitions[index][1])
		elif result == 1:
			array.append(competitions[index][0])
	hashTable = {team:array.count(team) for team in array}
	winningTeam = max(hashTable, key=hashTable.get)
	return winningTeam

# AlgoExpert approach

homeTeamHasWon = 1
# O(n) Time | O(k) Space
def tournamentWinner(competitions, results):
	currentBestTeam = ""
	scores = {currentBestTeam: 0}

	for idx, competition in enumerate(competitions):
		result = results[idx]
		homeTeam, awayTeam = competition

		winningTeam = homeTeam if homeTeamHasWon == result else awayTeam

		updateScore(winningTeam, 3, scores)

		if scores[winningTeam] > scores[currentBestTeam]:
			currentBestTeam = winningTeam

	return currentBestTeam

def updateScore(team, points, hashTable):
	if team not in hashTable:
		hashTable[team] = 0

	hashTable[team] += points