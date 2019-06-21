import random


class SudokuGenerator:
    def __init__(self, singleBoxLength):
        self.boxSize = singleBoxLength
        self.sideLength = self.boxSize ** 2
        self.grid = [[0 for i in range(self.sideLength)] for j in range(self.sideLength)]

    def printGrid(self):
        for row in self.grid:
            print(row)
        print("\n")

    def setGrid(self, newGrid):
        self.grid = newGrid

    # def rowValid(self, row, subRow=False):
    #     numbers = []
    #     for number in self.grid[row]:
    #         if number > 0 and number <= self.sideLength:
    #             if number in numbers:
    #                 return False
    #             else:
    #                 numbers.append(number)
    #     if not subRow:
    #         if len(numbers) == self.sideLength:
    #             return True
    #         return False
    #
    # def colValid(self, col, subCol=False):
    #     numbers = []
    #     for row in self.grid:
    #         colNum = row[col]
    #         if colNum > 0 and colNum <= self.sideLength:
    #             if colNum in numbers:
    #                 return False
    #             else:
    #                 numbers.append(colNum)
    #     if not subCol:
    #         if len(numbers) == self.sideLength:
    #             return True
    #         return False
    #
    # def boxValid(self, point, subBox=False):
    #     numbers = []
    #     startPoint = Point(self.boxSize * (int(point.x / self.boxSize)), self.boxSize * (int(point.y / self.boxSize)))
    #
    #     for x in range(startPoint.x, startPoint.x + self.boxSize):
    #         for y in range(startPoint.y, startPoint.y + self.boxSize):
    #             number = self.grid[y][x]
    #             if number > 0 and number <= self.sideLength:
    #                 if number in numbers:
    #                     return False
    #                 else:
    #                     return True
    #     if not subBox:
    #         if len(numbers) == self.sideLength:
    #             return True
    #         return False

    def getValidNumbers(self, point):
        lst1 = self.getValidNumbersRow(point)
        lst2 = self.getValidNumbersCol(point)
        lst3 = self.getValidNumbersBox(point)
        validNumbers = list(set(lst1) & set(lst2) & set(lst3))
        return validNumbers

    def getValidNumbersRow(self, point):
        allNumbers = list(range(1, self.sideLength + 1))
        for number in self.grid[point.getY()]:
            if number in allNumbers:
                allNumbers[allNumbers.index(number)] = -1

        validNumbers = []
        for i in allNumbers:
            if i > 0:
                validNumbers.append(i)

        return validNumbers

    def getValidNumbersCol(self, point):
        allNumbers = list(range(1, self.sideLength + 1))
        for row in self.grid:
            number = row[point.getX()]
            if number in allNumbers:
                allNumbers[allNumbers.index(number)] = -1

        validNumbers = []
        for i in allNumbers:
            if i > 0:
                validNumbers.append(i)

        return validNumbers

    def getValidNumbersBox(self, point):
        allNumbers = list(range(1, self.sideLength + 1))
        startPoint = Point(self.boxSize * (int(point.x / self.boxSize)), self.boxSize * (int(point.y / self.boxSize)))
        for x in range(int(startPoint.x), int(startPoint.x + self.boxSize)):
            for y in range(int(startPoint.y), int(startPoint.y + self.boxSize)):
                number = self.grid[y][x]
                if number in allNumbers:
                    allNumbers[allNumbers.index(number)] = -1

        validNumbers = []
        for i in allNumbers:
            if i > 0:
                validNumbers.append(i)

        return validNumbers

    def populateGrid(self):

        row = 0
        reset = 0;
        while row < self.sideLength:
            col = 0
            moveOn = True
            self.grid[row] = [0 for i in range(self.sideLength)]

            while col < self.sideLength:
                validNumbers = self.getValidNumbers(Point(col, row))
                if len(validNumbers) < 1:
                    moveOn = False
                    # print("fail", Point(col, row))
                    # self.printGrid()
                    reset += 1
                else:
                    self.grid[row][col] = random.choice(validNumbers)
                col += 1


            if moveOn:
                row += 1
            if reset >= 1000:
                row = 0
                self.grid = [[0 for i in range(self.sideLength)] for j in range(self.sideLength)]
                reset = 0

    def hideNumbers(self, percent):
        for row in range(0, int(self.sideLength/2) + 1):
            for col in range(0, int(self.sideLength/2) + 1):
                oppositeRow = self.sideLength - row - 1
                oppositeCol = self.sideLength - col - 1
                rand = random.random()
                if rand < percent:
                    self.grid[row][col] = -1
                    self.grid[oppositeRow][oppositeCol] = -1



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __repr__(self):
        return "x: " + str(self.x) + ", y: " + str(self.y)


gen = SudokuGenerator(3)
gen.populateGrid()
gen.hideNumbers(.5)
gen.printGrid()
# print (list(range(1, 5)))
