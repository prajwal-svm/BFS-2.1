# 994. Rotting Oranges

# Time Complexity: O(m*n)
# Space Complexity: O(m*n)
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No


# BFS Intuition:
# Use a queue to traverse the grid level by level.
# Keep track of the number of fresh oranges and the number of minutes elapsed.
# If a fresh orange is adjacent to a rotten orange, it becomes rotten and the number of fresh oranges is decremented.
# Return the number of minutes elapsed when there are no fresh oranges left.

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        queue = deque()
        fresh = 0
        time = 0    

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0
        
        while queue:
            size = len(queue)
            for _ in range(size):
                x,y = queue.popleft()
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nx,ny = x+dx,y+dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx,ny))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1

# DFS Intuition:
# Use a recursive function to traverse the grid.
# Keep track of the number of fresh oranges and the number of minutes elapsed.
# If a fresh orange is adjacent to a rotten orange, it becomes rotten and the number of fresh oranges is decremented.
# Return the number of minutes elapsed when there are no fresh oranges left.

class Solution:
    def __init__(self):
        self.dirs = [[0,1], [1,0], [-1,0], [0,-1]]  

    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    self.dfs(grid, i, j, m, n, 2)

        max_time = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
                max_time = max(max_time, grid[i][j])

        if max_time == 0:
            return 0
        return max_time - 2

    def dfs(self, grid, i, j, m, n, time):
        # base case
        if i < 0 or j < 0 or i == m or j == n:
            return
        # if the orange is not fresh or the time is less than the current time, means it has already been visited
        if grid[i][j] != 1 and grid[i][j] < time:
            return

        # logic: make the orange rotten and set the time
        grid[i][j] = time

        # traverse the adjacent oranges
        for dr, dc in self.dirs:
            nr, nc = i + dr, j + dc
            self.dfs(grid, nr, nc, m, n, time + 1)
        