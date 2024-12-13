def maxAreaOfIsland(grid: list[list[int]]) -> int:
    if not grid or not grid[0]:
        return 0
    visited = set()
    rows, cols = len(grid), len(grid[0])
    max_area = 0

    def dfs(r, c):
        if (
                r not in range(rows) or
                c not in range(cols) or
                (r, c) in visited or
                grid[r][c] == 0
        ):
            return 0
        visited.add((r, c))
        return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(c + 1, r) + dfs(c - 1, r)

    for r in range(rows):
        for c in range(cols):
            max_area = max(max_area, dfs(r, c))

    return max_area


grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

print(maxAreaOfIsland(grid))
