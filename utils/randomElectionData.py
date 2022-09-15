import random

def generateData(candidateArr, candidates, voters, electionType):
  nameArr = []
  #Get candidate names 
  for i in range(candidates):
    nameArr.append(candidateArr[i].name)
  
  print("\nRandom Election Data:")
  print("--------------------")

  if electionType == 'generalElection':
    choiceArr = []
    #For each voter, randomly vote for a candidate
    for voter in range(voters):
      choice = random.choice(nameArr)
      print(f"Voter {voter+1} voted for {choice}.")
      choiceArr.append(choice)

    return choiceArr

  if electionType == 'runOffElection':
    rankArr = []
    #Randomly shuffle names and append to ranking arrays to reflect peoples choices
    for voter in range(voters):
      random.shuffle(nameArr)
      print(f"\nVoter {voter+1}:")
      for index, name in enumerate(nameArr):
        print(f"Rank {index+1}: {name}")
      rankArr.append(nameArr[:])

    return rankArr