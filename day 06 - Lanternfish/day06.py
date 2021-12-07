def read_data(path) -> list[str]:
  with open(path) as f:
    return [int(timerStr) for timerStr in f.readline().rstrip("\n").split(',')]

def simulate_lanternfish_days(lanternfishTimers: list[int], days: int):
  fish_count = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
  }

  for fishTimer in lanternfishTimers:
    fish_count[fishTimer] += 1

  for _ in range(days):
    new_fishes = fish_count[0]
    for fishTimer in range(0, 8):
      fish_count[fishTimer] = fish_count[fishTimer + 1]

    fish_count[6] += new_fishes
    fish_count[8] = new_fishes

  return sum(fish_count.values())

if __name__ == '__main__':
  lanternfishTimers: list[int] = read_data('input.txt')   
  print("Result part 1: " + str(simulate_lanternfish_days(lanternfishTimers, 80)))
  print("Result part 2: " + str(simulate_lanternfish_days(lanternfishTimers, 256)))