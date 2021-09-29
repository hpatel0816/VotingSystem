#Runoff Voting Project
import randomElectionData as red
from input import getInput

#Initialize array for preferences (Max 100 voters, Max 9 categories)
preferences = [[0 for i in range(5)]for j in range(3)]

class Category():
  def __init__(self, name):
    self.name = name
    self.votes = 0
    self.eliminated = False

def vote(voter, rank, choice, categoryCount, categoryArr):
  for i in range(categoryCount):
    if categoryArr[i].name == choice:
      preferences[voter][rank] += i


def tabulate(voterCount, categoryCount, categoryArr):
  for i in range(voterCount):
    for j in range(categoryCount):
      if categoryArr[preferences[i][j]].eliminated == False:
        categoryArr[preferences[i][j]].votes += 1
        break
    
def findWinner(voterCount, categoryCount, categoryArr):
  votesToWin = voterCount / 2
  #Find person with most votes (>50)
  for i in range(categoryCount):
    if categoryArr[i].votes > votesToWin:
      print(f"The winner is: {categoryArr[i].name}")
      return True

  return False

def findMin(voterCount, categoryCount, categoryArr):
  lowest = voterCount
  
  for i in range(categoryCount):
    if categoryArr[i].eliminated == False and categoryArr[i].votes < lowest:
      lowest = categoryArr[i].votes

  return lowest

def isTie(minVotes, categoryCount, categoryArr):
  for i in range(categoryCount):
    if categoryArr[i].eliminated == False and categoryArr[i].votes != minVotes:
      return False
  
  return True

def eliminate(minVotes, categoryCount, categoryArr):
  last = minVotes
  for i in range(categoryCount):
    if categoryArr[i].votes == last:
      categoryArr[i].eliminated == True


def runOffVoting(votingType):
  #Get user input on voters and category
  voterNum = getInput('integer', "\nEnter the number of voters: ")
  categoryNum = getInput('integer', "Enter the number of categories: ")

  #Get the categories to vote on
  categoryList = []
  for i in range(categoryNum):
    categoryName = getInput('string', f"Enter category #{i+1}:")
    category = Category(categoryName)
    categoryList.append(category)

  if votingType == 1:
    #Get user entered votes
    voter = 0
    while voter < voterNum:
      print(f"\nVoter {voter + 1}")
      category = 0
      while category < categoryNum:
        choice = getInput('string', f"Rank {category + 1}: ")
        if any(category.name == choice for category in categoryList):
          vote(voter, category, choice, categoryNum, categoryList)
          category += 1
        else:
          print("\nDoesn't match a category.\n")

      voter += 1

  elif votingType == 2:
    #Generate random election data
    electionData = red.generateData(categoryList, categoryNum, voterNum)
    #Vote based on preferences
    for i in range(voterNum):
      for j in range(categoryNum):
        vote(i, j, electionData[i][j], categoryNum, categoryList)

 
  while True:
    #Calculate votes
    tabulate(voterNum, categoryNum, categoryList)

    #Check for winner
    won = findWinner(voterNum, categoryNum, categoryList)
    if won:
      break

    #Get category with lowest votes
    min = findMin(voterNum, categoryNum, categoryList)

    #Check for tie
    tie = isTie(min, categoryNum, categoryList)
    if (tie):
      userChoice = getInput('integer', """\nThe voting is tied. 
    Press 1 to see all winners. 
    Press 2 to rerun voting.
    Enter your choice: """)
      if userChoice == 1:
        print("\nWinners:")
        for i in range(categoryNum):
          if not categoryList[i].eliminated:
            print(categoryList[i].name)
        break
      elif userChoice == 2:
        runOffVoting(votingType)
      else:
        print("An error occured")

    #Eliminate the last-place category
    eliminate(min, categoryNum, categoryList)

    #Reset votes for runoff
    for i in range(categoryNum):
      categoryList[i].votes = 0

   