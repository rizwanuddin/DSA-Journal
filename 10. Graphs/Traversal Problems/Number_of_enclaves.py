"""
Number of enclaves - Medium

Given an N x M binary matrix grid, where 0 represents a sea cell and 1 represents a land cell. 
A move consists of walking from one land cell to another adjacent (4-directionally) land cell 
or walking off the boundary of the grid. Find the number of land cells in the grid for which we 
cannot walk off the boundary of the grid in any number of moves.

Example 1:
Input: grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
Output: 3
Explanation:
The highlighted cells represents the land cells.

Example 2:
Input: grid = [[0, 0, 0, 1],[0, 0, 0, 1], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
Output:3
Explanation:
The highlighted cells represents the land cells.




# Number of Enclaves: My Thought Process

## 1. Clarify the prompt

I want to make sure I understand the problem correctly.
I'm given an N by M grid of 1s (land) and 0s (sea).
From a land cell, I can walk to an adjacent land cell,
or walk off the grid if I'm on the border.
I need to return how many land cells can never walk off the grid.

Quick questions:
- Are moves only up, down, left, and right? I'll assume yes, 4 directions.
- Are the values integers 1 and 0? I'll assume yes.
- Do I count cells, or islands? I'll assume cells.
- Can I modify the grid? I'll assume no, so I'll use a visited set.
- Can the grid be empty? I'll assume it has at least one row and one column.

So any land cell connected to the border can escape.
I'm counting the land cells that are not connected to the border.

## 2. Test cases

```
0 0 0 0
1 0 1 0
0 1 1 0
0 0 0 0
```
The 1 at (1,0) is on the border, so it can escape.
The group at (1,2), (2,1), (2,2) never touches the border.
Answer: 3.

- All land: everything connects to the border, answer is 0.
- All water: answer is 0.
- Single row or single column: every cell is on the border, answer is 0.
- Land inside that touches border land: it can escape, so it's not counted.

## 3. Brute force

My first idea is to check every land cell on its own.
For each land cell, I run a search to see if it can reach the border.
If it can't, I count it.

Time: O((N * M)^2).
- There can be N * M land cells.
- Each search can visit all N * M cells.

Space: O(N * M) for the visited set of one search.

Why it's slow:
- Cells in the same island repeat the same search over and over.
- The answer is the same for every cell in an island,
  so one search per island should be enough.

## 4. Optimal solution

Instead of asking every cell whether it can reach the border,
I can flip the question and start from the border.

Any land on the border can escape.
Any land connected to that border land can also escape.
So I search inward from every border land cell, and mark everything I reach.
Whatever land is left unmarked is trapped.

The data structure I will use is a visited set of (row, col) pairs,
plus DFS with the recursion stack,
because DFS reaches every cell connected to a starting cell,
and the set stops me from visiting a cell twice.

As I go through the grid, I check each cell on the border.

When a border cell is land and not visited, I run DFS from it,
to mark every land cell connected to it.

After that, I go through the whole grid again.
When a cell is land and not visited, it can't reach the border, so I count it.

At the end, I return the count.

Time: O(N * M)
- Each cell is visited by DFS at most once.
- Each visit checks 4 neighbors, which is constant.
- The two full scans of the grid are O(N * M) each.

Space: O(N * M)
- The visited set can hold every cell.
- The call stack can go N * M deep for one long winding island.

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

First I make a class called Solution.

Then I make a function called numberOfEnclaves that takes self and grid.

Before anything else, I store the number of rows in N and the number of columns in M.
I need these for the bounds checks and to know where the border is.

Then I create an empty set called visited.
It holds (row, col) pairs for every land cell that can escape.

Next I write a list called directions with the 4 moves:
up, down, left, and right.
This lets me loop over neighbors instead of writing 4 separate checks.

Now I define an inner function called dfs that takes r and c.
It marks every land cell connected to this one as able to escape.

First thing inside it, I add (r, c) to visited.
I mark it right away, so no other path visits it again.

Then I loop over each dr, dc in directions.

I compute the neighbor's row as r + dr, and store it in nr.
And the neighbor's column as c + dc, and store it in nc.

Then I check four things before going there.
First, nr is between 0 and N - 1.
Second, nc is between 0 and M - 1.
I check the bounds first, so I never index outside the grid.
Third, grid[nr][nc] is 1, so it's land.
Fourth, (nr, nc) is not in visited.
If all four are true, I call dfs on the neighbor.

After defining dfs, I loop r over every row, and c over every column.

For each cell, I compute on_border.
It's true if r is the first or last row, or c is the first or last column.

Then I check if the cell is on the border, is land, and is not visited.
If so, I call dfs on it.
That marks every land cell that can reach the border through this cell.

Now everything that can escape is in visited.

Next I set count to 0.

Then I loop over every cell again.
If a cell is land and not in visited, it can't reach the border.
So I add 1 to count.

And finally I return count.

## 7. Testing

Before I finish, I'll run my test cases.
- First example: the only border land is (1,0).
  DFS marks it, but its neighbors are all water.
  In the second scan, (1,2), (2,1), and (2,2) are land and unvisited.
  The answer is 3, which matches.
- All land: DFS from the border reaches everything, the answer is 0.
- All water: no DFS runs, and nothing is counted, the answer is 0.
- Single row or column: every cell is on the border,
  so every land cell gets marked, the answer is 0.
- Inner land touching border land: DFS reaches it from the border,
  so it's marked and not counted.

If the grid could be large, the recursion could hit Python's limit of about 1000.
In that case I would use BFS with a queue,
starting with every border land cell in the queue at once.
"""
class Solution:
    def numberOfEnclaves(self, grid):
        N = len(grid)
        M = len(grid[0])
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c):
            visited.add((r, c))
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < N and 0 <= nc < M
                        and grid[nr][nc] == 1
                        and (nr, nc) not in visited):
                    dfs(nr, nc)

        for r in range(N):
            for c in range(M):
                on_border = r == 0 or r == N - 1 or c == 0 or c == M - 1
                if on_border and grid[r][c] == 1 and (r, c) not in visited:
                    dfs(r, c)

        count = 0
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 1 and (r, c) not in visited:
                    count += 1

        return count
