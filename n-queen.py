import time

n = int(input("n: "))

start_time = time.perf_counter()

def print_grid(cols: list[int]):
  size = len(cols)
  numbers = "  |"
  separator = "----" * (size + 1)
  for i in range(1, size + 1):
    numbers += f" {i} |"
  print(numbers)
  print(separator)

  char = 65 # A
  for j in range(0, size):
    print(f"{chr(char+j)}{' |  ' * (cols[j] - 1)} | ~{' |  ' * (size - cols[j])} |")
    print(separator)

def possible(grid: list[int]) -> bool:
  n_grid = [*grid] # grid that doesn't mutate outside
  length = len(n_grid)
  while 0 in n_grid:
    n_grid.remove(0)
  
  if len(n_grid) == len(set(n_grid)):
    for i in range(1, min(length - n_grid[-1], len(n_grid)) + 1):
      pos = [len(n_grid) - i, n_grid[-1] + i]
      if n_grid[pos[0] - 1] == pos[1]:
        return False
    for i in range(1, min(n_grid[-1], len(n_grid))):
      pos = [len(n_grid) - i, n_grid[-1] - i]
      if n_grid[pos[0] - 1] == pos[1]:
        return False
    return True
  return False

def create_grid(size: int) -> list[int]:
  grid: list[int] = [0] * size
  return grid

def queen(grid: list[int], row: int) -> list[int]:
  while True:
    if row > len(grid):
      break
    r = row - 1
    grid[r] += 1
    if grid[r] > n:
      grid[r] = 0
      row -= 1
    elif possible(grid):
      row += 1
  return grid

def queen_arr(grid: list[int], row: int) -> list[list[int]]:
  arr: list[list[int]] = []
  while True:
    r = row - 1
    if row > len(grid):
      arr.append([*grid])
      grid[r - 1] += 1
      row -= 1
      continue
    grid[r] += 1
    if grid[r] > n:
      grid[r] = 0
      row -= 1
    elif possible(grid):
      row += 1
    if grid[0] == len(grid) and grid[1] == len(grid):
      break
  return arr


grid = create_grid(n)
short_time = time.perf_counter()
columns: list[int] = queen(grid, 1)
print_grid(columns)
print(columns)

# arr = queen_arr(create_grid(n), 1)
# print(len(arr), "different combinations")

print("%.5f" % (time.perf_counter() - start_time), "seconds")

# print_arr: str = input("print all the combinations? (y/n)\n")
# if print_arr == "y":
#   for i in arr:
#     print("\n")
#     print_grid(i)