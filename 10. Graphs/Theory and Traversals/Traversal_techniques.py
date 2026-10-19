"""
Traversal Techniques - Medium

Given an undirected connected graph with V vertices numbered from 0 to V-1, the task is to implement 
both Depth First Search (DFS) and Breadth First Search (BFS) traversals starting from the 0th vertex.

The graph is represented using an array/vector of edges, where each element is a pair [u, v] indicating 
an undirected edge between vertex u and vertex v.

Example 1:
Input: V = 5, edges = [ [0, 1], [0, 2], [0, 3], [2, 4] ]
Output:[0, 2, 4, 3, 1], [0, 2, 3, 1, 4]
Explanation:
DFS: Start from vertex 0. Visit vertex 2, then vertex 4, backtrack to vertex 0, then visit vertex 3, 
and finally vertex 1. The traversal is 0 → 2 → 4 → 3 → 1.
BFS: Start from vertex 0. Visit vertices 2, 3, and 1 (in the order they appear in the adjacency list). 
Then, visit vertex 4 from vertex 2. The traversal is 0 → 2 → 3 → 1 → 4.

Example 2:
Input: V = 4, edges = [ [0, 1], [0, 3], [1, 2] ]
Output: [0, 1, 2, 3], [0, 1, 3, 2]
Explanation:
DFS: Start from vertex 0. Visit vertex 1, then vertex 2, backtrack to vertex 0, then visit vertex 3. 
The traversal is 0 → 1 → 2 → 3.
BFS: Start from vertex 0. Visit vertices 1 and 3, then visit vertex 2 from vertex 1. 
The traversal is 0 → 1 → 3 → 2.





# Graph Traversal (Adjacency List, DFS, BFS): My Thought Process

## 1. Understanding

I want to make sure I understand the problem correctly.
I'm given V, the number of vertices, and a list of edges.
I need to build the graph, then return the order in which DFS visits the nodes,
and the order in which BFS visits the nodes.

Quick questions:
- Are the vertices labeled 0 to V - 1? I'll assume yes.
- Is the graph undirected? I'll assume yes, so each edge goes both ways.
- Do I start from node 0? I'll assume yes.
- Is the graph connected? I'll assume yes.
  If not, I only get the nodes reachable from 0.
- In what order do I visit the neighbors?
  I'll assume the order they appear in the edge list.
- Can there be cycles? I'll assume yes, so I must track visited nodes.
- Can V be 1, with no edges? I'll assume yes.

## 2. Restate

So I'm turning an edge list into a graph I can move through easily.
Then I visit every node reachable from 0, in two different orders.
DFS goes as deep as it can before coming back.
BFS goes level by level.

## 3. Example

```
V = 5
edges = [[0,1], [0,2], [0,3], [2,4]]

    0
  / | \
 1  2  3
    |
    4
```

The adjacency list is:
- 0: [1, 2, 3]
- 1: [0]
- 2: [0, 4]
- 3: [0]
- 4: [2]

DFS goes 0, then 1, back to 0, then 2, then 4, back to 0, then 3.
DFS order: [0, 1, 2, 4, 3].

BFS visits 0, then all its neighbors 1, 2, 3, then the next level, which is 4.
BFS order: [0, 1, 2, 3, 4].

Edge case: V = 1 with no edges returns [0] for both.

## 4. Brute force

My first idea is to skip building the graph.
Whenever I need the neighbors of a node, I scan the whole edge list
and pick out every edge that touches that node.

This works because the edge list has all the information.

The problem is the repeated work.
Each node scans all E edges, so the traversal costs O(V * E).
That gets slow when the graph is big.

## 5. Key observation

The repeated work is scanning all edges again and again, just to find neighbors.
I can do that scan once, up front.

I build an adjacency list.
It is a list where index i holds all the neighbors of node i.
Then getting the neighbors of any node is direct, and costs only its own degree.

The second problem is cycles.
A graph can lead me back to a node I already visited.
Without protection, I would loop forever.
So I keep a visited set, and never visit a node twice.

For the order:
- DFS needs to go deep first, and come back.
  The recursion call stack does exactly that.
- BFS needs to go level by level.
  A queue does that, because it's first in, first out.

## 6. Approach

Instead of scanning the edge list for every node,
I can build the adjacency list once, and use it for both traversals.

The data structure I will use for the graph is an adjacency list,
because it gives me the neighbors of a node directly.

For building it, as I go through the edges,
I will add each node to the other's list, because the graph is undirected.

For DFS, the data structure I will use is the recursion call stack,
plus a visited set,
because I need to go deep, then come back, and never revisit a node.
As I go through the nodes, I will mark the current node visited and add it to the output.
When a neighbor is not visited yet, I will go into it.
At the end, I return the output.

For BFS, the data structure I will use is a queue, plus a visited set,
because the queue gives me level by level order.
As I go through the nodes, I will take a node from the front and add it to the output.
When a neighbor is not visited yet, I will mark it visited and add it to the queue.
When the queue is empty, I have visited everything reachable.
At the end, I return the output.

## 7. While coding

First I import deque from collections.
I'm using it as the queue for BFS, because removing from the front is O(1).

Then I make a class called Solution.

I'll write a helper first, called build_adj, that takes self, V, and edges.
It turns the edge list into an adjacency list.

Inside it, I create an empty list called adj.
Then I loop V times, and add an empty list for each node.
Now adj[i] is where I will store the neighbors of node i.

Then I loop over the edges, unpacking each one into u and v.
I add v to the list of u.
And I add u to the list of v.
I do both, because the graph is undirected.
I'm adding the plain number, not a list around it,
because I'll need to look it up in a set later.

Then I return adj.

Now I write dfs, which takes self, V, and edges.
First, I call build_adj to get the adjacency list.
Then I create an empty set called visited.
And an empty list called out, for the visiting order.

Then I define an inner function called helper that takes a node.
Inside it, I add the node to visited.
I mark it right away, so it can't be visited again by another path.
Then I add the node to out.
I do this before going to the neighbors,
so a node is recorded before the nodes below it.

Then I loop over the neighbors of this node.
For each neighbor, I check if it's not in visited.
If it's not, I call helper on it, which goes deeper.
When it comes back, the loop moves to the next neighbor.

After defining helper, I call it on 0, which is my starting node.
And I return out.

Now I write bfs, which takes self, V, and edges.
Again, I start by building the adjacency list.

Then I create a queue with just 0 in it.
And I create the visited set, with 0 already in it.
I mark the start as visited right away, because it's already in the queue.

Then I create an empty list called out.

Now I start a while loop that runs as long as the queue isn't empty.
Inside it, I take a node from the front, using popleft.
I add it to out.
I don't need to track levels here.
I only want the order, so I don't need the queue's size.

Then I loop over the neighbors of this node.
For each neighbor, I check if it's not in visited.
If it's not, I add it to visited, and I add it to the queue.
I mark it visited when I add it to the queue, not when I take it out.
If I waited, the same node could get added by two different neighbors,
and it would end up in the output twice.

When the queue is empty, I return out.

## 8. Testing

Before I finish, I want to test the edge cases.
- One node, no edges: adj is [[]], and both return [0].
- Cycle, like 0-1, 1-2, 2-0: visited stops me from looping forever.
- Disconnected graph: I only get the nodes reachable from 0.
  If I needed all nodes, I would loop over every node,
  and start a traversal from each one that isn't visited.
- Duplicate edges: the neighbor appears twice in the list,
  but the visited check skips the second one.
- Self-loop, like 2-2: the node is already visited, so it's skipped.
- Long chain: DFS goes V levels deep.

For my example, BFS goes like this:
- The queue is [0]. Take 0. Add 1, 2, 3. The queue is [1, 2, 3].
- Take 1. Its only neighbor, 0, is visited.
- Take 2. Add 4. The queue is [3, 4].
- Take 3. Nothing new.
- Take 4. Nothing new.

The order is [0, 1, 2, 3, 4].

If the graph could be very deep, Python's recursion limit is about 1000.
In that case I would write DFS iteratively, using a stack.
One detail is that a stack reverses the neighbor order,
so I would push the neighbors in reverse to keep the same order.

## 9. Complexity

Building the adjacency list:
Time: O(V + E)
- I create V lists, and go through E edges once.
Space: O(V + E)
- Each edge is stored twice, once for each side.

DFS and BFS:
Time: O(V + E)
- Each node is visited once.
- Each node's neighbor list is scanned once, and the lists add up to 2E.

Space: O(V)
- The visited set holds up to V nodes.
- DFS also has the call stack, up to V deep.
- BFS also has the queue, up to V nodes.
- The output holds V nodes.
- The adjacency list takes O(V + E), but I built that before the traversal.

Compared with the brute force, O(V * E) becomes O(V + E).
"""
from collections import deque

class Solution:

    def build_adj(self, V, edges):
        adj = []
        for i in range(V):
            adj.append([])
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return adj

    def dfs(self, V, edges):
        adj = self.build_adj(V, edges)
        visited = set()
        out = []
        def helper(node):
            visited.add(node)
            out.append(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    helper(neighbor)
        helper(0)
        return out

    def bfs(self, V, edges):
        adj = self.build_adj(V, edges)
        queue = deque([0])
        visited = {0}
        out = []
        while queue:
            node = queue.popleft()
            out.append(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return out

