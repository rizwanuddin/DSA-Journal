"""
Number of Islands - Medium

Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.
An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. 
You may assume water is surrounding the grid (i.e., all the edges are water).

Example 1:
Input: grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
Output: 1

Example 2:
Input: grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
Output: 4




# Number of Islands (8 Directions): My Thought Process

## 1. Clarify the prompt

I want to make sure I understand the problem correctly.
I'm given an N by M grid of "1"s (land) and "0"s (water).
An island is a group of land cells connected to each other.
I need to return the number of islands.

Quick questions:
- Do diagonal cells count as connected? I'll assume yes, all 8 directions.
- Are the values strings "1" and "0", or integers? I'll assume strings.
- Can the grid be empty? I'll assume it has at least one row and one column.
- Can I modify the grid? I'll assume no, so I'll track visited cells separately.

So I'm counting connected components, where each land cell is a node
and its neighbors are the 8 cells around it.

## 2. Test cases

```
1 1 0 0
0 1 0 0
0 0 1 0
1 0 0 0
```
The top-left group and the middle 1 touch diagonally, so they're one island.
The bottom-left 1 is alone. Answer: 2.

- All water: answer is 0.
- All land: answer is 1.
- Checkerboard of 1s and 0s: every 1 touches another diagonally, answer is 1.
- Single cell "1": answer is 1.
- Land on the edges and corners: must not go out of bounds.

## 3. Brute force

My first idea is to check every pair of land cells.
For each pair, I search the grid to see if one can reach the other.
Then I group cells that can reach each other, and count the groups.

Time: O((N * M)^3) in the worst case.
- There are up to (N * M)^2 pairs of land cells.
- Each search can visit all N * M cells.

Space: O(N * M) for the visited set of one search.

Why it's slow:
- Every search explores the same island again and again.
- Once I search from one cell, I already know its whole island.

## 4. Optimal solution

Instead of checking every pair of cells,
I can start one search per island, and mark every cell it reaches.

The data structure I will use is a visited set of (row, col) pairs,
plus DFS with the recursion stack,
because DFS reaches every cell in an island,
and the set stops me from visiting a cell twice.

As I go through every cell, row by row, I check if it's land and not visited.

When I find one, it's a new island.
I add 1 to the count, and run DFS from it to mark the whole island.

Inside DFS, I check all 8 neighbors.
When a neighbor is in bounds, is land, and isn't visited, I go into it.

At the end, I return the count.

Time: O(N * M)
- Each cell is visited at most once by DFS.
- Each visit checks 8 neighbors, which is constant.
- The outer loops scan every cell once.

Space: O(N * M)
- The visited set can hold every cell.
- The call stack can go N * M deep if the whole grid is one snake-shaped island.

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

First I make a class called Solution.

Then I make a function called noOfIslands that takes self and grid.

Before anything else, I store the number of rows in N and the number of columns in M.
I need these for the bounds checks.

Then I create an empty set called visited.
It holds (row, col) pairs, because a cell is identified by two numbers.

Then I set count to 0.
This counts the islands.

Next I write a list called directions with the 8 moves.
Each one is a change in row and a change in column.
That includes up, down, left, right, and the 4 diagonals.
Writing them as a list lets me loop over neighbors instead of writing 8 if statements.

Now I define an inner function called dfs that takes r and c.
It marks every cell in this island as visited.

First thing inside it, I add (r, c) to visited.
I mark it right away, so no other path can visit it again.

Then I loop over each dr, dc in directions.

I compute the neighbor's row as r + dr, and store it in nr.
And the neighbor's column as c + dc, and store it in nc.

Then I check four things before going there.
First, nr is between 0 and N - 1.
Second, nc is between 0 and M - 1.
I check the bounds first, so I never index outside the grid.
Third, grid[nr][nc] is "1", so it's land.
Fourth, (nr, nc) is not in visited, so I haven't been there.
If all four are true, I call dfs on the neighbor, which goes deeper.

After defining dfs, I loop r over every row, and c over every column.

For each cell, I check if it's "1" and not in visited.
If so, it's part of an island I haven't counted yet.
I add 1 to count, and call dfs on it.
After that call, the whole island is in visited,
so the loops skip the rest of its cells.

When the loops end, every cell has been checked, and I return count.

## 7. Testing

Before I finish, I'll run my test cases.
- First example: (0,0) is new land, count is 1.
  DFS marks (0,0), (0,1), (1,1), then (2,2) through the diagonal.
  The next unvisited land is (3,0), count is 2.
  The answer is 2, which matches.
- All water: the if never passes, the answer is 0.
- All land: the first DFS reaches everything, the answer is 1.
- Checkerboard: diagonals connect every 1, the answer is 1.
- Single "1": count is 1, DFS has no valid neighbors.
- Edge and corner cells: the bounds check runs before indexing, so no crash.

If the grid could be large, the recursion could hit Python's limit of about 1000.
In that case I would use BFS with a queue instead.
If 4-directional connectivity were asked,
I'd only change the directions list to the 4 straight moves.
"""
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
                