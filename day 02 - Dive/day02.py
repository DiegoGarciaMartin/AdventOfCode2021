def read_data(path):
  with open(path) as f:
    commands = [line.rstrip("\n").split(" ") for line in f.readlines()]
  return [[command[0], int(command[1])] for command in commands]

def part1(listCommands: list) -> int:
  
  horizontalPosition = 0
  depth = 0

  for command in listCommands:
    if (command[0] == "forward"):
      horizontalPosition += command[1]
    elif (command[0] == "down"):
      depth += command[1]
    elif (command[0] == "up"):
      depth -= command[1]

  return horizontalPosition * depth

def part2(listCommands: list) -> int:
  
  horizontalPosition = 0
  depth = 0
  aim = 0

  for command in listCommands:
    if (command[0] == "forward"):
      horizontalPosition += command[1]
      depth += (aim * command[1])
    elif (command[0] == "down"):
      aim += command[1]
    elif (command[0] == "up"):
      aim -= command[1]

  return horizontalPosition * depth


if __name__ == '__main__':
  listCommands = read_data('input.txt')
  print("Result part 1: " + str(part1(listCommands)))
  print("Result part 2: " + str(part2(listCommands)))