import random

def generateData(categoryArr, categories, voters):
  nameArr = []
  for i in range(categories):
    nameArr.append(categoryArr[i].name)

  rankArr = []
  for i in range(voters):
    random.shuffle(nameArr)
    rankArr.append(nameArr[:])

  return rankArr
