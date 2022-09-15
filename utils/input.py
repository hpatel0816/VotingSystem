#Prompt and validate user input
def getInput(inputType, promptTxt):
  #Repeat until input is valid
  while True:
    try:
      #integer prompt
      if inputType == 'integer':
        userInput = int(input(promptTxt))
        return userInput
      #string prompt
      elif inputType == 'string':
        userInput = input(promptTxt)
        return userInput
    except ValueError:
      print(f"\n***Enter a valid {inputType}.***\n")
    except:
      print("An error occured.")