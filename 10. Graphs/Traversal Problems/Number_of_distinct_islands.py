"""
Number of distinct islands

You are given a 2D matrix grid of size N × M, where each cell contains either 0 or 1. Find the number of distinct islands where a group of connected 1s 
(horizontally or vertically) forms an island. Two islands are considered to be same if and only if one island is equal to another (not rotated or reflected).

Example 1:
Input: grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1],[0, 0, 0, 1, 1]]
Output: 1
Explanation:
Same colored islands are equal. We have 2 equal islands, so we have only 1 distinct island.

Example 2:
Input: grid = [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1],[1, 1, 0, 1, 1]]
Output: 3
Explanation:
Same colored islands are equal. We have 4 islands, but 2 of them are equal, So we have 3 distinct islands..





# Number of Distinct Islands: My Thought Process

## What is the problem exactly stating?

"So what is the problem exactly stating?
It is stating that I'll be given a grid of 0s and 1s.
A group of 1s connected up, down, left, or right is an island.
I need to count how many islands have a different shape.
Two islands have the same shape if I can slide one on top of the other
without rotating or flipping it."

"Quick things I'd confirm:
are islands connected only in 4 directions? I'll assume yes, no diagonals.
Does a rotated island count as the same shape? I'll assume no, only sliding.
Can the grid have no islands? I'll assume yes, and then the answer is 0."

"So the real question is:
how do I check if two islands are the same shape?"

## Brute force

"So if this problem comes up in an interview,
what is the extreme naive solution I can think of?"

"I'll find every island with a DFS, and collect its cells.
To compare shapes, I need to ignore where the island is,
so I'll subtract the island's first cell from every cell.
Now every island is a list of relative positions."

"Then I keep a list of all the unique shapes I've seen so far.
For every new island, I compare its shape against every shape in that list,
one by one.
If it matches none of them, I add it to the list."

"At the end, the size of the list is my answer. Quite simple."

### Time complexity

"Now what will be the time complexity?"

"To ease out computations, I'll say the grid has N rows and M columns,
so there are N into M cells.
Let I be the number of islands, and S be the size of the biggest island."

"First portion, finding all the islands with DFS.
Each cell is visited once, so that's big O of N into M."

"Next portion, the comparisons.
Every island is compared against up to I stored shapes,
and each comparison can look at up to S cells.
So this is I into I into S."

"So the overall time complexity is N into M, plus I square into S.
In the worst case, there are lots of different small islands,
so this gets near about big O of (N into M) square."

### Space complexity

"Am I using any extra space?
The visited set and the stored shapes both hold up to N into M cells.
So the space is big O of N into M."

"Obviously the interviewer will not be happy with this,
because I'm comparing every island against a whole list, one by one,
and he'll ask me to optimize."

## Optimal

"Here's the key thing I notice.
The slow part is searching the list of shapes.
What data structure answers 'have I seen this before?' in big O of 1?
A set, right?"

"But a set needs something hashable.
So I need to turn each island's shape into something I can put in a set.
A list can't go in a set, but a tuple can.
So I'll freeze the list of relative positions into a tuple."

"Now, one thing I have to be careful about.
For two islands with the same shape,
the list of positions has to come out exactly the same, in the same order.
Can I make sure of that? I can, with two things."

"First, I always start the DFS from the first cell I find
while scanning row by row.
That's always the top-most, then left-most cell of the island.
So for the same shape, the start cell is always the same relative cell."

"Second, I always check the 4 directions in the same fixed order.
So the DFS walks through the island in the same order every time."

"So the same shape always gives the same list, agreed?
And two different shapes always give different lists,
because their sets of cells are different."

"So I'll use DFS, a visited set, and a set of shapes.
In case you don't know about a set, nothing to worry about.
Just remember, it only keeps unique items, and checking is big O of 1."

"What is the next step?
I scan the grid.
When I find a 1 that isn't visited, it's a new island.
I make a fresh empty list, and run DFS from that cell."

"Inside DFS, I mark the cell as visited,
and I add its position relative to the start cell:
the row minus the start row, and the column minus the start column.
Then I go to the 4 neighbors that are 1s and not visited."

"When DFS finishes, I turn the list into a tuple,
and add it to the shapes set.
If I've seen the shape before, the set just ignores it."

"At the end, I return the size of the set. Done and dusted."

### Time complexity

"Now let's discuss the time complexity."

"First portion, the scan of the grid.
Two loops over every cell, that's N into M."

"Next portion, all the DFS calls.
Each cell is added to visited only once,
so all the DFS calls together visit at most N into M cells.
Each visit checks 4 neighbors, which is constant,
and adds one position to a list, which is big O of 1.
So that's big O of N into M."

"Next portion, putting each shape into the set.
Turning a list into a tuple, and hashing it,
takes time equal to the island's size.
And if I add up the sizes of all the islands,
that's at most N into M, because each cell is in only one island.
So this portion is also big O of N into M."

"So the overall time complexity is
N into M, plus N into M, plus N into M,
which is nothing but big O of N into M."

"If I compare with the brute force,
that was near about (N into M) square in the worst case.
Now it's just N into M, because the set check is big O of 1."

### Space complexity

"What about the space complexity?
The visited set holds up to N into M cells.
The shapes set stores every unique shape.
In the worst case, all the islands are different,
and together they hold at most N into M positions.
So that's big O of N into M."

"The recursion stack can also go N into M deep,
if the whole grid is one long winding island.
That's big O of N into M too."

"So the overall space is big O of N into M."

"If the grid could be really large,
the recursion might hit Python's limit of about 1000.
In that case, I'd switch to BFS with a queue,
with the same fixed order of directions."

## Code

"First, I store the number of rows in N, and columns in M."

"Then I make an empty set called visited,
and an empty set called shapes."

"Then I write the 4 directions: up, down, left, and right.
I keep this order fixed, because the shape depends on it."

"Now I define a helper called dfs.
It takes r and c, the start row and start column, and the shape list."

"First thing inside, I add (r, c) to visited,
and I append (r minus start_r, c minus start_c) to shape.
That's the position relative to the start cell."

"Then for each direction, I compute nr and nc.
I check that nr is inside the rows, nc is inside the columns,
the cell is a 1, and it isn't visited.
I check the bounds first, so I never index outside the grid.
If all of that is true, I call dfs on the neighbor,
and I pass the same start_r, start_c, and shape."

"After defining dfs, I loop over every cell, row by row."

"If the cell is a 1 and isn't visited,
it's a new island.
I make a fresh empty list called shape.
I make a fresh one for every island, so shapes don't get mixed up."

"I call dfs on it, with r and c as the start cell."

"Then I turn shape into a tuple, and add it to shapes.
I use a tuple, because a list can't go in a set."

"Finally, I return the length of shapes."

## Quick check

```
grid = [[1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1]]
```

- "The first island starts at (0,0).
  DFS goes (0,0), (1,0), (1,1), (0,1).
  The shape is (0,0), (1,0), (1,1), (0,1)."
- "The second island starts at (2,2).
  DFS goes (2,2), (3,2), (3,3), (2,3).
  Relative to the start, that's (0,0), (1,0), (1,1), (0,1)."
- "It's the same tuple, so the set still has 1 shape.
  The answer is 1. Correct."

```
grid = [[1, 1, 0, 1],
        [0, 0, 0, 1]]
```

- "The first island is a horizontal domino.
  The shape is (0,0), (0,1)."
- "The second island is a vertical domino.
  The shape is (0,0), (1,0)."
- "They're different tuples, so the answer is 2. Correct."

"No islands: the set stays empty, so I return 0."

"One single 1: the shape is just (0,0), so the answer is 1."
"""
class Solution:
    def diffIslands(self, grid):
        N = len(grid)                                            # O(1)
        M = len(grid[0])                                           # O(1)
        visited = set()                                             # SPACE O(N*M): tracks visited cells
        shapes = set()                                               # SPACE: stores unique island shapes

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]                # O(1): constant 4 directions

        def dfs(r, c, start_r, start_c, shape):
            visited.add((r, c))                                         # O(1)
            shape.append((r - start_r, c - start_c))                      # O(1): record relative position
            for dr, dc in directions:                                     # O(1): constant 4 checks
                nr = r + dr
                nc = c + dc
                if (0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 1 and (nr, nc) not in visited):
                    dfs(nr, nc, start_r, start_c, shape)

        for r in range(N):                                             # TIME O(N*M): visit each cell once overall
            for c in range(M):
                if grid[r][c] == 1 and (r, c) not in visited:
                    shape = []                                            # fresh list per NEW island
                    dfs(r, c, r, c, shape)
                    shapes.add(tuple(shape))                               # freeze into hashable tuple

        return len(shapes)

# TOTAL TIME:  O(N*M) [grid scan] + O(N*M) [DFS over all cells combined] = O(N*M)
# TOTAL SPACE: O(N*M) [visited] + O(N*M) [shapes, worst case all cells across islands] = O(N*M)
                

