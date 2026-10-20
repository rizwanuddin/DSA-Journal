"""
Flood fill algorithm - Medium

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image. 
Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, 
"flood fill" the image.

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting 
pixel of the same colour as the starting pixel, plus any pixels connected 4-directionally to those pixels 
(also with the same colour as the starting pixel), and so on. Replace the colour of all of the aforementioned 
pixels with the newColor.

Example 1:
Input: image = [ [1, 1, 1], [1, 1, 0], [1, 0, 1] ], sr = 1, sc = 1, newColor = 2
Output: [ [2, 2, 2], [2, 2, 0], [2, 0, 1] ]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), 
all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) 
are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Example 2:
Input: image = [ [0, 1, 0], [1, 1, 0], [0, 0, 1] ], sr = 2, sc = 2, newColor = 3
Output: [ [0, 1, 0], [1, 1, 0], [0, 0, 3] ]
Explanation: Starting from the pixel at position (2, 2) (i.e., the blue pixel), we 
flood fill all adjacent pixels that have the same color as the starting pixel. In 
this case, only the pixel at position (2, 2) itself is of the same color. So, only 
that pixel gets colored with the new color, resulting in the updated image.




# Flood Fill: My Thought Process

## 1. Clarify the prompt

I want to make sure I understand the problem correctly.
I'm given an image as an N by M grid of colors, a starting cell (sr, sc),
and a new color.
I need to recolor the starting cell, and every cell connected to it
that has the same original color.
Then I return the image.

Quick questions:
- Are connections only up, down, left, and right? I'll assume yes, 4 directions.
- Can I modify the image in place? I'll assume yes.
- What if the new color equals the original color? I'll assume I return the image unchanged.
- Is (sr, sc) always inside the grid? I'll assume yes.

So I'm finding the connected region of the starting color and repainting it.

## 2. Test cases

```
image = [[1,1,1],
         [1,1,0],
         [1,0,1]]
sr = 1, sc = 1, newColor = 2
```
The region of 1s connected to the center becomes 2.
The bottom-right 1 is only connected diagonally, so it stays 1.

```
[[2,2,2],
 [2,2,0],
 [2,0,1]]
```

- New color equals the original: the image comes back unchanged.
- Single cell: only that cell changes.
- Whole grid is one color: every cell changes.
- Starting cell on an edge or corner: must not go out of bounds.

## 3. Brute force

My first idea is to repeat passes over the whole grid.
First I recolor the starting cell.
Then on each pass, I recolor any cell with the original color
that is next to a cell that already has the new color.
I keep passing over the grid until a pass changes nothing.

Time: O((N * M)^2) in the worst case.
- Each pass scans all N * M cells.
- A long, winding region may only grow by one cell per pass,
  so I may need up to N * M passes.

Space: O(1) extra.

Why it's slow:
- Every pass rescans cells that can't change.
- I only need to look at the neighbors of cells I just recolored.

## 4. Optimal solution

Instead of rescanning the whole grid on every pass,
I can start from the given cell and spread out only through matching neighbors.

The data structure I will use is DFS with the recursion stack,
because it naturally spreads from a cell to its neighbors, then theirs.

I don't need a visited set.
Once a cell is recolored, it no longer matches the original color,
so I will never go into it again.

As I go through the region, I recolor the current cell first.
Then I check its 4 neighbors.

When a neighbor is in bounds and still has the original color,
I go into it.

One special case: if the new color equals the original,
recoloring doesn't mark anything as done,
so the search would loop forever.
I return the image right away in that case.

At the end, I return the image.

Time: O(N * M)
- Each cell is recolored at most once.
- Each recolor checks 4 neighbors, which is constant.

Space: O(N * M)
- No visited set, but the call stack can go N * M deep
  if the whole region is one long winding path.

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

First I make a class called Solution.

Then I make a function called floodFill that takes self, image, sr, sc, and newColor.

Before anything else, I save the starting cell's color in original.
I need it because the starting cell is about to change,
and I still have to compare neighbors against the old color.

Then I check if original equals newColor.
If so, I return the image right away.
Nothing needs to change.
This check also prevents an infinite loop,
because recoloring a cell to the same color wouldn't stop me from revisiting it.

Then I store the number of rows in N and the number of columns in M.
I need these for the bounds checks.

Next I write a list called direction with the 4 moves:
up, left, right, and down.
Each one is a change in row and a change in column.
This lets me loop over neighbors instead of writing 4 separate checks.

Now I define an inner function called dfs that takes r and c.

First thing inside it, I set image[r][c] to newColor.
This recolors the cell, and also works as my visited marker.
After this, the cell no longer matches original.

Then I loop over each dr, dc in direction.

I compute the neighbor's row as r + dr, and store it in nr.
And the neighbor's column as c + dc, and store it in nc.

Then I check three things.
First, nr is between 0 and N - 1.
Second, nc is between 0 and M - 1.
I check the bounds first, so I never index outside the grid.
Third, image[nr][nc] equals original, so it's part of the same region
and hasn't been recolored yet.
If all three are true, I call dfs on the neighbor.

After defining dfs, I call it on sr and sc to start the fill.

And finally I return image.

## 7. Testing

Before I finish, I'll run my test cases.
- First example: original is 1, and newColor is 2, so I don't return early.
  DFS starts at (1,1), recolors it, then spreads to every connected 1.
  The bottom-right 1 has no straight path from the region, so it stays 1.
  The output matches.
- New color equals original: the early return gives back the same image.
- Single cell: it gets recolored, and no neighbors are in bounds.
- Whole grid one color: DFS reaches every cell.
- Edge or corner start: the bounds check runs before indexing, so no crash.

If the region could be very large, the recursion could hit Python's limit of about 1000.
In that case I would use BFS with a queue.
"""
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        original = image[sr][sc]
        if original == newColor:
            return image
        N = len(image)
        M = len(image[0])
        direction = [      (-1,0),          
                     (0,-1),      (0,1),
                           (1,0)        ]
        def dfs(r, c):
            image[r][c] = newColor
            for dr, dc in direction:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < N and 0 <= nc < M and original == image[nr][nc]):
                    dfs(nr, nc)
        dfs(sr, sc)  
        return image

