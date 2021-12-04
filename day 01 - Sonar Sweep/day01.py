def read_data(path):
  with open(path) as f:
    return [int(x) for x in f.readlines()]

def part1(listMeasurements: list) -> int:
  return len([i for i in range(len(listMeasurements) - 1) if (listMeasurements[i] < listMeasurements[i + 1])])

def part2(listMeasurements: list) -> int:
  sumsGroups = [sum(listMeasurements[i:i+3]) for i in range(len(listMeasurements) - 2)]
  return part1(sumsGroups)

if __name__ == '__main__':
  listMeasurements = read_data('input.txt')
  print("Result part 1: " + str(part1(listMeasurements)))
  print("Result part 2: " + str(part2(listMeasurements)))