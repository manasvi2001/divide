import random

class Divide:
  def __init__(self, size):
    self.score = 0
    self.size = size
    self.layout = [[0 for i in range(self.size)] for j in range(self.size)]
    self.indices = [0, 0]
    self.primes = [2,3,5,7,11,13,17,19]
    self.numbersOnBoard = []
    self.currentNumber = 0
    self.temporaryNumber = 0

  def startGame(self):
    self.indices = self.randomIndices()
    self.currentNumber = self.generateNumber(True)
    self.updateLayout()
    while 1:
      self.gameLoop()

  def isGameOver(self):
    for row in self.layout:
      for cell in row:
        if cell == 0:
          return False
    return True

  def printMatrix(self):
    for row in self.layout:
      print(row)

  def divideNumbers(self, a, b):
    if (b == 0):
      return a
    return a//b

  def isDivisible(self, a, b):
    if (b == 0):
      return False
    return a%b == 0

  def generateNumber(self, isFirst):
    # Return a random generated number
    if isFirst:
      return random.choice(self.primes)
    else:
      self.extractNumbersOnBoard()
      numbersToChooseFrom = [[i for num in self.numbersOnBoard for i in range(num, 101, num)], self.primes]
      randomList = random.choices(numbersToChooseFrom, weights=(70, 30), k=1)[0]
      return random.choice(randomList)

  def randomIndices(self):
    return [random.randint(1, self.size), random.randint(1, self.size)]

  def extractNumbersOnBoard(self):
    self.numbersOnBoard = [i for rows in self.layout for i in rows if i!=0]

  def updateLayout(self):
    self.layout[self.indices[0] - 1][self.indices[1] - 1] = self.currentNumber
    self.checkAndReduce()

  def checkAndReduce(self):
    for _ in range(self.size):
      for i in range(self.size):
        for j in range(self.size):
          if self.layout[i][j] == 0:
            continue
          else:
            if (i-1 >= 0 and self.isDivisible(self.layout[i][j], self.layout[i-1][j])):
              self.layout[i][j] = self.divideNumbers(self.layout[i][j], self.layout[i-1][j])
              self.layout[i-1][j] = 0
              self.score += 1
            if (j-1 >= 0 and self.isDivisible(self.layout[i][j], self.layout[i][j-1])):
              self.layout[i][j] = self.divideNumbers(self.layout[i][j], self.layout[i][j-1])
              self.layout[i][j-1] = 0
              self.score += 1
            if (i+1 < self.size and self.isDivisible(self.layout[i][j], self.layout[i+1][j])):
              self.layout[i][j] = self.divideNumbers(self.layout[i][j], self.layout[i+1][j])
              self.layout[i+1][j] = 0
              self.score += 1
            if (j+1 < self.size and self.isDivisible(self.layout[i][j], self.layout[i][j+1])):
              self.layout[i][j] = self.divideNumbers(self.layout[i][j], self.layout[i][j+1])
              self.layout[i][j+1] = 0
              self.score += 1

  def takeInput(self):
    self.indices = input("Enter row and column (1 2): ")
    self.indices = self.indices.split()
    self.indices = [int(i) for i in self.indices]
    for i in self.indices:
      if int(i) < 1 or int(i) > self.size:
        print("Invalid cell position")
        return True
    if self.layout[self.indices[0] - 1][self.indices[1] - 1] != 0:
      print("Number already present in this cell")
      return True
    return False

  def gameLoop(self):
    self.printMatrix()
    print("Your score: %d"% (self.score))
    if (self.isGameOver()):
      print("You played well. Try beating the score. Final score: %d"% (self.score))
      if (input("Do you want to play again?(Y/N): ") == 'Y'):
        self.startGame()
      else:
        exit()
    else:
      self.currentNumber = self.generateNumber(False)
      print("Next number to put on board: %d"% (self.currentNumber))
      while self.takeInput():
        pass
      self.updateLayout()
    # Generate Random Number
    # Enter indices and check validity
    return 0

size = 0
while (size < 3 or size > 6):
  size = int(input("Enter size of game board (3-6): "))

divide = Divide(size)
divide.startGame()