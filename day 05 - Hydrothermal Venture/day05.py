class Coordinates:
  def __init__(self, x: int, y: int) -> None:
    self.x = x
    self.y = y

  def str(self) -> str:
    return str(self.x) + ',' + str(self.y)


class LineSegment:
  def __init__(self, c1: Coordinates, c2: Coordinates) -> None:
    self.c1 = c1
    self.c2 = c2

  def get_cover_points(self) -> list[Coordinates]:

    if self.c1.x == self.c2.x:
      yMin: int = self.c1.y if self.c1.y <= self.c2.y else self.c2.y
      yMax: int = self.c1.y if self.c1.y > self.c2.y else self.c2.y
      return [Coordinates(self.c1.x, y) for y in range(yMin, yMax + 1, 1)] 
    elif self.c1.y == self.c2.y:
      xMin: int = self.c1.x if self.c1.x < self.c2.x else self.c2.x
      xMax: int = self.c1.x if self.c1.x > self.c2.x else self.c2.x
      return [Coordinates(x, self.c1.y) for x in range(xMin, xMax + 1, 1)]
    else:
      return [] 


  def get_cover_points_all(self) -> list[Coordinates]:

    if self.c1.x == self.c2.x:
      yMin: int = self.c1.y if self.c1.y <= self.c2.y else self.c2.y
      yMax: int = self.c1.y if self.c1.y > self.c2.y else self.c2.y
      return [Coordinates(self.c1.x, y) for y in range(yMin, yMax + 1, 1)] 
    elif self.c1.y == self.c2.y:
      xMin: int = self.c1.x if self.c1.x < self.c2.x else self.c2.x
      xMax: int = self.c1.x if self.c1.x > self.c2.x else self.c2.x
      return [Coordinates(x, self.c1.y) for x in range(xMin, xMax + 1, 1)]
    else:

      rangeStop: int = self.c1.x - self.c2.x if self.c1.x >= self.c2.x else self.c2.x - self.c1.x 
      xIncrement: int = 1 if self.c1.x <= self.c2.x else -1 
      yIncrement: int = 1 if self.c1.y <= self.c2.y else -1 

      return [Coordinates(self.c1.x + (xIncrement * i), self.c1.y + (yIncrement * i)) for i in range(0, rangeStop + 1, 1)] 


##############################################################################


def read_data(path) -> list[LineSegment]:
  with open(path) as f:
    return [parse_line(line.rstrip("\n")) for line in f.readlines() if line != "\n"]

def parse_line(line: str) -> LineSegment:
  coordenatesStr = line.replace(' ', '').split('->')
  coordenates1 = coordenatesStr[0].split(',')
  coordenates2 = coordenatesStr[1].split(',')

  return LineSegment(
    Coordinates(int(coordenates1[0]),int(coordenates1[1])), 
    Coordinates(int(coordenates2[0]),int(coordenates2[1]))
  )

def part1(ventsLines: list[LineSegment]) -> int:

  coverPointsCount: dict[str, int] = {}

  for l in ventsLines:
    for p in l.get_cover_points():
      if coverPointsCount.get(p.str()) != None:
        coverPointsCount.update({p.str(): coverPointsCount.get(p.str()) + 1})
      else:
        coverPointsCount.update({p.str(): 1}) 

  return len([v for v in coverPointsCount.values() if v > 1])

def part2(ventsLines: list[LineSegment]) -> int:

  coverPointsCount: dict[str, int] = {}

  for l in ventsLines:
    for p in l.get_cover_points_all():
      if coverPointsCount.get(p.str()) != None:
        coverPointsCount.update({p.str(): coverPointsCount.get(p.str()) + 1})
      else:
        coverPointsCount.update({p.str(): 1}) 

  return len([v for v in coverPointsCount.values() if v > 1])

if __name__ == '__main__':
  ventsLines: list[LineSegment] = read_data('input.txt')   
  print("Result part 1: " + str(part1(ventsLines))) 
  print("Result part 2: " + str(part2(ventsLines)))