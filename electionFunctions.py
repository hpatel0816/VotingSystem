#Functions to mandate elections

def generalVote(voter, choice, candidateCount, candidateArr):
  for i in range(candidateCount):
    if candidateArr[i].name == choice:
      candidateArr[i].addVote()


def runOffVote(voter, rank, choice, candidateCount, candidateArr, preferences):
  for i in range(candidateCount):
    if candidateArr[i].name == choice:
      preferences[voter][rank] = i
      return True
  return False


def tabulate(voterCount, candidateCount, candidateArr, preferences):
  for i in range(voterCount):
    for j in range(candidateCount):
      if candidateArr[preferences[i][j]].eliminated == False:
        candidateArr[preferences[i][j]].addVote()
        break
    

def findWinner(voterCount, candidateCount, candidateArr, electionType):
  if electionType == 'generalElection':
    mostVotes = max(candidate.votes for candidate in candidateArr)

    #print(mostVotes)
    winner = []
    for i in candidateArr:
      if i.votes == mostVotes:
        winner.append(i.name)

    if len(winner) == 1:
      print(f"\nThe winner is {winner[0]}")
    else:
      print("\nWinners:")
      for i in winner:
        print(i)

  elif electionType == 'runOffElection':
    votesToWin = voterCount / 2

    #Find person with most votes (>50)
    for i in range(candidateCount):
      if candidateArr[i].votes > votesToWin:
        print(f"The winner is: {candidateArr[i].name}")
        return True
    return False
  else:
    print("An error occured.")


def findMin(voterCount, candidateCount, candidateArr):
  lowest = voterCount
  for i in range(candidateCount):
    if candidateArr[i].eliminated == False and candidateArr[i].votes < lowest:
      lowest = candidateArr[i].votes
  return lowest


def isTie(minVotes, candidateCount, candidateArr):
  for i in range(candidateCount):
    if candidateArr[i].eliminated == False and candidateArr[i].votes != minVotes:
      return False
  return True


def eliminate(minVotes, candidateCount, candidateArr):
  for i in range(candidateCount):
    if candidateArr[i].eliminated == False and candidateArr[i].votes == minVotes:
      candidateArr[i].eliminate()
      print(f"{candidateArr[i].name} got eliminated.")