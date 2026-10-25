"""
Redundant Connection - Medium

You are given a connected undirected graph with n nodes labeled from 1 to n. Initially,
it contained no cycles and consisted of n-1 edges.
We have now added one additional edge to the graph. The edge has two different 
vertices chosen from 1 to n, and was not an edge that previously existed in the graph.
The graph is represented as an array edges of length n where edges[i] = [ai, bi] 
represents an edge between nodes ai and bi in the graph.
Return an edge that can be removed so that the graph is still a connected non-cyclical 
graph. If there are multiple answers, return the edge that appears last in the input 
edges.

Example 1:
Input: edges = [[1,2],[1,3],[3,4],[2,4]]
Output: [2,4]

Example 2:
Input: edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
Output: [3,4]




# Redundant Connection: My Thought Process

## 1. Clarify the prompt

"Before I jump in, I want to make sure I understand the problem correctly."

"So I'm given a list of undirected edges.
The graph started as a tree with n nodes, labeled 1 to n,
and then one extra edge was added.
That extra edge creates exactly one cycle.
I need to find an edge I can remove so the graph becomes a tree again."

"I have a few quick questions before I start."

"Are the nodes labeled 1 to n, not 0 to n - 1?"
→ I'll assume 1 to n.

"Is there always exactly one extra edge?"
→ I'll assume yes, so there are exactly n edges for n nodes.

"If more than one edge could be removed, which one should I return?"
→ I'll assume the one that appears last in the input.

"Are the edges undirected?"
→ I'll assume yes.

"Okay, so every edge in the cycle is a candidate,
and I want the one that comes last in the list."

"That fits nicely with going through the edges in order.
The cycle doesn't exist until its last edge is added.
So the first edge that connects two nodes that are already connected
is exactly the last edge of the cycle."

## 2. Test cases

"Let me write down a few test cases before I think about the approach."

```
edges = [[1,2], [1,3], [2,3]]
```
"1-2 and 1-3 already connect 2 and 3.
So [2,3] closes the loop. Answer: [2, 3]."

```
edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
```
"1-2-3-4 is a chain, so 1 and 4 are already connected.
[1,4] closes the loop. [1,5] comes after, but it's not part of the cycle.
Answer: [1, 4]."

"A few edge cases:"
- "The smallest case is a triangle with 3 nodes, like the first example."
- "The extra edge is the very last edge in the list."
- "The cycle doesn't include node 1, like [[1,2], [2,3], [3,4], [2,4]].
  Answer: [2, 4]."

"Do these expected outputs match what you have in mind?"

## 3. Brute force

"My first idea is the simplest one.
I build the graph one edge at a time.
Before adding an edge between u and v,
I run a DFS to check if u can already reach v
using the edges I've added so far."

"If it can, u and v are already connected,
so this edge would close a loop, and I return it."

"If it can't, I add the edge and move on."

"This works because the first edge that connects
two already-connected nodes is the one that makes the cycle."

"The time is O(n^2).
There are n edges, and for each one,
the DFS can walk the whole graph built so far."

"The space is O(n), for the adjacency list and the visited set."

"The problem is that every DFS starts from scratch.
I keep walking the same parts of the graph again,
just to answer one question: are u and v already in the same group?"

## 4. Optimal solution

"The bottleneck is running a whole DFS just to ask
whether two nodes are already connected."

"Instead of searching the graph every time,
I can keep track of which group each node belongs to,
and update the groups as I add edges."

"The data structure I'll use is Union-Find, also called Disjoint Set Union,
because it answers 'are these two nodes in the same group?'
and 'merge these two groups' in almost constant time."

"Here's how it works.
Every node points to a parent.
If I keep following parents, I reach the group's leader, called the root.
Two nodes are in the same group if they have the same root."

"I'll use two tricks to keep it fast."

"Path halving: while I walk up to the root,
I make each node skip over its parent and point to its grandparent.
That makes the path shorter every time I search."

"Union by size: when I merge two groups,
I attach the smaller group under the bigger one.
That keeps the trees flat."

"As I go through the edges, I try to merge u's group and v's group."

"When u and v already have the same root,
they're already connected, so this edge closes the cycle, and I return it."

"Otherwise, I merge their groups and keep going."

"The time is O(n * α(n)), which is basically O(n).
α is the inverse Ackermann function,
and it stays at 4 or less for any real input size.
So each find and union is effectively constant time."

"The space is O(n), for the parent and size lists."

"So I go from O(n^2) down to about O(n)."

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

"First, I'll make a class called Solution."

"Then a function called findRedundantConnection that takes self and edges."

"I'll create an empty list called par.
It stores each node's parent."

"Then I loop i from 0 to len(edges), and append i to par.
So every node starts as its own parent, which means its own group.
I go up to len(edges) because the nodes are labeled 1 to n,
and n equals the number of edges.
Index 0 just goes unused."

"Next, I'll create a list called rank, with a 1 for every node.
Here I'm using rank as the size of each group.
Every group starts with just one node, so it starts at 1."

"Now I'll define a helper called find that takes n.
It returns the root of n's group."

"I start by setting p to par[n], which is n's parent."

"Then I loop while p is not equal to par[p].
If a node is its own parent, it's the root, so that's when I stop."

"Inside the loop, I set par[p] to par[par[p]].
That makes p skip its parent and point to its grandparent.
This is path halving.
It flattens the tree as I go, so future lookups are faster."

"Then I move p up to its new parent."

"When the loop ends, p is the root, and I return it."

"I'm writing find as a loop instead of recursion,
so there's no risk of hitting the recursion limit."

"Next, I'll define a helper called union that takes n1 and n2.
It merges their groups,
and returns False if they were already in the same group."

"First, I find the roots of both nodes and call them p1 and p2."

"If p1 equals p2, they're already in the same group.
That means this edge would make a cycle, so I return False."

"Otherwise, I compare the sizes of the two groups."

"If p1's group is bigger, I set par[p2] to p1.
So the smaller group hangs under the bigger one.
Then I add p2's size to p1's size,
because p1's group now contains both."

"Otherwise, I do the opposite.
I set par[p1] to p2, and add p1's size to p2's size."

"Then I return True, because the merge worked."

"Now I loop over each edge, unpacking it into n1 and n2."

"For each edge, I call union on n1 and n2.
If it returns False, they were already connected,
so this is the redundant edge, and I return [n1, n2]."

"I don't need a return after the loop,
because the problem guarantees there's always one extra edge,
so the loop always returns from inside."

## 7. Testing

"Before I finish, I'll trace through my test cases."

- "First example: [1,2] merges 1 and 2 into one group of size 2.
  [1,3] merges 3 into that group.
  [2,3]: find(2) and find(3) return the same root,
  so union returns False, and I return [2, 3]. That matches."
- "Second example: [1,2], [2,3], and [3,4] put 1, 2, 3, and 4
  in one group of size 4.
  [1,4]: both have the same root, so I return [1, 4].
  I never reach [1,5]. That matches."
- "Cycle without node 1: [1,2], [2,3], [3,4] make one group.
  [2,4] finds the same root on both sides, so I return [2, 4]."
- "Extra edge last: every earlier edge merges two different groups,
  and only the last edge finds the same root, so it's returned."

"The output matches what I expected for all of them."

"To recap, time is about O(n) with path halving and union by size,
and space is O(n)."
"""
# Brute approach
class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)
        adj = []
        for i in range(n + 1):
            adj.append([])

        def canReach(node, target, visited):
            if node == target:
                return True
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    if canReach(nei, target, visited):
                        return True
            return False

        for u, v in edges:
            if canReach(u, v, set()):
                return [u, v]
            adj[u].append(v)
            adj[v].append(u)

        return []

#Optimal Approach
class Solution:
    def findRedundantConnection(self, edges):
        par = []
        for i in range(len(edges) + 1):
            par.append(i)

        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]