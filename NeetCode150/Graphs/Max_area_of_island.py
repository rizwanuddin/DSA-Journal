"""
Max Area of Island - Medium

You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).
An island is defined as a group of 1's connected horizontally or vertically. 
You may assume all four edges of the grid are surrounded by water.
The area of an island is defined as the number of cells within the island.
Return the maximum area of an island in grid. If no island exists, return 0.

Example 1:
Input: grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]
Output: 6
Explanation: 1's cannot be connected diagonally, so the maximum area of the island is 6.




# Max Area of Island: My Thought Process

## 1. Clarify the prompt

I want to make sure I understand the problem correctly.
I'm given an N by M grid of 1s (land) and 0s (water).
An island is a group of land cells connected to each other.
The area of an island is the number of cells in it.
I need to return the area of the biggest island.

Quick questions:
- Are connections only up, down, left, and right? I'll assume yes, 4 directions.
- Are the values integers 1 and 0? I'll assume yes.
- If there's no land at all, is the answer 0? I'll assume yes.
- Can I modify the grid? I'll assume no, so I'll use a visited set.
- Can the grid be empty? I'll assume it has at least one row and one column.

So I'm finding every connected component of land,
measuring its size, and returning the largest one.

## 2. Test cases

```
1 1 0 0
1 0 0 1
0 0 1 1
0 0 0 1
```
The top-left island has 3 cells.
The right island has (1,3), (2,2), (2,3), (3,3), so 4 cells.
Answer: 4.

- All water: answer is 0.
- All land: answer is N * M.
- Single "1": answer is 1.
- Cells touching only diagonally: they are separate islands.

## 3. Brute force

My first idea is to start a search from every land cell.
Each search counts how many cells are reachable from that cell.
I take the biggest count I see.

Time: O((N * M)^2).
- There can be N * M land cells.
- Each search can visit all N * M cells.

Space: O(N * M) for the visited set of one search.

Why it's slow:
- Every cell in the same island runs the same search,
  and gets the same area.
- One search per island is enough.

## 4. Optimal solution

Instead of searching from every land cell,
I can search once per island, and mark every cell it reaches.

The data structure I will use is a visited set of (row, col) pairs,
plus DFS with the recursion stack,
because DFS reaches every cell in an island,
and the set stops me from counting a cell twice.

The key part is having DFS return the area.
Each call counts its own cell as 1,
then adds the areas returned by its unvisited land neighbors.
So the first call returns the size of the whole island.

As I go through every cell, I check if it's land and not visited.

When I find one, it's a new island.
I run DFS from it, and compare the area it returns with my best so far.

At the end, I return the best area.

Time: O(N * M)
- Each cell is visited by DFS at most once.
- Each visit checks 4 neighbors, which is constant.
- The outer loops scan every cell once.

Space: O(N * M)
- The visited set can hold every cell.
- The call stack can go N * M deep for one long winding island.

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

First I make a class called Solution.

Then I make a function called maxAreaIsland that takes self and grid.

I store the number of rows in N and the number of columns in M.
I need these for the bounds checks.

Then I create an empty set called visited.
It holds (row, col) pairs for land cells I've already counted.

Then I set max_area to 0.
It's 0 and not something negative,
because if there's no land, the answer should be 0.

Next I write a list called directions with the 4 moves:
up, left, right, and down.

Now I define an inner function called dfs that takes r and c.
It returns the area of the island that contains this cell.

First thing inside it, I add (r, c) to visited.
I mark it right away, so no other path counts it again.

Then I set area to 1.
That's for this cell itself.

Then I loop over each dr, dc in directions.

I compute the neighbor's row as r + dr, and store it in nr.
And the neighbor's column as c + dc, and store it in nc.

Then I check four things before going there.
First, nr is between 0 and N - 1.
Second, nc is between 0 and M - 1.
I check the bounds first, so I never index outside the grid.
Third, grid[nr][nc] is 1, so it's land.
Fourth, (nr, nc) is not in visited.

If all four are true, I call dfs on the neighbor,
and add what it returns to area.
That's the area of the part of the island reached through that neighbor.

After the loop, I return area.
So each call hands its total back up to the call that made it.

After defining dfs, I loop r over every row, and c over every column.

For each cell, I check if it's 1 and not in visited.
If so, it's a new island.
I call dfs on it, which returns that island's area.
I set max_area to the bigger of max_area and that area.
After the call, the whole island is in visited,
so the loops skip the rest of its cells.

When the loops end, every island has been measured,
and I return max_area.

## 7. Testing

Before I finish, I'll run my test cases.
- First example: DFS from (0,0) returns 3, so max_area is 3.
  The next new land is (1,3).
  DFS goes to (2,3), then (2,2) and (3,3), and returns 4.
  max_area becomes 4, which matches.
- All water: no DFS runs, the answer is 0.
- All land: one DFS reaches every cell, the answer is N * M.
- Single "1": DFS returns 1.
- Diagonal-only cells: no straight neighbor connects them,
  so each one is its own island with area 1.

If the grid could be large, the recursion could hit Python's limit of about 1000.
In that case I would use BFS with a queue,
and count each cell as I take it out.
"""
class Solution:
    def maxAreaIsland(self, grid):
        N = len(grid)
        M = len(grid[0])
        visited = set()
        max_area = 0
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

        def dfs(r, c):
            visited.add((r, c))
            area = 1
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < N and 0 <= nc < M
                        and grid[nr][nc] == 1
                        and (nr, nc) not in visited):
                    area += dfs(nr, nc)
            return area

        for r in range(N):
            for c in range(M):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, dfs(r, c))

        return max_area