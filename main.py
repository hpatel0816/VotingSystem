from utils.input import getInput
from election import elections

def Welcome():
  print("Welcome to the Voting System.\n")

  #Initialize program functionality
  while True:
    votingSystem = getInput('integer',"""What voting system do you want: \n
    1. General Election
    2. Runoff Election\n
    Enter your choice: """)

    if votingSystem == 1 or votingSystem == 2:
      break
    else:
      print("\nEnter a valid input.\n\n")

  while True:
    votingType = getInput('integer', """\nWhat kind of voting do you want: \n
    1. User-entered voting
    2. Randomly generated voting\n
    Enter your choice: """)

    if votingType == 1 or votingType == 2:
      break
    else:
      print("\nEnter a valid input.\n\n")

  #Run election type
  if votingSystem == 1:
    elections.generalElection(votingType)
  elif votingSystem == 2:
    elections.runOffElection(votingType)
  else:
    print("\nAn error occured.")

if __name__ == "__main__":
  Welcome()
