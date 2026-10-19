"""
Number of provinces - Medium

Given an undirected graph with V vertices. Two vertices u and v belong to a single province 
if there is a path from u to v or v to u. Find the number of provinces. The graph is given 
as an n x n matrix adj where adj[i][j] = 1 if the ith city and the jth city are directly 
connected, and adj[i][j] = 0 otherwise.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

Example 1:
Input: adj=[ [1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1] ]
Output: 2
Explanation:In this graph, there are two provinces: [1, 4] and [2, 3]. City 1 and city 4 have a 
path between them, and city 2 and city 3 also have a path between them. There is no path between 
any city in province 1 and any city in province 2.

Example 2:
Input: adj= [ [1, 0, 1], [0, 1, 0], [1, 0, 1] ]
Output: 2
Explanation: The graph clearly has 2 Provinces [1,3] and [2]. As city 1 and city 3 has a path between 
them they belong to a single province. City 2 has no path to city 1 or city 3 hence it belongs to another province.




# Number of Provinces: My Thought Process

## 1. Clarify the prompt

I want to make sure I understand the problem correctly.
I'm given an n by n matrix called adj.
adj[i][j] = 1 means city i and city j are directly connected.
A province is a group of cities connected directly or indirectly.
I need to return the number of provinces.

Quick questions:
- Is the matrix symmetric? I'll assume yes, connections go both ways.
- Is adj[i][i] always 1? I'll assume yes.
- Can the matrix be empty? I'll assume yes, and return 0.
- Are the only values 0 and 1? I'll assume yes.

So I'm counting connected components in a graph given as a matrix.

## 2. Test cases

```
[[1,1,0],
 [1,1,0],
 [0,0,1]]
```
Cities 0 and 1 are together, 2 is alone. Answer: 2.

- Identity matrix (nobody connected): answer is n.
- All ones (everyone connected): answer is 1.
- Indirect link, 0-1 and 1-2 but not 0-2: answer is 1.
- Single city, [[1]]: answer is 1.
- Empty matrix: answer is 0.

## 3. Brute force

My first idea is to check every pair of cities.
For each pair, I search the graph to see if one can reach the other.
Then I group the cities that can reach each other, and count the groups.

Time: O(n^4).
- There are n^2 pairs.
- Each search can cost O(n^2) on a matrix.

Space: O(n) for the visited set of one search.

Why it's slow:
- Every search explores the same cities again and again.
- Once I search from one city, I already know its whole group.

## 4. Optimal solution

Instead of checking every pair,
I can start one search per province, and mark everything it reaches.

The data structure I will use is a visited set, plus DFS with the recursion stack,
because DFS reaches every city in a group, and the set stops me from repeating cities.

As I go through the cities from 0 to n - 1, I check if each one is visited.

When a city is not visited, it's a new province.
I add 1 to the count, and run DFS from it to mark the whole province.

When a city is already visited, I skip it.

At the end, I return the count.

Time: O(n^2)
- Each city is searched once, because of the visited set.
- Each search scans one full row of n entries.
- I can't do better, because just reading the matrix is O(n^2).

Space: O(n)
- The visited set holds up to n cities.
- The call stack goes up to n deep.

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

First I make a class called Solution.

Then I make a function called noOfProvince that takes self and adj.

Before anything else, I store the number of cities in V.
It's the length of adj, since the matrix is V by V.

Then I create an empty set called visited.
This holds every city I've already reached.

Then I set count to 0.
This counts the provinces.

Now I define an inner function called dfs that takes a node.
It marks every city in this city's province as visited.

First thing inside it, I add the node to visited.
I mark it right away, so it can't be visited again by another path.
This line matters.
A city is connected to itself, so without it, the search would call itself forever.

Then I loop j from 0 to V - 1.
This scans the row of this city, to find its neighbors.

For each j, I check two things.
First, adj[node][j] equals 1, so j is connected to this city.
Second, j is not in visited, so I haven't been there yet.
If both are true, I call dfs on j, which goes deeper.

After defining dfs, I loop i from 0 to V - 1.
I loop over every city, because there may be several separate provinces.

For each i, I check if it's not in visited.
If so, this city is in a province I haven't seen.
I add 1 to count, and call dfs on i.
After that call, every city in that province is in visited.
So the loop skips all of them from now on.

When the loop ends, every city is covered, and I return count.

## 7. Testing

Before I finish, I'll run my test cases.
- First example: i = 0 is new, count is 1, DFS marks 0 and 1.
  i = 1 is visited, skip.
  i = 2 is new, count is 2, DFS marks 2.
  The answer is 2, which matches.
- Identity matrix: every city is new, so the answer is n.
- All ones: the first search reaches everything, so the answer is 1.
- Indirect link: DFS goes 0 to 1 to 2, so the answer is 1.
- Single city: the answer is 1.
- Empty matrix: V is 0, the loops don't run, the answer is 0.

If the graph could be very deep, Python's recursion limit is about 1000.
In that case I would use BFS with a queue, or Union-Find.
"""
class Solution:
    def noOfProvince(self, adj):
        V = len(adj)
        visited = set()
        count = 0

        def dfs(node):
            visited.add(node)
            for j in range(V):
                if adj[node][j] == 1 and j not in visited:
                    dfs(j)

        for i in range(V):
            if i not in visited:
                count += 1
                dfs(i)
        return count
        
