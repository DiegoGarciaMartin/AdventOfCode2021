import copy

class Board:

  def __init__(self, board) -> None:
    self.board = board
    self.win = False

  def checkNumber(self, n) -> bool:

    if self.win:
      return False

    for idxRow,row in enumerate(self.board):
      for idxColumn,numberBoard in enumerate(row):
        if (numberBoard.number == n):
          numberBoard.marked = True
          if self.__checkBoardRow(idxRow) or self.__checkBoardColumn(idxColumn):
            self.win = True
            return True

    return False

  def getSumUnmarkedNumbers(self) -> int:
    sum = 0
    
    for row in self.board:
      for numberBoard in row:
        if not numberBoard.marked:
          sum += numberBoard.number

    return sum

  def __checkBoardRow(self, idxRow) -> bool:
    for numberBoard in self.board[idxRow]:
      if not numberBoard.marked:
        return False
    return True

  def __checkBoardColumn(self, idxColumn) -> bool:
    for column in self.board:
      if not column[idxColumn].marked:
        return False
    return True


class BoardNumber:

  def __init__(self, number) -> None:
    self.number = number
    self.marked = False

###########################################################################

def read_data(path):
  with open(path) as f:
    return [line.rstrip("\n") for line in f.readlines() if line != "\n"]

def part1(bingoNumbers, boards) -> int:
  for number in bingoNumbers:
    for board in boards:
      if board.checkNumber(number):
        return board.getSumUnmarkedNumbers() * number

def part2(bingoNumbers, boards) -> int:
  lastBoardWin: Board = None
  lastNumberWin: int = None

  for number in bingoNumbers:
    for board in boards:
      if board.checkNumber(number):
        lastBoardWin = board
        lastNumberWin = number 
        
  return lastBoardWin.getSumUnmarkedNumbers() * lastNumberWin

if __name__ == '__main__':
  bingo = read_data('input.txt')

  bingoNumbers = [int(x) for x in bingo[0].split(',')]

  boardsStr = [bingo[i:(i+5)] for i in range(1, len(bingo), 5)]
  boards = []

  for boardStr in boardsStr:
    boards.append(Board([
      [BoardNumber(int(x)) for x in boardStr[0].split(' ') if x != ''],
      [BoardNumber(int(x)) for x in boardStr[1].split(' ') if x != ''],
      [BoardNumber(int(x)) for x in boardStr[2].split(' ') if x != ''],
      [BoardNumber(int(x)) for x in boardStr[3].split(' ') if x != ''],
      [BoardNumber(int(x)) for x in boardStr[4].split(' ') if x != ''] 
    ]))
  
  print("Result part 1: " + str(part1(bingoNumbers, copy.deepcopy(boards))))
  print("Result part 2: " + str(part2(bingoNumbers, copy.deepcopy(boards))))