"""
Graph Valid Tree - Medium

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a 
function to check whether these edges make up a valid tree.

Example 1:
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true

Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as 
[1, 0] and thus will not appear together in edges.




# Graph Valid Tree: My Thought Process

## 1. Clarify the prompt

"Before I jump in, I want to make sure I understand the problem correctly."

"So I'm given n nodes, labeled 0 to n - 1, and a list of undirected edges.
I need to return True if these edges form a valid tree,
and False if they don't."

"A valid tree has two rules.
First, everything is connected, so I can reach every node from any node.
Second, there are no cycles."

"I have a few quick questions before I start."

"Are the edges undirected?"
→ I'll assume yes.

"Can there be duplicate edges, like [0, 1] twice?"
→ I'll assume it's possible. That would count as a cycle, so it's not a tree.

"Can there be self-loops, like [2, 2]?"
→ I'll assume it's possible, and that would also make it not a tree.

"Is a single node with no edges a valid tree?"
→ I'll assume yes.

"Okay, so I need to check two things: no cycles, and fully connected."

## 2. Test cases

"Let me write down a few test cases before I think about the approach."

```
n = 5, edges = [[0,1], [0,2], [0,3], [1,4]]
```
"4 edges for 5 nodes, everything is connected, and there's no loop.
Answer: True."

```
n = 5, edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
```
"1, 2, and 3 form a loop. Answer: False."

```
n = 4, edges = [[0,1], [2,3]]
```
"Two separate pieces, so it's not connected. Answer: False."

"A few edge cases:"
- "One node, no edges: Answer: True."
- "Two nodes, no edges: they're not connected. Answer: False."
- "A duplicate edge, like [[0,1], [0,1]] with n = 2: that's a cycle. Answer: False."
- "A self-loop, like [[0,0]] with n = 2: Answer: False."

"Do these expected outputs match what you have in mind?"

## 3. Brute force

"My first idea is the simplest one.
I add the edges one at a time.
Before adding an edge between u and v,
I search the graph so far to see if u can already reach v.
If it can, this edge would close a loop, so I return False."

"After all the edges are added, I run one more search from node 0
to check if every node is reachable."

"This works because it checks both rules directly:
no edge ever closes a loop, and everything ends up connected."

"The time is O(E * (V + E)),
where V is the number of nodes and E is the number of edges.
I run one search for every edge,
and each search can walk the whole graph."

"The space is O(V + E), for the graph and the visited set."

"The problem is that I'm running a full search for every single edge.
Most of those searches walk through the same nodes again and again."

## 4. Optimal solution

"The bottleneck is searching once per edge.
So I want to check both rules with a single search."

"The key fact is that a tree with n nodes always has exactly n - 1 edges."

"That gives me a shortcut.
If the number of edges isn't n - 1, I can return False right away.
Fewer than n - 1 means it can't be connected.
More than n - 1 means there has to be a cycle."

"If there are exactly n - 1 edges, I only need to check one thing:
is it connected?"

"That's because with exactly n - 1 edges,
being connected and having no cycles go together.
If it's connected with n - 1 edges, there's no room for a cycle."

"So instead of checking for a cycle on every edge,
I can count the edges once, then run one DFS to check connectivity."

"The data structures I'll use are an adjacency list and a visited set.
The adjacency list gives me each node's neighbors directly.
The visited set records every node DFS reaches,
and stops me from visiting a node twice."

"As I go, I first check if the edge count is n - 1.
If not, I return False."

"Then I build the adjacency list,
and run DFS from node 0, adding every node I reach to visited."

"At the end, I return True if visited has all n nodes,
and False otherwise."

"The time is O(V + E).
Building the adjacency list touches every edge once,
and DFS visits each node and each edge once."

"The space is O(V + E), for the adjacency list, the visited set,
and the call stack."

"So I go from O(E * (V + E)) down to O(V + E)."

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

"First, I'll make a class called Solution."

"Then a function called isValid that takes self, n, and edges."

"Before anything else, I check if the number of edges is n - 1.
If it isn't, I return False right away.
This handles cycles and missing connections in one line,
without building anything."

"Next, I'll create an empty set called visited.
It holds every node DFS reaches."

"Then I'll build the adjacency list.
I'll create an empty list called adj,
and loop n times to give each node its own empty list.
I make one for every node, so a node with no edges still has an entry."

"Then I loop over each edge, unpacking it into u and v.
I add v to u's list, and u to v's list.
I add both, because the edges are undirected."

"Now I'll define a helper called dfs that takes a node."

"First thing inside it, I add the node to visited."

"Then I loop over each neighbor in adj[node].
If the neighbor isn't in visited, I call dfs on it."

"After defining dfs, I call it on node 0.
Any node works as a starting point,
because if the graph is a tree, every node is reachable from it."

"Finally, I return whether the size of visited equals n.
If DFS reached every node, the graph is connected.
And since I already know there are exactly n - 1 edges,
that means it's a valid tree."

## 7. Testing

"Before I finish, I'll trace through my test cases."

- "First example: 4 edges, n - 1 is 4, so I continue.
  DFS from 0 reaches 1, 2, 3, then 4 through 1.
  visited has 5 nodes, so the answer is True, which matches."
- "Second example: 5 edges, but n - 1 is 4.
  So I return False right away, which matches."
- "Two pieces with n = 4: 2 edges, but n - 1 is 3.
  So I return False right away, which matches."
- "One node, no edges: 0 edges equals n - 1, so I continue.
  DFS reaches node 0, visited has 1 node, so the answer is True."
- "Two nodes, no edges: 0 edges, but n - 1 is 1, so the answer is False."
- "Duplicate edge with n = 2: 2 edges, but n - 1 is 1, so the answer is False."
- "Self-loop [[0,0]] with n = 2: 1 edge equals n - 1, so I continue.
  DFS from 0 never reaches 1, so visited has 1 node,
  and the answer is False."

"The output matches what I expected for all of them."

"To recap, time is O(V + E) and space is O(V + E)."

"If the graph could be very deep, the recursion might hit
Python's limit of about 1000.
In that case, I'd use BFS with a queue,
or Union-Find, which checks each edge and returns False
as soon as an edge joins two nodes that are already connected."
"""
class Solution:
    def isValid(self, n, edges):
        if len(edges) != n - 1:
            return False

        visited = set()
        adj = []
        for i in range(n):
            adj.append([])

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)

        dfs(0)

        return len(visited) == n

        