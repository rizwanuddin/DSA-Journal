"""
Word Search - Medium

Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.
For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring 
cells. The same cell may not be used more than once in a word.

Example 1:
Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "CAT"
Output: true

Example 2:
Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "BAT"
Output: false





# Word Search: My Thought Process

## 1. Clarify the prompt

"Before I jump in, I want to make sure I understand the problem correctly."

"So I'm given a grid of letters and a word.
I need to return True if I can spell the word
by moving from one cell to a neighboring cell, letter by letter.
Otherwise, I return False."

"I have a few quick questions before I start."

"Are neighbors only up, down, left, and right, not diagonal?"
→ I'll assume only 4 directions.

"Can I use the same cell more than once in the word?"
→ I'll assume no. Each cell can only be used once per path.

"Is it case-sensitive?"
→ I'll assume yes.

"Can the word be empty?"
→ I'll assume it has at least one letter.

"Can the board be empty?"
→ I'll assume it has at least one row and one column.

"Okay, so I'm looking for a path through the grid that spells the word,
without stepping on the same cell twice."

## 2. Test cases

"Let me write down a few test cases before I think about the approach."

```
A B C E
S F C S
A D E E
```

"word = "ABCCED":
A → B → C, then down to C, then down to E, then left to D.
Answer: True."

"word = "SEE":
S on the right edge → E below it → E to its left.
Answer: True."

"word = "ABCB":
A → B → C, but the only B next to C is the one I already used.
Answer: False."

"A few edge cases:"
- "A one-letter word that's on the board: Answer: True."
- "A one-letter word that isn't on the board: Answer: False."
- "A word longer than the number of cells: it can't fit. Answer: False."
- "A 1 by 1 board: only a one-letter word can match."

"Do these expected outputs match what you have in mind?"

## 3. Brute force

"My first idea is the simplest one.
From every cell, I try every possible path of the same length as the word,
moving in all 4 directions at each step.
Once I've built a full path, I check if it spells the word."

"This works because if the word is anywhere on the board,
one of those paths will spell it."

"The time is O(N * M * 4^L),
where N and M are the grid size, and L is the length of the word.
From each cell, every step branches 4 ways, and there are L steps."

"The space is O(L), for the path I'm building."

"The problem is that I keep building paths that went wrong early.
If the second letter doesn't match, every path that continues from there
is already useless, but I still finish building all of them."

## 4. Optimal solution

"The bottleneck is building full paths before checking if they match."

"Instead of building whole paths and checking at the end,
I can check each letter as I go,
and stop a path the moment a letter doesn't match.
That's backtracking."

"The data structures I'll use are DFS with the recursion stack,
and a visited set.
DFS lets me try one direction, and come back if it doesn't work.
The visited set stops me from using the same cell twice in one path."

"As I go through the grid, I start a DFS from every cell
that matches the first letter."

"When I'm at a cell, I mark it as visited,
and look at its 4 neighbors.
I only move into a neighbor if it's inside the grid,
matches the next letter, and isn't already used in this path."

"When I've matched the last letter, I return True."

"When none of the neighbors work, I un-mark the cell,
so another path can use it later, and return False."

"At the end, if no starting cell works, I return False."

"The time is O(N * M * 3^L) in the worst case.
I start from every cell, and after the first step,
each cell only has 3 new directions to try,
because I can't go back to the cell I came from.
In practice, it's much faster,
because most paths stop after one or two letters."

"The space is O(L), for the recursion stack and the visited set,
since a path is never longer than the word."

"So I go from O(N * M * 4^L) to O(N * M * 3^L),
and I cut off bad paths early instead of finishing them."

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

"First, I'll make a class called Solution,
and a function called wordSearch that takes self, board, and word."

"I'll store the number of rows in N and the number of columns in M.
I need these for the bounds checks."

"Then I'll create an empty set called visited.
It holds the cells used in the path I'm currently building."

"Next, I'll write a directions list with the 4 moves:
up, down, left, and right."

"Now I'll define a helper called dfs that takes r, c, and i.
When I call it, I already know board[r][c] matches word[i].
It returns True if I can finish the rest of the word from here."

"First thing inside it, I check if i is the last index of the word.
If it is, I've matched every letter, so I return True."

"Otherwise, I add (r, c) to visited.
This cell is now part of my path, so I can't use it again."

"Then I loop over each direction."

"I compute the neighbor's row as r plus dr, and call it nr.
And the neighbor's column as c plus dc, and call it nc."

"Now I check four things before I move there.
First, nr is inside the grid.
Second, nc is inside the grid.
I check the bounds first, so I never index outside the grid.
Third, the neighbor's letter matches word[i + 1], the next letter I need.
Fourth, the neighbor is not already in visited."

"If all four are true, I call dfs on the neighbor, with i + 1.
If that returns True, the rest of the word was found,
so I return True right away."

"If the loop finishes, none of the neighbors worked.
So I remove (r, c) from visited.
That's the backtracking step.
It frees up this cell, so a different path can use it later."

"Then I return False."

"Now back in the main function, I loop over every row and every column."

"For each cell, I check if it matches the first letter of the word,
and if dfs from that cell with i = 0 returns True.
If both are true, I return True.
I check the first letter first, so I don't start a DFS from cells that can't work."

"If the loops finish without finding it, I return False."

## 7. Testing

"Before I finish, I'll trace through my test cases."

- "ABCCED: the only A that works is at (0,0).
  dfs goes to B at (0,1), then C at (0,2),
  then down to C at (1,2), then down to E at (2,2),
  then left to D at (2,1).
  D is the last letter, so I return True. That matches."
- "SEE: S at (1,3) goes down to E at (2,3),
  then left to E at (2,2). That's the last letter, so I return True."
- "ABCB: I reach C at (0,2).
  The B at (0,1) is next to it, but it's already in visited.
  No other neighbor is a B, so that path fails.
  Every other path fails too, so I return False. That matches."
- "One-letter word on the board: dfs is called with i = 0,
  which is already the last index, so it returns True right away."
- "One-letter word not on the board: no cell matches word[0],
  so I never call dfs, and I return False."
- "Word longer than the grid: every path runs out of unvisited cells,
  so I return False."
- "1 by 1 board: only a one-letter word can match."

"The output matches what I expected for all of them."

"To recap, time is O(N * M * 3^L) and space is O(L)."

"A couple of ways to make it faster in practice:
I can count the letters first, and return False right away
if the board doesn't have enough of some letter.
And if the last letter of the word is rarer than the first one,
I can search for the word backwards, so fewer DFS calls get started."
"""
class Solution:
    def wordSearch(self, board, word):
        N = len(board)
        M = len(board[0])
        visited = set()

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c, i):
            if i == len(word) - 1:
                return True

            visited.add((r, c))
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < N and 0 <= nc < M
                        and board[nr][nc] == word[i + 1]
                        and (nr, nc) not in visited):
                    if dfs(nr, nc, i + 1):
                        return True
            visited.remove((r, c))
            return False

        for r in range(N):
            for c in range(M):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        return False
 
        
