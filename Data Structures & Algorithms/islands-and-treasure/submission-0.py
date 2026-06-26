from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()

        # first add all the gates(0) to queue
        for r in range(rows):
            for c in range(cols):
               if grid[r][c] == 0:
                queue.append((r, c)) 
        
        distance = 0
        while queue:
            distance+=1

            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                    new_r = r + dr
                    new_c = c + dc

                    if new_r < 0 or new_c < 0 or new_r >= rows or new_c >= cols:
                        continue
                    if grid[new_r][new_c] != 2147483647:
                        continue

                    grid[new_r][new_c] = distance
                    queue.append((new_r, new_c))
        
        