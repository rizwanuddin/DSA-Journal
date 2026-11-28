"""
Surrounded Regions

You are given a matrix mat of size N x M where each cell contains either 'O' or 'X'.
Your task is to replace all 'O' cells that are completely surrounded by 'X' with 'X'.
Rules:
An 'O' (or a group of connected 'O's) is considered surrounded if it is not connected to any border of the matrix.
Two 'O' cells are considered connected if they are adjacent horizontally or vertically (not diagonally).
A region of connected 'O's that touches the border (i.e., first row, last row, first column, or last column) is not surrounded and should not be changed.

Example 1:
Input: mat = [ ["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"] ]
Output: [ ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"] ]
Explanation:
The 'O' cells at positions (1,1), (1,2), (2,2), and (3,1) are surrounded by 'X' cells in all directions (horizontally and vertically).
However, the 'O' region at (3,1) is adjacent to an edge of the board, so it cannot be completely surrounded by 'X' cells. Therefore, it remains unchanged.

Example 2:
Input: mat = [ ["X", "X", "X"], ["X", "O", "X"], ["X", "X", "X"] ]
Output: [ ["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"] ]
Explanation: The only 'O' cell at position (1,1) is completely surrounded by 'X' cells in all directions (horizontally and vertically). Hence, it is replaced with 
'X' in the output.




# Replace O's with X's (Surrounded Regions): My Thought Process

## What is the problem exactly stating?

"So what is the problem exactly stating?
It is stating that I'll be given a matrix of 'X's and 'O's.
Any group of 'O's that is completely surrounded by 'X's
needs to be replaced with 'X's.
But any 'O' that is connected to the border can't be surrounded,
so it stays an 'O'."

"Quick things I'd confirm:
are 'O's connected only up, down, left, and right? I'll assume yes, no diagonals.
Can I change the matrix in place? I'll assume yes, and I'll return it.
Can the matrix be empty? I'll assume it has at least one row and one column."

"So the real question is:
which 'O's can reach the border, and which ones can't?"

## Brute force

"So if this problem comes up in an interview,
what is the extreme naive solution I can think of?"

"For every 'O', I'll run a DFS
to see if it can reach the border through other 'O's.
If it can, it's safe, so I leave it.
If the search ends without touching the border, I flip it to 'X'."

"I do this for every single 'O'. Quite simple."

### Time complexity

"Now what will be the time complexity?"

"To ease out computations, I'll say the matrix has N rows and M columns,
so there are N into M cells."

"In the worst case, almost every cell is an 'O',
so I start a DFS from up to N into M cells."

"And each DFS can walk through the whole matrix,
which is another N into M."

"So the overall time complexity is N into M, into N into M,
which is nothing but big O of (N into M) square."

### Space complexity

"Am I using any extra space?
Each DFS needs a visited set, and the recursion stack,
and both can go up to N into M.
So the space is big O of N into M."

"Obviously the interviewer will not be happy with this,
because every 'O' in the same group runs the same search again and again,
and he'll ask me to optimize."

## Optimal

"Here's the key thing I notice.
Instead of asking every 'O' if it can reach the border,
what if I flip the question around?
I start from the border, and mark every 'O' that's connected to it."

"Any 'O' on the border is safe, right?
And any 'O' connected to a safe 'O' is also safe, agreed?
So if I start a DFS from every border 'O',
everything it reaches is safe."

"After that, can I say every 'O' I didn't reach is surrounded? I can.
Because if it could reach the border,
the DFS from that border would have found it."

"So I'll use DFS, with a visited set.
In case you don't know about it, nothing to worry about.
Just remember, DFS goes as deep as it can,
and visits every cell connected to where it started.
The visited set remembers which 'O's are safe,
and stops me from visiting a cell twice."

"What is the next step?
I go through every cell.
If it's on the border, it's an 'O', and it's not visited yet,
I run DFS from it, to mark its whole group as safe."

"Inside DFS, I mark the cell as visited,
then check its 4 neighbors.
If a neighbor is inside the matrix, is an 'O', and isn't visited,
I go into it."

"Then I go through the whole matrix again.
Any 'O' that isn't in visited is surrounded, so I flip it to 'X'."

"At the end, I return the matrix. Done and dusted."

### Time complexity

"Now let's discuss the time complexity."

"First portion, the border pass.
I loop over every cell, that's N into M.
And all the DFS calls combined,
how many cells do they visit?
Each cell is added to visited only once,
so all the DFS calls together visit at most N into M cells.
Each visit checks 4 neighbors, which is constant.
So this whole portion is near about big O of N into M."

"Next portion, the flip pass.
I loop over every cell again,
and each check is big O of 1, on average, for the set.
So that's N into M."

"So the overall time complexity is
N into M, plus N into M,
which is nothing but big O of N into M."

"If I compare with the brute force,
that was (N into M) square, and now it's just N into M.
I only search each group once, starting from the border."

### Space complexity

"What about the space complexity?
The visited set can hold every cell in the worst case,
if the whole matrix is 'O's. That's big O of N into M."

"The recursion stack can also go N into M deep in the worst case,
if all the 'O's form one long winding path.
That's another big O of N into M."

"So the overall space is big O of N into M, plus big O of N into M,
which is nothing but big O of N into M."

"If the matrix could be really large,
the recursion might hit Python's limit of about 1000.
In that case, I'd switch to BFS with a queue,
starting with all the border 'O's."

## Code

"First, I store the number of rows in N, and columns in M."

"Then I make an empty set called visited.
It holds every 'O' I've marked as safe."

"Then I write the 4 directions: up, down, left, and right."

"Now I define a helper called dfs that takes r and c."

"First thing inside, I add (r, c) to visited.
I mark it right away, so no other path visits it again."

"Then for each direction, I compute nr as r plus dr, and nc as c plus dc."

"I check that nr is inside the rows, nc is inside the columns,
the neighbor is an 'O', and it isn't in visited.
I check the bounds first, so I never index outside the matrix."

"If all of that is true, I call dfs on the neighbor."

"After defining dfs, I loop over every cell."

"I compute on_border.
It's true if r is 0, or c is 0, or r is N - 1, or c is M - 1."

"If the cell is on the border, it's an 'O', and it isn't visited,
I call dfs on it."

"Then I loop over every cell again.
If it's an 'O' and it isn't in visited, it's surrounded,
so I set it to 'X'."

"Finally, I return mat."

## Quick check

```
X X X X
X O O X
X X O X
X O X X
```

- "The only border 'O' is at (3,1).
  DFS marks it, but all its neighbors are 'X', so nothing else gets marked."
- "In the second pass, (1,1), (1,2), and (2,2) are 'O's that aren't visited,
  so they flip to 'X'."
- "The answer is:

  ```
  X X X X
  X X X X
  X X X X
  X O X X
  ```

  Perfect."

```
O O
O O
```

- "Every cell is on the border, so every 'O' gets marked.
  Nothing flips. Correct."
"""
class Solution:
    def replaceOs(self, mat):
        N = len(mat)                                             # O(1)
        M = len(mat[0])                                           # O(1)
        visited = set()                                            # SPACE O(N*M): worst case every cell is O

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]              # O(1): constant 4 directions

        def dfs(r, c):
            visited.add((r, c))                                      # O(1)
            for dr, dc in directions:                                  # O(1): constant 4 checks
                nr = r + dr
                nc = c + dc
                if (0 <= nr < N and 0 <= nc < M and mat[nr][nc] == "O" and (nr, nc) not in visited):
                    dfs(nr, nc)

        for r in range(N):                                           # TIME O(N*M): visit each border-triggered cell once
            for c in range(M):
                on_border = r == 0 or c == 0 or r == N - 1 or c == M - 1
                if on_border and mat[r][c] == "O" and (r, c) not in visited:
                    dfs(r, c)

        for r in range(N):                                           # TIME O(N*M): second full scan, no DFS, O(1) per cell
            for c in range(M):
                if mat[r][c] == "O" and (r, c) not in visited:
                    mat[r][c] = "X"

        return mat

# TOTAL TIME:  O(N*M) [border dfs pass] + O(N*M) [flip pass] = O(N*M)
# TOTAL SPACE: O(N*M) [visited] + O(N*M) [recursion stack worst case] = O(N*M)