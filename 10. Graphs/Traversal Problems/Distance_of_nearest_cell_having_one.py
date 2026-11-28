"""
Distance of nearest cell having one

Given a binary grid of N x M. Find the distance of the nearest 1 in the grid for each cell.
The distance is calculated as |i1 - i2| + |j1 - j2|, where i1, j1 are the row number and column number of the current cell, and i2, j2 are the row number and 
column number of the nearest cell having value 1.

Example 1:
Input: grid = [ [0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 1] ]
Output: [ [1, 0, 0, 1], [0, 0, 1, 1], [1, 1, 0, 0] ]
Explanation: 0's at (0,0), (0,3), (1,2), (1,3), (2,0) and (2,1) are at a distance of 1 from 1's at (0,1),(0,2), (0,2), (2,3), (1,0) and (1,1) respectively.

Example 2:
Input: grid = [ [1, 0, 1], [1, 1, 0], [1, 0, 0] ]
Output: [ [0, 1, 0], [0, 0, 1], [0, 1, 2] ]
Explanation: 0's at (0,1), (1,2), (2,1) and (2,2) are at a distance of 1, 1, 1 and 2 from 1's at (0,0),(0,2), (2,0) and (1,1) respectively.





# Distance of Nearest Cell Having 1: My Thought Process

## What is the problem exactly stating?

"So what is the problem exactly stating?
It is stating that I'll be given a grid of 0s and 1s.
For every cell, I need to find the distance to the nearest 1.
Distance means how many steps up, down, left, or right it takes to get there.
If a cell is already a 1, its distance is 0."

"Quick things I'd confirm:
can I only move up, down, left, and right? I'll assume yes, no diagonals.
Is there always at least one 1 in the grid? I'll assume yes.
Should I return a new grid, not change the input? I'll assume a new grid."

"So for every 0, the question is: how far is the closest 1?"

## Brute force

"So if this problem comes up in an interview,
what is the extreme naive solution I can think of?"

"For every cell, I'll go through the whole grid,
and look at every cell that has a 1.
For each of those 1s, I compute the distance,
which is nothing but the row difference plus the column difference.
I keep the smallest one, and that's the answer for this cell."

"I do this for every cell. Quite simple."

### Time complexity

"Now what will be the time complexity?"

"To ease out computations, I'll say the grid has N rows and M columns,
so there are N into M cells in total."

"I have an outer loop that goes through every cell, that's N into M.
For every cell, I scan the whole grid again to find the 1s,
that's another N into M.
Computing one distance is big O of 1."

"So the overall time complexity is N into M, into N into M,
which is nothing but big O of (N into M) square."

### Space complexity

"Am I using any extra space?
Only the answer grid, which is N into M.
So the space is big O of N into M."

"Obviously the interviewer will not be happy with this,
because every cell is searching the whole grid all over again,
and he'll ask me to optimize."

## Optimal

"Here's the key thing I notice.
Instead of every 0 searching for its nearest 1,
what if I flip it around?
What if every 1 spreads outward, one step at a time?"

"Think of it like a wave.
All the 1s start at distance 0, at the same time.
After one step, the wave reaches every cell that's 1 step away from some 1.
After two steps, every cell that's 2 steps away, and so on."

"Can I say the first time the wave reaches a cell,
that's its nearest 1? I can.
Because the wave moves out evenly from all the 1s together,
whichever 1 is closest gets there first."

"So I'll use BFS, with a queue.
In case you don't know about it, nothing to worry about.
Just remember, a queue is first in, first out,
so BFS visits cells level by level, in order of distance."

"And I'll put all the 1s into the queue at the start.
This is called multi-source BFS.
That's what makes all the 1s spread at the same time,
instead of one after another."

"What is the next step?
I make a dist grid, filled with -1.
-1 means I haven't reached this cell yet."

"I go through the grid, and for every 1,
I set its dist to 0, and add it to the queue."

"Now I run the BFS.
I take a cell out of the queue, and look at its 4 neighbors.
If a neighbor is inside the grid, and its dist is still -1,
then this is the first time the wave reaches it.
So its distance is the current cell's distance plus 1.
I set that, and add it to the queue."

"The -1 also works as my visited check.
Once a cell has a distance, it's never updated again,
so no cell goes into the queue twice."

"When the queue is empty, every cell has its distance,
and I return the dist grid. Done and dusted."

### Time complexity

"Now let's discuss the time complexity."

"First portion, making the dist grid.
That's N into M slots, so big O of N into M."

"Next portion, the first scan to find all the 1s.
Two loops over every cell, so that's N into M."

"Next portion, the BFS.
For how many times is the while loop running?
Every cell goes into the queue exactly once, agreed?
Because once its dist is set, it's never added again.
So the while loop runs N into M times."

"Inside, I check 4 neighbors.
That's a constant, so big O of 1 for each cell."

"So the BFS is N into M, into 4, which is nothing but big O of N into M."

"So the overall time complexity is
N into M, plus N into M, plus N into M,
which is near about big O of N into M."

"If I compare with the brute force,
that was (N into M) square, and now it's just N into M.
I visit each cell only once."

### Space complexity

"What about the space complexity?
The dist grid is big O of N into M."

"The queue can hold a lot of cells in the worst case.
For example, if half the grid is 1s, they all start in the queue.
So that's big O of N into M too."

"So the overall space is big O of N into M, plus big O of N into M,
which is nothing but big O of N into M."

## Code

"First, I store the number of rows in N, and columns in M."

"Then I make dist, a grid of N rows and M columns, all set to -1.
I build each row separately, with a loop,
so each row is its own list."

"Then I make an empty deque called queue.
I use a deque because popleft is big O of 1.
A normal list's pop(0) would be big O of n."

"Then I loop over every cell.
If grid[r][c] is 1, I set dist[r][c] to 0,
and append (r, c) to the queue."

"Next, I write the 4 directions: up, down, left, and right."

"Now I loop while the queue isn't empty."

"Inside, I popleft r and c."

"Then for each direction, I compute nr as r plus dr, and nc as c plus dc."

"I check that nr is inside the rows, nc is inside the columns,
and dist[nr][nc] is still -1.
I check the bounds first, so I never index outside the grid."

"If all of that is true,
I set dist[nr][nc] to dist[r][c] plus 1,
and append (nr, nc) to the queue."

"When the queue is empty, I return dist."

## Quick check

```
grid = [[0, 1, 1, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1]]
```

- "All the 1s start in the queue, with distance 0."
- "From them, every 0 next to a 1 gets distance 1.
  (0,0) is next to (0,1), (0,3) is next to (0,2),
  (1,2) and (1,3) are next to 1s, and so are (2,0) and (2,1)."
- "Every 0 is right next to a 1, so nothing needs distance 2."
- "The answer is:

  ```
  [[1, 0, 0, 1],
   [0, 0, 1, 1],
   [1, 1, 0, 0]]
  ```

  Perfect."

```
grid = [[1, 0, 1],
        [1, 1, 0],
        [1, 0, 0]]
```

- "The 1s start at 0.
  (0,1), (1,2), and (2,1) are next to a 1, so they get 1."
- "(2,2) isn't next to any 1.
  It's reached from (1,2) or (2,1), so it gets 1 + 1 = 2."
- "The answer is:

  ```
  [[0, 1, 0],
   [0, 0, 1],
   [0, 1, 2]]
  ```

  Correct."
"""

from collections import deque

class Solution:

    def distToOne(self, grid):
        N = len(grid)                                          # O(1)
        M = len(grid[0])                                        # O(1)
        dist = [[-1] * M for _ in range(N)]                       # SPACE O(N*M): one slot per cell
        queue = deque()

        for r in range(N):                                       # TIME O(N*M): find all initial 1s
            for c in range(M):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    queue.append((r, c))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]            # O(1): constant 4 directions

        while queue:                                              # TIME O(N*M): each cell enqueued once total
            r, c = queue.popleft()
            for dr, dc in directions:                              # O(1): constant 4 checks
                nr = r + dr
                nc = c + dc
                if (0 <= nr < N and 0 <= nc < M and dist[nr][nc] == -1):
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

        return dist

# TOTAL TIME:  O(N*M) [initial scan] + O(N*M) [BFS, each cell processed once] = O(N*M)
# TOTAL SPACE: O(N*M) [dist grid] + O(N*M) [queue worst case] = O(N*M)



