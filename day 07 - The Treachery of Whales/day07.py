def read_data(path) -> list[str]:
  with open(path) as f:
    return [int(pos) for pos in f.readline().rstrip("\n").split(',')]

def calculate_fuel(pos: int, crab_positions: list[int]) -> int:
  return sum(abs(n - pos) for n in crab_positions)

def part1(crab_positions: list[int]) -> int:

  pos_min: int = min(crab_positions)
  pos_max: int = max(crab_positions)

  fuel = calculate_fuel(pos_min, crab_positions)

  for pos in range(pos_min + 1, pos_max + 1):
    fuel = min(fuel, calculate_fuel(pos, crab_positions))

  return fuel

def calculate_fuel2(pos: int, crab_positions: list[int]) -> int:

  fuel: int = 0

  for crabPos in crab_positions:
    fuel += abs(pos - crabPos) * (abs(pos - crabPos) + 1) // 2

  return fuel

def part2(crab_positions: list[int]) -> int:

  pos_min: int = min(crab_positions)
  pos_max: int = max(crab_positions)

  fuel = calculate_fuel2(pos_min, crab_positions)

  for pos in range(pos_min + 1, pos_max + 1):
    fuel = min(fuel, calculate_fuel2(pos, crab_positions))

  return fuel

if __name__ == '__main__':
  crab_positions: list[int] = read_data('input.txt')
  print("Result part 1: " + str(part1(crab_positions)))
  print("Result part 2: " + str(part2(crab_positions)))