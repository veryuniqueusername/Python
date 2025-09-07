def create_empty_grid(size):
    return [[0 for _ in range(size)] for _ in range(size)]


def can_place(grid, x, y, size):
    n = len(grid)
    if x + size > n or y + size > n:
        return False
    for i in range(size):
        for j in range(size):
            if grid[y + i][x + j] != 0:
                return False
    return True


def place_tile(grid, x, y, size, tile_id):
    for i in range(size):
        for j in range(size):
            grid[y + i][x + j] = tile_id


def remove_tile(grid, x, y, size):
    for i in range(size):
        for j in range(size):
            grid[y + i][x + j] = 0


def find_next_empty(grid):
    for y in range(len(grid)):
        for x in range(len(grid)):
            if grid[y][x] == 0:
                return x, y
    return None, None


def backtrack(grid, tiles, index):
    if index == len(tiles):
        return True  # All tiles placed

    size, count = tiles[index]
    for _ in range(count):
        for y in range(len(grid)):
            for x in range(len(grid)):
                if can_place(grid, x, y, size):
                    tile_id = size  # Use size as tile ID
                    place_tile(grid, x, y, size, tile_id)
                    if backtrack(grid, tiles[:index] + [(size, count - 1)] + tiles[index + 1:], index):
                        return True
                    remove_tile(grid, x, y, size)
        return False  # Could not place current tile
    return backtrack(grid, tiles, index + 1)  # Move to next tile size


def solve_partridge_square(n):
    side_length = n * (n + 1) // 2
    grid = create_empty_grid(side_length)

    # Prepare tile list: (size, count), largest first
    tiles = [(size, size) for size in range(n, 0, -1)]

    print(f"Trying to tile a {side_length}×{side_length} grid with:")
    for size, count in tiles:
        print(f"  {count} tile(s) of size {size}×{size}")

    success = backtrack(grid, tiles, 0)
    if success:
        print("Solution found:")
        for row in grid:
            print(" ".join(f"{cell:2}" if cell else "__" for cell in row))
    else:
        print("No solution found.")


if __name__ == "__main__":
    n = 8
    solve_partridge_square(n)
