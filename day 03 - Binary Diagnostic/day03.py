def read_data(path):
  with open(path) as f:
    # //commands = [line.rstrip("\n").split(" ") for line in f.readlines()]
    return [line.rstrip("\n") for line in f.readlines()]

def part1(diagnosticReport: list) -> int:
  gammaRate = ''
  epsilonRate = ''

  for index in range(len(diagnosticReport[0])):
    listBitsAtPositionIdx = [n[index] for n in diagnosticReport]
    countZero = listBitsAtPositionIdx.count('0')
    countOne = listBitsAtPositionIdx.count('1')

    if (countZero > countOne):
      gammaRate += '0'
      epsilonRate += '1'
    else:
      gammaRate += '1'
      epsilonRate += '0'

  return int(gammaRate, 2) * int(epsilonRate, 2)

def part2(diagnosticReport: list) -> int:

  oxygenGeneratorRatingSublist = diagnosticReport.copy()
  co2ScrubberRatingSublist = diagnosticReport.copy()

  for index in range(len(diagnosticReport[0])):

    # Oxygen Generator Rating
    if(len(oxygenGeneratorRatingSublist) > 1):
      listBitsOxygenAtPositionIdx = [n[index] for n in oxygenGeneratorRatingSublist]
      countZero = listBitsOxygenAtPositionIdx.count('0')
      countOne = listBitsOxygenAtPositionIdx.count('1')

      if countOne >= countZero:
        oxygenGeneratorRatingSublist = [n for n in oxygenGeneratorRatingSublist if n[index] == '1']
      else:
        oxygenGeneratorRatingSublist = [n for n in oxygenGeneratorRatingSublist if n[index] == '0']

    # CO2 Scrubber Rating
    if(len(co2ScrubberRatingSublist) > 1):
      listBitsCO2AtPositionIdx = [n[index] for n in co2ScrubberRatingSublist]
      countZero = listBitsCO2AtPositionIdx.count('0')
      countOne = listBitsCO2AtPositionIdx.count('1')

      if countOne < countZero :
        co2ScrubberRatingSublist = [n for n in co2ScrubberRatingSublist if n[index] == '1']
      else:
        co2ScrubberRatingSublist = [n for n in co2ScrubberRatingSublist if n[index] == '0']

  return int(oxygenGeneratorRatingSublist[0], 2) * int(co2ScrubberRatingSublist[0], 2)


if __name__ == '__main__':
  diagnosticReport = read_data('input.txt')
  print("Result part 1: " + str(part1(diagnosticReport)))
  print("Result part 2: " + str(part2(diagnosticReport)))