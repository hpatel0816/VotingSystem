import fppVoting
import runOffVoting

def Welcome():
  print("Welcome to the Voting System.\n")

  votingSystem = int(input("""What voting system do you want: \n
  1. First-past-the-post
  2. Runoff\n
  Enter your choice: """))

  '''voterNum = int(input("\nHow many voters in the election (Max: 1000): "))
  candidates = int(input("How many candidates in the election (Max: 10): "))'''

  votingType = int(input("""\nWhat kind of voting do you want: \next
  1. User-entered votingSystem
  2. Randomly generated voting\n
  Enter your choice: """))

  if votingSystem == 1:
    fppVoting.fppVoting(votingType)
  elif votingSystem == 2:
    runOffVoting.runOffVoting(votingType)
  else:
    print("An error occured.")

if __name__ == "__main__":
  Welcome()