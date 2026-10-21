"""
Walls And Gates - Medium

You are given a m×n
m×n 2D grid initialized with these three possible values:
-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 
2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest. If a land 
cell cannot reach a treasure chest then the value should remain INF.
Assume the grid can only be traversed up, down, left, or right.
Modify the grid in-place.

Example 1:
Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]

Example 2:
Input: [
  [0,-1],
  [2147483647,2147483647]
]

Output: [
  [0,-1],
  [1,2]
]





# Walls and Gates: My Thought Process

## 1. Clarify the prompt

I want to make sure I understand the problem correctly.
I'm given an N by M grid.
-1 is a wall, 0 is a gate, and 2147483647 (INF) is an empty room.
I need to fill each empty room with the distance to its nearest gate.
If a room can't reach any gate, it stays INF.

Quick questions:
- Do I move only up, down, left, and right? I'll assume yes, 4 directions.
- Do I modify the grid in place, without returning anything? I'll assume yes.
- Can I walk through other gates or rooms, but not walls? I'll assume yes.
- Can there be no gates at all? I'll assume yes, then every room stays INF.
- Can the grid be empty? I'll assume yes, and just return.

So for every empty room, I want the shortest walking distance to any gate.

## 2. Test cases

```
INF  -1   0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
```
After filling:
```
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
```

- No gates: nothing changes.
- No empty rooms: nothing changes.
- A room surrounded by walls: it stays INF.
- A room between two gates: it takes the closer one.

## 3. Brute force

My first idea is to run a separate BFS from every empty room,
and stop when I reach the first gate.
That distance is the room's answer.

Time: O((N * M)^2).
- There can be N * M empty rooms.
- Each BFS can visit all N * M cells.

Space: O(N * M) for the queue and visited set of one BFS.

A better version is one BFS per gate,
keeping the smaller distance in each room.
That's O(G * N * M), where G is the number of gates.
With many gates, it's still O((N * M)^2).

Why it's slow:
- The searches overlap.
- Rooms near each other explore the same area again and again.

## 4. Optimal solution

Instead of one search per room or per gate,
I can start one BFS from all the gates at the same time.

The data structure I will use is a queue,
because BFS expands in order of distance.
So the first time a gate's wave reaches a room,
that is the shortest distance from any gate.

I put every gate into the queue at the start.
This is multi-source BFS.
All the gates spread together, one step at a time.

As I go through the queue, I take a cell and check its 4 neighbors.

When a neighbor is in bounds and is still INF, it's an empty room
that hasn't been reached yet.
I set its distance to the current cell's distance + 1,
and add it to the queue.

The INF check also works as my visited check.
Once a room gets a distance, it's no longer INF,
so it's never updated again.
Walls are -1, so they're never entered.

I don't need to track levels separately,
because each cell's distance is stored in the grid itself.

When the queue is empty, every reachable room has its distance.

Time: O(N * M)
- Each cell is added to the queue at most once.
- Each one checks 4 neighbors, which is constant.

Space: O(N * M)
- The queue can hold up to N * M cells.
- I don't need a visited set, because I update the grid in place.

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

First I import deque from collections.
I'm using it as my queue, because removing from the front is O(1).

Then I make a class called Solution.

Then I make a function called wallAndGates that takes self and grid.

Before anything else, I check if grid is empty, and if so I return.
That keeps grid[0] from crashing on the next lines.

I store the number of rows in N and the number of columns in M.
I need these for the bounds checks.

Then I set INF to 2147483647.
That's the value for an empty room, so I give it a name to make the check readable.

Then I create an empty queue.

Next I write a list called directions with the 4 moves:
up, down, left, and right.

Now I loop r over every row, and c over every column.
If grid[r][c] is 0, it's a gate, so I add (r, c) to the queue.
All the gates go in together, so they all spread at the same time.

Now I start a while loop that runs as long as the queue isn't empty.

Inside it, I take r and c from the front, using popleft.

Then I loop over each dr, dc in directions.

I compute the neighbor's row as r + dr, and store it in nr.
And the neighbor's column as c + dc, and store it in nc.

Then I check that nr is between 0 and N - 1,
nc is between 0 and M - 1,
and grid[nr][nc] is INF.
I check the bounds first, so I never index outside the grid.
The INF check means it's an empty room I haven't reached yet.
It skips walls, gates, and rooms that already have a distance.

If all of that is true, I set grid[nr][nc] to grid[r][c] + 1.
That's one step further than the cell I came from.

Then I add (nr, nc) to the queue,
so it can spread to its own neighbors later.

When the queue is empty, every reachable room has its shortest distance.
I don't return anything, because I changed the grid in place.

## 7. Testing

Before I finish, I'll run my test cases.
- First example: both gates start in the queue.
  The rooms next to them get 1, then the next ring gets 2, and so on.
  (3,3) is reached last, with 4.
  This matches the expected grid.
- No gates: the queue starts empty, so nothing changes.
- No empty rooms: no neighbor is ever INF, so nothing changes.
- Room surrounded by walls: no path reaches it, so it stays INF.
- Room between two gates: the closer gate's wave reaches it first,
  and after that it's no longer INF, so the farther gate can't overwrite it.
"""
# I WROTE ALL THIS BY MYSELF EHHEHEHEHEHHEHEEHHEHE
from collections import deque
class Solution:
    def wallAndGates(self, grid):
        if not grid:
            return 
        N = len(grid)
        M = len(grid[0])
        queue = deque()
        dist_count = 0
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        INF = 2147483647
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 0:
                    queue.append((r,c))
        while queue:
            dist_count += 1
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (0 <= nr < N and 0 <= nc < M and grid[nr][nc]==INF):
                        grid[nr][nc] = dist_count
                        queue.append((nr,nc))
        return grid

###EWW JUST A LIL BIT BETTER CLAUDE'S CODE
from collections import deque


class Solution:
    def wallAndGates(self, grid):
        if not grid:
            return

        N = len(grid)
        M = len(grid[0])
        INF = 2147483647
        queue = deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r in range(N):
            for c in range(M):
                if grid[r][c] == 0:
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))