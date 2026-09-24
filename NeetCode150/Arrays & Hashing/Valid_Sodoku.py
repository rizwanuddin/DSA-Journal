"""
Valid Sudoku - Explanation

You are given a 9 x 9 Sudoku board board. A Sudoku board is valid 
if the following rules are followed:

    Each row must contain the digits 1-9 without duplicates.
    Each column must contain the digits 1-9 without duplicates.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the 
    digits 1-9 without duplicates.

Return true if the Sudoku board is valid, otherwise return false
Note: A board does not need to be full or be solvable to be valid.




# VALID SUDOKU — INTERVIEW EXPLANATION

## 1. CLARIFY

"Let me make sure I understand the problem. I'm given a 9x9 Sudoku
board, and I need to check if it's valid — meaning no row, column, or
3x3 sub-box contains a repeated digit. The board doesn't need to be
complete or solvable, just free of duplicates in filled cells."

## 2. BRUTE FORCE

"The brute-force way is to check rows, columns, and boxes separately
in three different passes, using a set for each to catch duplicates.
That works, but it means scanning the board three separate times."

## 3. OPTIMIZE

"I can do all three checks in a single pass instead. For every cell,
I check it against its row's set, its column's set, and its box's
set at the same time, so I only ever look at each cell once."

## 4. KEY OBSERVATION

"Each cell belongs to exactly one row, one column, and one of nine
3x3 boxes. If I maintain one set per row, one per column, and one per
box, I can check all three constraints for a cell in constant time,
using a single combined condition."

## 5. APPROACH

"I'll create three lists of sets — one for rows, one for columns, one
for boxes — each with 9 empty sets.

I'll scan the board cell by cell. For each non-empty cell, I'll
figure out which box it belongs to using row and column division.

I'll check if this digit is already present in its row's set, column's
set, or box's set. If it is, the board is invalid, so I return False
immediately.

If not, I add the digit to all three relevant sets and continue.

If I get through every cell without a conflict, the board is valid."

## 6. WHILE CODING

"First, I set up three lists of 9 empty sets each — one for rows,
columns, and boxes."

rows = []
cols = []
boxes = []
for i in range(9):
    rows.append(set())
    cols.append(set())
    boxes.append(set())

"Now I scan every cell in the grid."

for r in range(9):
    for c in range(9):
        val = board[r][c]

"Empty cells don't need checking, so I skip them."

        if val == ".":
            continue

"I calculate which of the nine boxes this cell belongs to."

        box_index = (r // 3) * 3 + (c // 3)

"I check if this digit already exists in this row, column, or box."

        if val in rows[r] or val in cols[c] or val in boxes[box_index]:
            return False

"If there's no conflict, I record this digit in all three relevant
sets."

        rows[r].add(val)
        cols[c].add(val)
        boxes[box_index].add(val)

"If every cell passes without triggering a conflict, the board is
valid."

return True

## 7. EDGE CASES

"If the board is completely empty, every cell is '.', so the loop
just skips everything and returns True, which is correct since an
empty board has no duplicates.

If the board is partially filled, only the non-empty cells are
checked, which matches the problem's note that the board doesn't need
to be full to be valid."

## 8. COMPLEXITY

"Time complexity is O(1), since the board size is fixed at 81 cells
regardless of input — though it's sometimes described as O(9^2) to
reflect that fixed grid size.

Space complexity is also O(1) for the same reason, since the three
lists always hold exactly 9 sets each, bounded by the fixed board
size."
"""
class Solution:
    def valid_sodoku(self, board):
        rows = []
        cols = []
        boxes = []
        for i in range(9):
            rows.append(set())
            cols.append(set())
            boxes.append(set())
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                box_index = (r // 3) * 3 + (c // 3)
                if val in rows[r] or val in cols[r] or val in boxes[box_index]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)
        return True


"""
# VALID SUDOKU — SHORT EXPLANATION

- Check every cell once
- For each cell, verify the digit hasn't already appeared in its
  row, column, or 3x3 box
- Use one set per row (9 total), one per column (9 total), one per
  box (9 total) to track "seen" digits
- If a digit's already in any of the three relevant sets, it's a
  duplicate, so the board is invalid
- Otherwise, add it to all three sets and move on

## Box formula

box_index = (r // 3) * 3 + (c // 3)

- r // 3 -> which row-band (0, 1, or 2)
- c // 3 -> which column-band (0, 1, or 2)
- combine into a single number 0-8 identifying which of the 9 boxes
  the cell belongs to
"""