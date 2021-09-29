#Prompt and validate user input
def getInput(inputType, promptTxt):
  #Repeat until input is valid
  while True:
    try:
      #integer prompt
      if inputType == 'integer':
        userInput = int(input(promptTxt))
        if not userInput:
          raise ValueError('empty input')
        return userInput
      #string prompt
      elif inputType == 'string':
        userInput = input(promptTxt)
        if not userInput:
          raise ValueError()
        if any(char.isdigit() for char in userInput):
          print("***Enter a valid string.***\n")
        else:
          return userInput
    except ValueError:
      print(f"\n***Enter a valid {inputType}.***\n")
    except:
      print("An error occured.")