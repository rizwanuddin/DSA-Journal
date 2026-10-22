"""
Surrounded Regions - Medium

You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:
Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell. Regions can have any shape; they do not need to be squares or rectangles.
Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely 
enclosed by 'X' cells.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

Example 1:
Input: board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
]
Output: [
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","O","X","X"]
]
Explanation: The bottom 'O' region is not captured because it touches the edge of the board, so it cannot be surrounded.

Example 2:
Input: board = [["X"]]
Output: [["X"]]
Constraints:
1 <= board.length, board[i].length <= 200
board[i][j] is 'X' or 'O'.




# Surrounded Regions: My Thought Process

## 1. Clarify the prompt

"Before I jump in, I want to make sure I understand the problem correctly."

"So I'm given a board of 'X's and 'O's.
A group of 'O's is surrounded if it's completely closed in by 'X's
on all four sides.
I need to flip every surrounded 'O' into an 'X'.
Any 'O' that is connected to the edge of the board can't be surrounded,
so it stays an 'O'."

"I have a few quick questions before I start."

"Are 'O's connected only up, down, left, and right, or diagonally too?"
→ I'll assume only 4 directions.

"Should I change the board in place, or return a new one?"
→ I'll assume in place, and I'll return the board at the end.

"Are the values the strings 'X' and 'O'?"
→ I'll assume yes.

"Can the board be empty?"
→ I'll assume it has at least one row and one column.

"Okay, so the real question is:
which 'O's can reach the edge, and which ones can't?"

## 2. Test cases

"Let me write down a few test cases before I think about the approach."

```
X X X X
X O O X
X X O X
X O X X
```

"The three 'O's in the middle are closed in by 'X's, so they flip.
The 'O' at the bottom, at (3,1), is on the edge, so it stays."

```
X X X X
X X X X
X X X X
X O X X
```

"A few edge cases:"
- "If every 'O' is on the edge, nothing changes."
- "If an inner 'O' is connected to an edge 'O', it's safe, so it stays."
- "If there are no 'O's at all, nothing changes."
- "With a single row or a single column, every cell is on the edge,
  so nothing changes."

"Do these expected outputs match what you have in mind?"

## 3. Brute force

"My first idea is the simplest one.
For each 'O', I run a search to see if it can reach the edge."

"I walk through connected 'O's.
If I ever touch the border, that 'O' is safe.
If the search ends without touching the border, I flip it to 'X'."

"This works because I'm checking every 'O' one at a time."

"The time is O((N * M)^2).
There can be N * M 'O's,
and each search can walk through the whole board, which is another N * M."

"The space is O(N * M), for the visited set of one search."

"The problem is that I repeat a lot of work.
Every 'O' in the same group runs the same search and gets the same answer.
I'm doing one search per cell when one search per group would be enough."

## 4. Optimal solution

"The bottleneck is asking every single 'O' if it can reach the edge.
So I want to flip the question around."

"Instead of starting from every 'O' and asking
'can this reach the edge?',
I can start from the edge and mark every 'O' that is connected to it."

"Any 'O' on the border is safe.
Any 'O' connected to a safe 'O' is also safe.
So I search inward from every border 'O', and mark everything I reach.
After that, any 'O' I didn't mark must be surrounded, so I flip it."

"The data structure I'll use is a visited set of (row, col) pairs,
because it remembers which 'O's are safe,
and it stops me from visiting the same cell twice."

"As I go along the border, when I find an 'O' that isn't marked yet,
I run a DFS from it to mark its whole group as safe."

"When the DFS sees a neighbor that's inside the board,
is an 'O', and isn't marked yet, it moves into it."

"After that, I go through the whole board again.
When I find an 'O' that isn't in the safe set, I flip it to 'X'."

"At the end, I return the board."

"The time is O(N * M).
Each cell is visited by DFS at most once,
and I scan the board twice, which is still O(N * M)."

"The space is O(N * M), for the visited set and the call stack."

"So I go from O((N * M)^2) down to O(N * M)."

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

"First, I'll make a class called Solution."

"Then a function called regions that takes self and board."

"I'll store the number of rows in N and the number of columns in M.
I need these for the bounds checks, and to know where the border is."

"Next, I'll create an empty set called visited.
It holds every 'O' I've marked as safe."

"Then I'll write a directions list with the 4 moves:
up, down, left, and right.
That way I can loop over neighbors instead of writing four separate checks."

"Now I'll define a helper called dfs that takes r and c.
It marks every 'O' connected to this one as safe."

"First thing inside it, I add (r, c) to visited.
I mark it right away, so no other path visits it again."

"Then I loop over each direction."

"I compute the neighbor's row as r plus dr, and call it nr.
And the neighbor's column as c plus dc, and call it nc."

"Now I check four things before I move there.
First, nr is inside the board.
Second, nc is inside the board.
I check the bounds first, so I never index outside the board.
Third, the neighbor is an 'O'.
Fourth, it's not already in visited."

"If all four are true, I call dfs on the neighbor."

"Now I start from the border."

"I loop over every row and every column.
For each cell, I figure out if it's on the border.
It's on the border if it's in the first row, the last row,
the first column, or the last column."

"If the cell is on the border, is an 'O', and isn't visited yet,
I call dfs on it.
That marks its whole group as safe."

"At this point, every safe 'O' is in visited."

"Now I loop over the whole board one more time.
If a cell is an 'O' and it's not in visited,
it can't reach the edge, so it's surrounded.
I set it to 'X'."

"Finally, I return the board."

## 7. Testing

"Before I finish, I'll trace through my test cases."

- "First example: the only border 'O' is at (3,1).
  DFS marks it, but its neighbors are all 'X', so nothing else is marked.
  In the second pass, (1,1), (1,2), and (2,2) are 'O's that aren't marked,
  so they flip to 'X'.
  The output matches what I expected."
- "Every 'O' on the edge: they all get marked, so nothing flips."
- "Inner 'O' touching an edge 'O': DFS reaches it from the edge,
  so it's marked and stays an 'O'."
- "No 'O's: no DFS runs and nothing flips."
- "Single row or column: every cell is on the border,
  so every 'O' is marked and nothing flips."

"The output matches what I expected for all of them."

"To recap, time is O(N * M) and space is O(N * M)."

"If the board could be really large, the recursion might hit
Python's limit of about 1000.
In that case, I'd switch to BFS,
and start the queue with all the border 'O's."
"""

class Solution:
    def regions(self, board):
        N = len(board)
        M = len(board[0])
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c):
            visited.add((r, c))
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < N and 0 <= nc < M
                        and board[nr][nc] == "O"
                        and (nr, nc) not in visited):
                    dfs(nr, nc)

        for r in range(N):
            for c in range(M):
                on_border = r == 0 or r == N - 1 or c == 0 or c == M - 1
                if on_border and board[r][c] == "O" and (r, c) not in visited:
                    dfs(r, c)

        for r in range(N):
            for c in range(M):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X"
        return board