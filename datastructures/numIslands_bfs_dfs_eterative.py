"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
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
import collections


def numIslands(grid: list[list[str]]) -> int:
    #  return zero if the grid is empty
    if not grid or not grid[0]:
        return 0

    # visited nodes in the grid
    visited = set()
    # number of islands identified
    islands = 0
    # size of the grid
    rows, cols = len(grid), len(grid[0])

    # this breath first search algorythm
    # will recursively take avery node which represent land
    # as well as all adjacent nodes that represent land
    # until all adjacent nodes that represent land are
    # identified as one land mass
    # Also because of the use of a double ended queue
    # which is a generalization of a stack and a queue
    # by changing the direction of the pop function
    # the same code can be use as a depth first search algorithm
    # bfs: queue like behaviour FIFO
    # dfs: stack like behaviour LIFO
    def bfs(r, c):
        # defining a double ended queue
        q = collections.deque()
        # adding the node being visited the the visited set
        visited.add((r, c))
        # appending the node visited to the queue
        q.append((r, c))
        # while the queue is not empty
        while q:
            # popleft the node
            row, col = q.popleft() # bfs (FIFO first in first out)
            # row, col = q.pop() # dfs (LIFO last in first out)
            # defined the allow directions right left top down
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            # for every adjacent node to the right left top down
            for ar, ac in directions:
                # define the coordinated to be adjacent node to the right left top down
                r, c, = row + ar, col + ac
                # as long as the node coordinated is in the grid range
                # for r and c and the node is land (value of "1") and
                # the node has not yet been visited
                if (
                        r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visited
                ):
                    # add the node coordinated to the queue
                    q.append((r, c))
                    # added to the visited set
                    visited.add((r, c))

    # for every node in the grid
    for r in range(rows):
        for c in range(cols):
            # if the node represents land (value of "1")
            # and the node has not been visited
            if grid[r][c] == "1" and (r, c) not in visited:
                # count an island
                islands += 1
                # add the node to the visited set
                visited.add((r, c))
                # and execute a bfs against the adjacent nodes
                bfs(r, c)

    # return the number of islands found
    return islands


grid = [["0", "0", "1", "0"],
        ["1", "1", "0", "0"],
        ["0", "0", "0", "1"],
        ["0", "1", "0", "0"]]

print(numIslands(grid))