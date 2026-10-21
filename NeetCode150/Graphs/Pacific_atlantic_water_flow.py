"""
Pacific Atlantic Water Flow - Medium

You are given a rectangular island heights where heights[r][c] represents the height a
bove sea level of the cell at coordinate (r, c).
The islands borders the Pacific Ocean from the top and left sides, and borders the 
Atlantic Ocean from the bottom and right sides.
Water can flow in four directions (up, down, left, or right) from a cell to a 
neighboring cell with height equal or lower. Water can also flow into the ocean from 
cells adjacent to the ocean.
Find all cells where water can flow from that cell to both the Pacific and Atlantic 
oceans. Return it as a 2D list where each element is a list [r, c] representing the 
row and column of the cell. You may return the answer in any order.

Example 1:
Input: heights = [
  [4,2,7,3,4],
  [7,4,6,4,7],
  [6,3,5,3,6]
]
Output: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]

Example 2:
Input: heights = [[1],[1]]
Output: [[0,0],[1,0]]




# Pacific Atlantic Water Flow: My Thought Process

## 1. Clarify the prompt

"Before I jump in, I want to make sure I understand the problem correctly."

"So I'm given a grid of heights.
The Pacific Ocean touches the top edge and the left edge.
The Atlantic Ocean touches the bottom edge and the right edge.
Rain can flow from a cell into a neighbor if the neighbor is the same height or lower.
I need to return every cell where water can reach both oceans."

"I have a few quick questions before I start."

"Can water only move up, down, left, and right, or diagonally too?"
→ I'll assume only 4 directions.

"If two cells have the same height, can water flow between them?"
→ I'll assume yes.

"Does the order of the cells in my output matter?"
→ I'll assume no.

"Can the grid be empty?"
→ I'll assume it has at least one row and one column.

"Okay, so for every cell, I need to answer two questions:
can its water reach the Pacific, and can it reach the Atlantic?"

## 2. Test cases

"Let me write down a few test cases before I think about the approach."

```
1 2 2 3 5
3 2 3 4 4
2 4 5 3 1
6 7 1 4 5
5 1 1 2 4
```

"Take the middle cell (2,2), which has height 5.
Water can go up and left, downhill, to the Pacific.
It can also go right and down, downhill, to the Atlantic.
So (2,2) is in the answer."

"The full answer here is
(0,4), (1,3), (1,4), (2,2), (3,0), (3,1), (4,0)."

"A few edge cases:"
- "A single cell touches every edge, so it reaches both oceans."
- "With a single row, every cell touches the top and the bottom,
  so every cell is in the answer."
- "If every height is the same, water can go anywhere,
  so every cell is in the answer."
- "The top-right and bottom-left corners touch both oceans directly."

"Do these expected outputs match what you have in mind?"

## 3. Brute force

"My first idea is the simplest one.
For each cell, I pour water on it and follow where it can go."

"I run a search from that cell, moving only to neighbors
that are the same height or lower.
If the search touches a Pacific edge and an Atlantic edge,
that cell goes in the answer."

"This works because I'm literally checking every cell, one by one."

"The time is O((N * M)^2).
There are N * M cells,
and each search can walk through the whole grid, which is another N * M."

"The space is O(N * M), for the visited set of one search."

"The problem is that I repeat a lot of work.
Cells next to each other usually flow the same way,
so their searches cover almost the same area.
And every search forgets what the last one found."

## 4. Optimal solution

"The bottleneck is searching from every single cell.
So I want to flip the question around."

"Instead of starting from every cell and asking,
'can this reach the ocean?',
I can start from the oceans and ask,
'which cells can flow down to me?'"

"Water flows downhill.
So if I walk backward, starting from the ocean,
I move uphill: I go to a neighbor only if it's the same height or higher.
Every cell I reach that way can drain into that ocean."

"I'll do this twice.
Once starting from all the Pacific edge cells,
and once starting from all the Atlantic edge cells.
The cells that show up in both searches are my answer."

"The data structure I'll use is two sets, one for each ocean,
because each set remembers which cells can reach that ocean,
and it also works as my visited set, so I never visit a cell twice."

"As I go through the edges, I start a DFS from every top-row
and left-column cell for the Pacific,
and from every bottom-row and right-column cell for the Atlantic."

"When a neighbor is inside the grid, not visited yet,
and at least as high as where I am, I move into it."

"At the end, I return the cells that are in both sets."

"The time is O(N * M).
Each search visits every cell at most once,
and I only do two searches, one per ocean."

"The space is O(N * M), for the two sets and the call stack."

"So I go from O((N * M)^2) down to O(N * M)."

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

"First, I'll make a class called Solution."

"Then a function called findFlow that takes self and heights."

"I'll store the number of rows in N and the number of columns in M.
I need these for the bounds checks."

"Next, I'll create two empty sets, pacific and atlantic.
Each one holds the cells that can drain into that ocean."

"Then I'll write a directions list with the 4 moves:
up, down, left, and right.
That way I can loop over neighbors instead of writing four separate checks."

"Now I'll define a helper called dfs that takes r, c, and visited.
I'm passing the set in as a parameter,
so I can reuse the same function for both oceans."

"First thing inside it, I add (r, c) to visited.
This marks the cell as able to reach this ocean."

"Then I loop over each direction."

"I compute the neighbor's row as r plus dr, and call it nr.
And the neighbor's column as c plus dc, and call it nc."

"Now I check four things before I move there.
First, nr is inside the grid.
Second, nc is inside the grid.
I check the bounds first, so I never index outside the grid.
Third, the neighbor isn't already in visited.
Fourth, the neighbor's height is greater than or equal to mine.
I'm going uphill because I'm walking backward from the ocean.
If water can flow from that neighbor down to me,
then that neighbor can reach the ocean too."

"If all four are true, I call dfs on the neighbor, with the same set."

"Now I start the searches from the edges."

"I loop over every column.
I call dfs on the top cell with pacific, since the top row touches the Pacific.
And I call dfs on the bottom cell with atlantic,
since the bottom row touches the Atlantic."

"Then I loop over every row.
I call dfs on the leftmost cell with pacific,
since the left column touches the Pacific.
And I call dfs on the rightmost cell with atlantic,
since the right column touches the Atlantic."

"At this point, both sets are complete."

"Finally, I return every cell in the intersection of pacific and atlantic,
as a list of [r, c] pairs.
The intersection gives me exactly the cells that can reach both oceans."

## 7. Testing

"Before I finish, I'll trace through my test cases."

- "First example: the Pacific search climbs up from the top and left edges.
  The Atlantic search climbs up from the bottom and right edges.
  (2,2) with height 5 gets reached by both searches,
  so it's in the intersection. The full list matches what I expected."
- "Single cell: it's on every edge, so both searches start from it.
  It's in both sets, so it's in the answer."
- "Single row: every cell is in both the top row and the bottom row,
  so every cell is in both sets."
- "All heights equal: the greater-than-or-equal check
  lets both searches reach everything, so every cell is in the answer."
- "Corners: the top-right is on the top edge and the right edge,
  so both searches start there."

"The output matches what I expected for all of them."

"To recap, time is O(N * M) and space is O(N * M)."

"If the grid could be really large, the recursion might hit
Python's limit of about 1000.
In that case, I'd switch to BFS,
and start each ocean's queue with all of its edge cells."
"""
class Solution:
    def findFlow(self, heights):
        N = len(heights)
        M = len(heights[0])
        pacific = set()
        atlantic = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c, visited):
            visited.add((r,c))
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)

        for c in range(M):
            dfs(0, c, pacific)
            dfs(N-1, c, pacific)

        for r in range(N):
            dfs(r, 0, pacific)
            dfs(r, M - 1, atlantic)

        return [[r,c] for (r,c) in pacific & atlantic] #common cells among pacific and atlantic