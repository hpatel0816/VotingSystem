from input import getInput
import fppVoting
import runOffVoting

def Welcome():
  print("Welcome to the Voting System.\n")

  votingSystem = getInput('integer',"""What voting system do you want: \n
  1. First-past-the-post
  2. Runoff\n
  Enter your choice: """)

  votingType = getInput('integer', """\nWhat kind of voting do you want: \n
  1. User-entered voting
  2. Randomly generated voting\n
  Enter your choice: """)

  if votingSystem == 1:
    fppVoting.fppVoting(votingType)
  elif votingSystem == 2:
    runOffVoting.runOffVoting(votingType)
  else:
    print("An error occured.")

if __name__ == "__main__":
  Welcome()

'''Check and validateuser id

only people with voting id can vote'''