class EntryNote:

  def __init__(self, patterns: list[str], output: list[str]) -> None:
    self.patterns = patterns
    self.output = output

class SevenSegmentDisplayDecoder:

# Position of the segments in display
#   aaaa  
#  b    c
#  b    c
#   dddd
#  e    f
#  e    f
#   gggg 

  def __init__(self, entry: EntryNote) -> None:
    self.entry = entry
    self.letterSegmentA = None
    self.letterSegmentB = None
    self.letterSegmentC = None
    self.letterSegmentD = None
    self.letterSegmentE = None
    self.letterSegmentF = None
    self.letterSegmentG = None
    self.outputValue = 0

    self.__decodeEntry()
    self.__decodeOutputValue()

  def __findElementsByLenght(self, searchList: list[str], lenght: int) -> list[str]:
    return [ele for ele in searchList if len(ele) == lenght]

  def __decodeEntry(self) -> None:

    # Set letters C and F (the order can be wrong)
    numOnePattern: str = self.__findElementsByLenght(self.entry.patterns, 2)[0]
    self.letterSegmentC = numOnePattern[0]
    self.letterSegmentF = numOnePattern[1]

    # Set letter A using number 7
    numSevenPattern: str = self.__findElementsByLenght(self.entry.patterns, 3)[0]
    numSevenPattern = numSevenPattern.replace(self.letterSegmentC, '').replace(self.letterSegmentF, '')
    self.letterSegmentA = numSevenPattern
  
    # Set letters B, D and G using numbers 4 and 3
    numFourPattern: str = self.__findElementsByLenght(self.entry.patterns, 4)[0]
    numFourPattern = numFourPattern.replace(self.letterSegmentC, '').replace(self.letterSegmentF, '')

    segmentsLen5Patterns: list[str] = self.__findElementsByLenght(self.entry.patterns, 5) # Numbers 2,3,5

    for idx,s in enumerate(segmentsLen5Patterns):
      segmentsLen5Patterns[idx] = s.replace(self.letterSegmentA, '').replace(self.letterSegmentC, '').replace(self.letterSegmentF, '')

    numThreePattern: str = self.__findElementsByLenght(segmentsLen5Patterns, 2)[0]
    segmentsLen5Patterns.remove(numThreePattern)

    if numFourPattern[0] == numThreePattern[0]:
      self.letterSegmentD = numFourPattern[0]
      self.letterSegmentB = numFourPattern[1]
      self.letterSegmentG = numThreePattern[1]
    elif numFourPattern[0] == numThreePattern[1]:
      self.letterSegmentD = numFourPattern[0]
      self.letterSegmentB = numFourPattern[1]
      self.letterSegmentG = numThreePattern[0]
    elif numFourPattern[1] == numThreePattern[1]:
      self.letterSegmentD = numFourPattern[1]
      self.letterSegmentB = numFourPattern[0]
      self.letterSegmentG = numThreePattern[0]
    elif numFourPattern[1] == numThreePattern[0]:
      self.letterSegmentD = numFourPattern[1]
      self.letterSegmentB = numFourPattern[0]
      self.letterSegmentG = numThreePattern[1]

    # Set letter E using number 2
    for idx,s in enumerate(segmentsLen5Patterns):
      segmentsLen5Patterns[idx] = s.replace(self.letterSegmentB, '').replace(self.letterSegmentD, '').replace(self.letterSegmentG, '')

    numTwoPattern: str = self.__findElementsByLenght(segmentsLen5Patterns, 1)[0]
    self.letterSegmentE = numTwoPattern
    
    # Check the order of the letters C and F using number 6
    segmentsLen6Patterns: list[str] = self.__findElementsByLenght(self.entry.patterns, 6) # Numbers 0,6,9

    for idx,s in enumerate(segmentsLen6Patterns):
      segmentsLen6Patterns[idx] = s.replace(self.letterSegmentA, '').replace(self.letterSegmentB, '').replace(self.letterSegmentD, '').replace(self.letterSegmentE, '').replace(self.letterSegmentG, '')

    numSixPattern: str = self.__findElementsByLenght(segmentsLen6Patterns, 1)[0]

    if numSixPattern != self.letterSegmentF:
      self.letterSegmentC = self.letterSegmentF
      self.letterSegmentF = numSixPattern

  def __decodeOutputValue(self) -> None:
    outputValueStr: str = ''

    for out in self.entry.output:
      if len(out) == 2:
        outputValueStr += '1'
      elif len(out) == 3:
        outputValueStr += '7'
      elif len(out) == 4:
        outputValueStr += '4'
      elif len(out) == 7:
        outputValueStr += '8'
      elif len(out) == 5 and out.find(self.letterSegmentC) != -1 and out.find(self.letterSegmentE) != -1:
        outputValueStr += '2'
      elif len(out) == 5 and out.find(self.letterSegmentC) != -1 and out.find(self.letterSegmentF) != -1:
        outputValueStr += '3'
      elif len(out) == 5 and out.find(self.letterSegmentB) != -1 and out.find(self.letterSegmentF) != -1:
        outputValueStr += '5'
      elif len(out) == 6 and out.find(self.letterSegmentD) == -1:
        outputValueStr += '0'
      elif len(out) == 6 and out.find(self.letterSegmentC) == -1:
        outputValueStr += '6'
      elif len(out) == 6 and out.find(self.letterSegmentE) == -1:
        outputValueStr += '9'

    self.outputValue = int(outputValueStr)


###################################################################################


def parseEntryNote(entryStr: str) -> EntryNote:
  return EntryNote(
    entryStr.split('|')[0].strip().split(' '),
    entryStr.split('|')[1].strip().split(' ')
  )

def read_data(path) -> list[EntryNote]:
  with open(path) as f:
    return [parseEntryNote(line.rstrip("\n")) for line in f.readlines()]

def part1(entry_notes: list[EntryNote]) -> int:

  outputs_knowed: int = 0

  for entry in entry_notes:
    outputs_knowed += sum(len(output) in [2,3,4,7] for output in entry.output)

  return outputs_knowed

def part2(entry_notes: list[EntryNote]) -> int:

  outputSums: int = 0

  for entry in entry_notes:
    displayDecoder: SevenSegmentDisplayDecoder = SevenSegmentDisplayDecoder(entry)
    outputSums += displayDecoder.outputValue

  return outputSums

if __name__ == '__main__':
  entry_notes: list[EntryNote] = read_data('input.txt')
  print("Result part 1: " + str(part1(entry_notes)))
  print("Result part 2: " + str(part2(entry_notes)))