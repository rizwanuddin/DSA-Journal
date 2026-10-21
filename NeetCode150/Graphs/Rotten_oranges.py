"""
Rotting Oranges - Medium

You are given a 2-D matrix grid. Each cell can have one of three possible values:
0 representing an empty cell
1 representing a fresh fruit
2 representing a rotten fruit
Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten 
fruit, then the fresh fruit also becomes rotten.
Return the minimum number of minutes that must elapse until there are zero fresh 
fruits remaining. If this state is impossible within the grid, return -1.

Example 1:
Input: grid = [[1,1,0],[0,1,1],[0,1,2]]
Output: 4

Example 2:
Input: grid = [[1,0,1],[0,2,0],[1,0,1]]
Output: -1
# Rotting Oranges: My Thought Process

## 1. Clarify the prompt

I want to make sure I understand the problem correctly.
I'm given an N by M grid.
0 is an empty cell, 1 is a fresh orange, and 2 is a rotten orange.
Every minute, each rotten orange rots the fresh oranges directly next to it.
I need to return the minimum number of minutes until no fresh orange is left.
If some fresh orange can never rot, I return -1.

Quick questions:
- Does rot spread only up, down, left, and right? I'll assume yes, 4 directions.
- Can I modify the grid? I'll assume yes, I'll mark oranges as rotten in place.
- If there are no fresh oranges at the start, is the answer 0? I'll assume yes.
- Can there be several rotten oranges at the start? I'll assume yes.
- Can the grid be empty? I'll assume it has at least one row and one column.

So all the rotten oranges spread at the same time, one step per minute,
and I need the time it takes to reach the last fresh orange.

## 2. Test cases

```
2 1 1
1 1 0
0 1 1
```
Minute 1: (0,1) and (1,0) rot.
Minute 2: (0,2) and (1,1) rot.
Minute 3: (2,1) rots.
Minute 4: (2,2) rots.
Answer: 4.

- A fresh orange cut off by empty cells: answer is -1.
- No fresh oranges: answer is 0.
- Fresh oranges but no rotten ones: answer is -1.
- Two rotten oranges on opposite sides: they spread at the same time,
  so the answer is smaller than with just one.

## 3. Brute force

My first idea is to simulate it minute by minute on the whole grid.
Each minute, I scan every cell.
For every rotten orange, I mark its fresh neighbors to rot.
Then I apply all the changes, and add 1 to the time.
I stop when a minute changes nothing.
If fresh oranges are still left, I return -1.

Time: O((N * M)^2).
- Each minute scans all N * M cells.
- The rot can take up to N * M minutes to spread, along a winding path.

Space: O(N * M) to store the changes for each minute.

Why it's slow:
- Every minute rescans oranges that already rotted long ago
  and can't affect anything new.
- I only need to look at the oranges that rotted in the last minute.

## 4. Optimal solution

Instead of rescanning the whole grid every minute,
I can only process the oranges that just rotted.

The data structure I will use is a queue,
because BFS processes cells level by level,
and each level is exactly one minute of spreading.

I start by putting every rotten orange into the queue at the same time.
This is called multi-source BFS.
It's what makes all of them spread together, instead of one after another.
I also count the fresh oranges, so I know when I'm done.

As I go through the queue, I process one level at a time.
For each rotten orange in the level, I check its 4 neighbors.

When a neighbor is a fresh orange,
I mark it rotten, add it to the queue, and subtract 1 from the fresh count.
Marking it right away means no other orange adds it twice.

After each full level, I add 1 minute.

I stop when the queue is empty, or when no fresh oranges are left.

At the end, if any fresh oranges are still left, I return -1.
Otherwise, I return the minutes.

Time: O(N * M)
- Each cell is added to the queue at most once.
- Each one checks 4 neighbors, which is constant.
- The first scan of the grid is also O(N * M).

Space: O(N * M)
- The queue can hold up to N * M cells in the worst case.

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

First I import deque from collections.
I'm using it as my queue, because removing from the front is O(1).

Then I make a class called Solution.

Then I make a function called TimeToRot that takes self and grid.

I store the number of rows in N and the number of columns in M.
I need these for the bounds checks.

Then I set fresh to 0.
This counts the fresh oranges I still need to rot.

Then I create an empty queue.
It will hold the positions of rotten oranges, as (row, col) pairs.

Then I set minTime to 0.
This counts the minutes.

Now I loop r over every row, and c over every column.
This first pass sets everything up.

If grid[r][c] is 1, it's fresh, so I add 1 to fresh.

Else if grid[r][c] is 2, it's rotten, so I add (r, c) to the queue.
All the starting rotten oranges go in together,
so they all spread at the same time.

Next I write a list called directions with the 4 moves:
up, down, left, and right.

Now I start a while loop that runs while the queue isn't empty
and fresh is more than 0.
I check fresh too, so I stop as soon as the last orange rots.
Otherwise, I would count one extra minute
for the last level, which has nothing left to rot.

At the start of each round, I store the queue's length in size.
Right now, the queue holds only the oranges that rotted in the last minute.
If I checked the length during the loop, the new oranges I add
would mix into this minute.

Then I loop size times.
This processes exactly one minute of spreading.

Inside it, I take r and c from the front of the queue, using popleft.

Then I loop over each dr, dc in directions.

I compute the neighbor's row as r + dr, and store it in nr.
And the neighbor's column as c + dc, and store it in nc.

Then I check that nr is between 0 and N - 1,
nc is between 0 and M - 1,
and grid[nr][nc] is 1, so it's a fresh orange.
I check the bounds first, so I never index outside the grid.

If all of that is true, I add (nr, nc) to the queue.
I set grid[nr][nc] to 2, so it's rotten now.
That also stops any other orange from adding it again.
And I subtract 1 from fresh.

When the for loop is done, one full minute has passed.
So I add 1 to minTime.

After the while loop ends, I check if fresh is still more than 0.
If so, some oranges were never reached, so I return -1.

Otherwise, I return minTime.

## 7. Testing

Before I finish, I'll run my test cases.
- First example: fresh starts at 6, the queue starts with (0,0).
  Each round rots the next layer, and fresh goes 6, 4, 2, 1, 0.
  The loop stops after the fourth round, with minTime at 4.
  The answer is 4, which matches.
- Cut-off orange: the queue empties while fresh is still more than 0,
  so I return -1.
- No fresh oranges: fresh is 0, the while loop never runs, and I return 0.
- No rotten oranges, but fresh ones: the queue is empty from the start,
  fresh is more than 0, so I return -1.
- Two rotten sources: both start in the queue at minute 0,
  so they spread at the same time.
"""
from collections import deque
class Solution:
    def TimeToRot(self, grid):
        N = len(grid)
        M = len(grid[0])
        fresh = 0
        queue = deque()
        minTime = 0
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue and fresh > 0:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 1):
                        queue.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            minTime += 1
        if fresh > 0:
            return -1
        return minTime