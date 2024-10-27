"""
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

    rows represented by m
    columns represented by n

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.

"""


def numIslands(grid: list[list[str]]) -> int:
    # return zero if the grid is empty
    if not grid or not grid[0]:
        return 0

    # number of islands identified
    islands = 0
    # grid node already visited
    visit = set()
    # grid search size
    rows, cols = len(grid), len(grid[0])

    # this depth first search algorythm
    # will recursively take avery node which represent land
    # as well as all adjacent nodes that represent land
    # until all adjacent nodes that represent land are
    # identified as one land mass
    def dfs(r, c):
        # if the node is out of range
        # or the node = "0" (water)
        # or the node has been already visited
        # exit the search
        if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visit
        ):
            return

        # otherwise
        # add the node to the visited set
        visit.add((r, c))
        # define the direction of search
        # up [0,1] down [0,-1] right [1,0] left [-1,0]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # for all adjacent nodes in each direction defined
        # execute a dfs on those nodes
        for ar, ac in directions:
            # execute recursive call to depth fist search
            dfs(r + ar, c + ac)

    # for each node in the grid
    for r in range(rows):
        for c in range(cols):
            # if the node is "1" and has not being visited yet
            if grid[r][c] == "1" and (r, c) not in visit:
                # add island count
                islands += 1
                # execute dfs on each adjacent node
                dfs(r, c)
    # return the number of island counted
    return islands


grid = [["0", "0", "1", "0"],
        ["1", "1", "0", "0"],
        ["0", "0", "0", "1"],
        ["0", "1", "0", "0"]]

print(numIslands(grid))
