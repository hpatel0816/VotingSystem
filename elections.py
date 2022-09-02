#Elections

from input import getInput
import randomElectionData as red
import electionFunctions as election

#Global variables
maxVoters = 100
maxCandidates = 9

#Class to store candidate info
class Candidate():
  def __init__(self, name):
    self.name = name
    self.votes = 0
    self.eliminated = False

  def addVote(self):
    self.votes += 1

  def eliminate(self):
    self.eliminated = True


def initializeElection():
  #Get number of voters and candidates
  while True:
    voterNum = getInput('integer', "\nEnter the number of voters: ")
    candidateNum = getInput('integer', "Enter the number of candidates: ")
    if voterNum <= maxVoters and candidateNum <= maxCandidates:
      break
    else:
      print(f"\nYour input exceeds the limit. (Max {maxVoters} voters. Max {maxCandidates} candidates.)")
  print("\n")

  #Get the candidates to vote on
  candidateList = []
  for i in range(candidateNum):
    candidateName = getInput('string', f"Enter candidate #{i+1}:")
    candidate = Candidate(candidateName)
    candidateList.append(candidate)
  return voterNum, candidateNum, candidateList
  
  
def generalElection(votingType):
  #Get election info
  voterNum, candidateNum, candidateList = initializeElection()

  if votingType == 1:
    #Get user entered votes
    print("\n")
    for i in range(voterNum):
      choice = getInput('string', f'Voter #{i+1} preference: ')
      if any(candidate.name == choice for candidate in candidateList):
        election.generalVote(i, choice, candidateNum, candidateList)
    
  elif votingType == 2:
    #Generate random election data
    electionData = red.generateData(candidateList, candidateNum, voterNum, 'generalElection')
    for i in range(voterNum):
      election.generalVote(i, electionData[i], candidateNum, candidateList)

  #Determine election winner
  election.findWinner(voterNum, candidateNum, candidateList, 'generalElection')


def runOffElection(votingType):
  ##Initialize array for preferences (Max 1000 voters, Max 9 candidates)
  preferences = [[0 for i in range(maxCandidates)] for j in range(maxVoters)]

  #Get election info
  voterNum, candidateNum, candidateList = initializeElection()

  if votingType == 1:
    #Get user entered votes
    voter = 0
    while voter < voterNum:
      print(f"\nVoter {voter + 1}")
      candidate = 0
      while candidate < candidateNum:
        choice = getInput('string', f"Rank {candidate + 1}: ")
        if any(candidate.name == choice for candidate in candidateList):
          election.runOffVote(voter, candidate, choice, candidateNum, candidateList, preferences)
          candidate += 1
        else:
          print("\nDoesn't match a candidate.\n")

      voter += 1

  elif votingType == 2:
    #Generate random election data
    electionData = red.generateData(candidateList, candidateNum, voterNum, 'runOffElection')
    #Vote based on preferences
    for i in range(voterNum):
      for j in range(candidateNum):
        election.runOffVote(i, j, electionData[i][j], candidateNum, candidateList, preferences)

 
  print("\n")
  
  while True:
    #Calculate votes
    election.tabulate(voterNum, candidateNum, candidateList, preferences)
    
    #Check for winner
    won = election.findWinner(voterNum, candidateNum, candidateList, 'runOffElection')
    if won:
      break

    #Get candidate with lowest votes
    min = election.findMin(voterNum, candidateNum, candidateList)

    #Check for tie
    tie = election.isTie(min, candidateNum, candidateList)
    if (tie):
      userChoice = getInput('integer', """\nThe voting is tied. 
    Press 1 to see all winners. 
    Press 2 to rerun voting.
    Enter your choice: """)
      if userChoice == 1:
        print("\nWinners:")
        #Print all winners
        for i in range(candidateNum):
          if not candidateList[i].eliminated:
            print(candidateList[i].name)
        break
      elif userChoice == 2:
        runOffElection(votingType)
      else:
        print("An error occured")

    #Eliminate the last-place candidate
    election.eliminate(min, candidateNum, candidateList)

    #Reset votes for runoff
    for i in range(candidateNum):
      candidateList[i].votes = 0

   