"""
Connected Components - Medium

Given a undirected Graph consisting of V vertices numbered from 0 to V-1 and E edges. 
The ith edge is represented by [ai,bi], denoting a edge between vertex ai and bi. We say 
two vertices u and v belong to a same component if there is a path from u to v or v to u. 
Find the number of connected components in the graph.

A connected component is a subgraph of a graph in which there exists a path between any two 
vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

Example 1:
Input: V=4, edges=[[0,1],[1,2]]
Output: 2
Explanation: Vertices {0,1,2} forms the first component and vertex 3 forms the second component.

Example 2:
Input: V = 7, edges = [[0, 1], [1, 2], [2, 3], [4, 5]]
Output: 3
Explanation:
The edges [0, 1], [1, 2], [2, 3] form a connected component with vertices {0, 1, 2, 3}.
The edge [4, 5] forms another connected component with vertices {4, 5}.
Therefore, the graph has 3 connected components: {0, 1, 2, 3}, {4, 5}, and the isolated 
vertices {6} (vertices 6 and any other unconnected vertices).




# Number of Connected Components in an Undirected Graph: My Thought Process

## 1. Understanding

I want to make sure I understand the problem correctly.
I'm given V, the number of nodes, and a list of undirected edges.
I need to return how many connected components the graph has.
A connected component is a group of nodes where every node can reach every other node.

Quick questions:
- Are the nodes labeled 0 to V - 1? I'll assume yes.
- Is the graph undirected? I'll assume yes, so each edge goes both ways.
- Can some nodes have no edges? I'll assume yes.
  Each of those is its own component.
- Can there be duplicate edges or self-loops? I'll assume yes, and handle them.
- Can V be 0? I'll assume it can, and return 0.

## 2. Restate

So I'm counting how many separate groups the graph has.
Nodes in the same group can reach each other through edges.
Nodes in different groups can't.

## 3. Example

```
V = 6
edges = [[0,1], [1,2], [3,4]]

0 - 1 - 2      3 - 4      5
```

There are three groups: {0, 1, 2}, {3, 4}, and {5}.
The answer is 3.

Edge case: V = 4 with no edges.
Every node is alone, so the answer is 4.

## 4. Brute force

My first idea is to check every pair of nodes.
For each pair, I check if one can reach the other, by searching the graph.
Then I group the nodes that can reach each other, and count the groups.

This works because it follows the definition of a component.

The problem is the repeated work.
There are V * V pairs, and each search can cost O(V + E).
That is far too slow, and most of the searches repeat the same exploration.

## 5. Key observation

The repeated work is searching from the same nodes again and again.
Once I start a search from one node,
it finds every node in that node's component.

So after one search, I never need to start another one in that same group.
All those nodes are done.

That gives me a simple plan.
I go through every node.
If a node is not visited yet, it belongs to a component I haven't seen.
I count 1, and run a search from it, to mark the whole group as visited.
If a node is already visited, it belongs to a group I already counted, so I skip it.

The number of times I start a search is the number of components.

I also need a visited set.
It stops me from going back through the same node, and from looping forever on cycles.

## 6. Approach

Instead of checking every pair of nodes,
I can start one search per component, and mark everything it reaches.

The data structure I will use is an adjacency list, to get the neighbors of a node directly.
For the search, I will use DFS with the recursion call stack,
plus a visited set,
because DFS can reach every node in a group, and the set stops me from repeating nodes.

As I go through the nodes from 0 to V - 1, I will check if each one is visited.

When a node is not visited, I will add 1 to the count,
and run DFS from it, to mark its whole component.

When a node is already visited, I will skip it.

At the end, I return the count.

## 7. While coding

First I make a class called Solution.

I'll write a helper first, called adjBuild, that takes self, V, and edges.
It turns the edge list into an adjacency list.

Inside it, I create an empty list called adj.
Then I loop V times, and add an empty list for each node.
Now adj[i] is where I store the neighbors of node i.
I create all V lists, so nodes with no edges still have an entry.

Then I loop over the edges, unpacking each one into u and v.
I add v to the list of u.
And I add u to the list of v.
I do both, because the graph is undirected.

Then I return adj.

Now I write connectedComp, which takes self, V, and edges.
First, I call adjBuild to get the adjacency list.

Then I create an empty set called visited.
This holds every node I've already reached.

Then I set count to 0.
This counts the components.

Then I define an inner function called dfs that takes a node.
It marks every node in this node's component as visited.

Inside it, I add the node to visited first.
I mark it right away, so it can't be visited again by another path.

Then I loop over the neighbors of this node.
For each neighbor, I check if it's not in visited.
If it's not, I call dfs on it, which goes deeper.
If it is, I skip it, which protects me from cycles.

After defining dfs, I loop i from 0 to V - 1.
I loop over every node, not just the connected ones,
because the graph may have several separate groups.

For each i, I check if it's not in visited.
If so, this node is in a component I haven't seen.
I add 1 to count, and call dfs on i.
After that call, every node in that component is in visited.
So the loop will skip all of them from now on.

When the loop ends, every node has been covered, and I return count.

## 8. Testing

Before I finish, I want to test the edge cases.
- V = 0: the loop doesn't run, and the answer is 0.
- One node, no edges: the loop finds 0 not visited, so the answer is 1.
- No edges at all: every node starts its own search, so the answer is V.
- Fully connected graph: the first search reaches everything, so the answer is 1.
- Cycle, like 0-1, 1-2, 2-0: visited stops me from looping forever.
- Duplicate edges or self-loops: the visited check skips them.
- Long chain: DFS goes V levels deep.

For my example:
- i = 0 is not visited. count becomes 1. DFS marks 0, 1, 2.
- i = 1 and i = 2 are visited. Skip.
- i = 3 is not visited. count becomes 2. DFS marks 3, 4.
- i = 4 is visited. Skip.
- i = 5 is not visited. count becomes 3. DFS marks 5.

The answer is 3.

If the graph could be very deep, Python's recursion limit is about 1000.
In that case I would use BFS with a queue, or an iterative DFS with a stack.
Another option is Union-Find.
It counts components by merging groups, and starts with V components,
then subtracts 1 each time an edge joins two different groups.

## 9. Complexity

Time: O(V + E)
- Building the adjacency list takes O(V + E).
- The outer loop visits each node once.
- Each node is searched at most once, because of the visited set.
- Each neighbor list is scanned once, and the lists add up to 2E.

Space: O(V + E)
- The adjacency list stores V lists and 2E entries.
- The visited set holds up to V nodes.
- The call stack can go up to V deep.

Compared with the brute force, O(V * (V + E)) becomes O(V + E).
"""
class Solution:
    def adjBuild(self, V, edges):
        adj = []
        for i in range(V):
            adj.append([])

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        return adj

    def connectedComp(self, V, edges):
        adj = self.adjBuild(V, edges)
        visited = set()
        count = 0

        def dfs(node):
            visited.add(node)
            for neighbour in adj[node]:
                if neighbour not in visited:
                    dfs(neighbour)

        for i in range(V):
            if i not in visited:
                count += 1
                dfs(i)

        return count
