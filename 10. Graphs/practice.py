"""Connected Components"""
class Solution:

    def adjBuild(self, V, edges):
        adj = []
        for i in range(V):
            adj.append([])
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return adj

    def connectedComp(self, V, edges):
        adj = self.adjBuild()
        visited = set()
        count = 0

        def dfs(node):
            visited.add(node)
            for neighbour in adj[node]:
                if neighbour not in visited:
                    dfs(neighbour)

        for i in range(V):
            if i not in visited:
                count += 1
                dfs(i)

        return count




"""Traversal Techniques"""
from collections import deque
class Solution:

    def adjBuild(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return adj

    def dfs(self, V, edges):
        adj = self.adjBuild(V, edges)
        visited = set()
        ans = []
        def helper(node):
            visited.add(node)
            ans.append(node)
            for neighbour in adj[node]:
                if neighbour not in visited:
                    helper(neighbour)
        helper(0)
        return ans

    def bfs(self, V, edges):
        adj = self.adjBuild(V, edges)
        queue = deque([0])
        ans = []
        visited = set()
        while queue:
            node = queue.popleft()
            ans.append(node)
            for neighbour in adj[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        return ans





"""Flood Fill Algorithm"""
class Solution:

    def floodFill(self, image, sr, sc, newColor):
        original = image[sr][sc]
        if original == newColor:
            return image
        N = len(image)
        M = len(image[0])
        direction = [      (-1,0),          
                    (0,-1),      (0,1),
                            (1,0)        ]
        def dfs(r, c):
            image[r][c] = newColor
            for dr, dc in direction:
                nr = r + dr
                nc = r + dc
                if (0 <= nr < N and 0 <= nc < M and original == image[nr][nc]):
                    dfs(nr, nc)
        dfs(sr, sc)
        return image





"""Number Of Enclaves"""
class Solution:

    def numberOfEnclaves(self, grid):
        N = len(grid)                                        # O(1)
        M = len(grid[0])                                     # O(1)
        visited = set()                                       # SPACE O(N*M): worst case every cell is land
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]        # O(1): always 4 directions

        def dfs(r, c):
            visited.add((r, c))                                # O(1)
            for dr, dc in directions:                          # O(1): constant 4 checks
                nr = r + dr
                nc = c + dc
                if (0 <= nr < N and 0 <= nc < M and grid[nr][nc] == "1" and (nr, nc) not in visited):
                    dfs(nr, nc)

        for r in range(N):                                     # TIME O(N*M): visit each cell once
            for c in range(M):
                on_border = r == 0 or c == 0 or r == N - 1 or c == M - 1
                if on_border and grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)

        count = 0
        for r in range(N):                                     # TIME O(N*M): second full scan
            for c in range(M):
                if grid[r][c] == "1" and (r, c) not in visited:
                    count += 1

        return count





"""Number of Islands"""
class Solution:
    def noOfIslands(self, grid):
        N = len(grid)
        M = len(grid[0])
        visited = set()
        count = 0

        directions = [(-1,-1), (-1,0), (-1,1),
                      (0,-1),          (0,1),
                      (1,-1),  (1,0),  (1,1)]

        def dfs(r, c):
            visited.add((r, c))
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < N and 0 <= nc < M
                        and grid[nr][nc] == "1"
                        and (nr, nc) not in visited):
                    dfs(nr, nc)

        for r in range(N):
            for c in range(M):
                if grid[r][c] == "1" and (r, c) not in visited:
                    count += 1
                    dfs(r, c)

        return count





"""Number of Provinces"""
class Solution:

    def noOfProvince(self, adj):
        V = len(adj)
        visited = set()
        count = 0

        def dfs(node):
            visited.add(node)
            for j in range(V):
                if adj[node][j] == 1 and j not in visited:
                    dfs(j)

        for i in range(V):
            if i not in visited:
                count += 1
                dfs(i)
        return count





"""Rotten Oranges"""
from collections import deque

from collections import deque

class Solution:

    def TimeToRot(self, grid):
        N = len(grid)                                          # O(1)
        M = len(grid[0])                                       # O(1)
        fresh = 0
        queue = deque()                                          # SPACE O(N*M): worst case all cells rotten at once
        minTime = 0

        for r in range(N):                                       # TIME O(N*M): scan every cell once
            for c in range(M):
                if grid[r][c] == 1:
                    fresh += 1                                    # O(1)
                elif grid[r][c] == 2:
                    queue.append((r, c))                          # O(1)

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]            # O(1): constant 4 directions

        while queue and fresh > 0:                                  # TIME O(N*M)
            size = len(queue)                                      # O(1): snapshot size for this minute
            for _ in range(size):
                r, c = queue.popleft()                              # O(1)
                for dr, dc in directions:                           # O(1): constant 4 checks
                    nr = r + dr
                    nc = c + dc
                    if (0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 1):
                        queue.append((nr, nc))                       # O(1)
                        grid[nr][nc] = 2                              # O(1): marks visited by turning rotten
                        fresh -= 1                                    # O(1)
            minTime += 1                                             # O(1): one full level = one minute

        if fresh > 0:
            return -1
        return minTime

# TOTAL TIME:  O(N*M) [initial scan] + O(N*M) [BFS, each cell enqueued/processed once] = O(N*M)
# TOTAL SPACE: O(N*M) [queue, worst case every cell is rotten] = O(N*M)
        



         

