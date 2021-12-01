def read_data(path):
  with open(path) as f:
    return [int(x) for x in f.readlines()]

def part1(listMeasurements: list):
  numberOfIncreases = len([i for i in range(len(listMeasurements) - 1) if (listMeasurements[i] < listMeasurements[i + 1])])
  print('Number of increases: ' + str(numberOfIncreases))

def part2(listMeasurements: list):
  sumsGroups = [sum(listMeasurements[i:i+3]) for i in range(len(listMeasurements) - 2)]
  part1(sumsGroups)

if __name__ == '__main__':
  listMeasurements = read_data('input.txt')
  part1(listMeasurements)
  part2(listMeasurements)