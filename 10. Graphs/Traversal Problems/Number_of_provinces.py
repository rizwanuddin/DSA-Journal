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

## 1. Understanding

I want to make sure I understand the problem correctly.
I'm given an n by n matrix called adj.
adj[i][j] = 1 means city i and city j are directly connected.
A province is a group of cities connected directly or indirectly.
I need to return the number of provinces.

Quick questions:
- Is the matrix symmetric? I'll assume yes, so connections go both ways.
- Is adj[i][i] always 1? I'll assume yes, a city is connected to itself.
- Can the matrix be empty? I'll assume it can, and return 0.
- Are the only values 0 and 1? I'll assume yes.

## 2. Restate

So the matrix is a graph, written as an adjacency matrix.
I need to count how many separate groups of cities it has.
This is counting connected components.

## 3. Example

```
adj = [[1,1,0],
       [1,1,0],
       [0,0,1]]
```

City 0 and city 1 are connected.
City 2 is alone.
There are two provinces: {0, 1} and {2}.
The answer is 2.

Edge case: the identity matrix, where nobody is connected.
Every city is its own province, so the answer is n.

## 4. Brute force

My first idea is to check every pair of cities.
For each pair, I check if one can reach the other, by searching the graph.
Then I group the cities that can reach each other, and count the groups.

This works because it follows the definition of a province.

The problem is the repeated work.
There are n * n pairs, and each search can cost O(n^2) on a matrix.
That is far too slow, and most searches repeat the same exploration.

## 5. Key observation

The repeated work is searching from the same cities again and again.
Once I start a search from one city,
it finds every city in that city's province.

So after one search, I never need to start another one in that same group.

That gives me a simple plan.
I go through every city.
If a city is not visited yet, it belongs to a province I haven't seen.
I count 1, and run a search from it, to mark the whole province as visited.
If it's already visited, I skip it.

The number of times I start a search is the number of provinces.

One difference from an edge list is that the graph is a matrix.
To find the neighbors of city i, I scan row i, and look for the 1s.

I also need a visited set.
It stops me from going back through the same city, and from looping forever.

## 6. Approach

Instead of checking every pair of cities,
I can start one search per province, and mark everything it reaches.

The data structure I will use is the matrix itself, to read the connections.
For the search, I will use DFS with the recursion call stack,
plus a visited set,
because DFS can reach every city in a group, and the set stops me from repeating cities.

As I go through the cities from 0 to n - 1, I will check if each one is visited.

When a city is not visited, I will add 1 to the count,
and run DFS from it, to mark its whole province.

Inside DFS, I will mark the city as visited first.
Then I will look at its row, and go to every connected city that isn't visited yet.

When a city is already visited, I will skip it.

At the end, I return the count.

## 7. While coding

First I make a class called Solution.

Then I make a function called noOfProvince that takes self and adj.

Before anything else, I store the number of cities in V.
It's the length of adj, since the matrix is V by V.

Then I create an empty set called visited.
This holds every city I've already reached.

Then I set count to 0.
This counts the provinces.

Then I define an inner function called dfs that takes a node.
It marks every city in this city's province as visited.

The first thing inside it, I add the node to visited.
I mark it right away, so it can't be visited again by another path.
This line matters.
Without it, the search would never stop,
because a city is connected to itself, and it would call itself forever.

Then I loop j from 0 to V - 1.
This scans the row of this city, to find its neighbors.

For each j, I check two things.
First, adj[node][j] is equal to 1, so j is connected to this city.
Second, j is not in visited, so I haven't been there yet.
If both are true, I call dfs on j, which goes deeper.
Otherwise, I skip it.

After defining dfs, I loop i from 0 to V - 1.
I loop over every city, not just the connected ones,
because the graph may have several separate provinces.

For each i, I check if it's not in visited.
If so, this city is in a province I haven't seen.
I add 1 to count, and call dfs on i.
After that call, every city in that province is in visited.
So the loop skips all of them from now on.

When the loop ends, every city has been covered, and I return count.

## 8. Testing

Before I finish, I want to test the edge cases.
- Empty matrix: V is 0, the loop doesn't run, and the answer is 0.
- One city: the matrix is [[1]], and the answer is 1.
- Identity matrix: nobody is connected, so every city starts its own search,
  and the answer is n.
- All ones: the first search reaches everything, so the answer is 1.
- Indirect connection, like 0-1 and 1-2 but not 0-2:
  DFS goes from 0 to 1 to 2, so they count as one province.
- adj[i][i] = 1: the self connection is skipped,
  because the city is already in visited.
- Long chain: DFS goes n levels deep.

For my example:
- i = 0 is not visited. count becomes 1. DFS marks 0, then finds 1 and marks it.
- i = 1 is visited. Skip.
- i = 2 is not visited. count becomes 2. DFS marks 2.

The answer is 2.

If the graph could be very deep, Python's recursion limit is about 1000.
In that case I would use BFS with a queue, or an iterative DFS with a stack.
Another option is Union-Find.
It starts with n provinces, and subtracts 1 each time an edge joins two different groups.

## 9. Complexity

Time: O(V^2)
- Each city is searched at most once, because of the visited set.
- Each search scans a full row of V entries.
- V cities times V entries is V^2.
- Reading the matrix costs O(V^2) anyway, so I can't do better with this input.

Space: O(V)
- The visited set holds up to V cities.
- The call stack can go up to V deep.
- I don't build any extra structure, because I use the matrix directly.
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
        
