"""
Clone Graph - Medium

Given a node in a connected undirected graph, return a deep copy of the graph.
Each node in the graph contains an integer value and a list of its neighbors.
class Node {
    public int val;
    public List<Node> neighbors;
}
The graph is shown in the test cases as an adjacency list. An adjacency list is a mapping of nodes to lists, 
used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
For simplicity, nodes values are numbered from 1 to n, where n is the total number of nodes in the graph. 
The index of each node within the adjacency list is the same as the node's value (1-indexed).
The input node will always be the first node in the graph and have 1 as the value.

Example 1:
Input: adjList = [[2],[1,3],[2]]
Output: [[2],[1,3],[2]]
Explanation: There are 3 nodes in the graph.
Node 1: val = 1 and neighbors = [2].
Node 2: val = 2 and neighbors = [1, 3].
Node 3: val = 3 and neighbors = [2].

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: The graph has one node with no neighbors.

Example 3:
Input: adjList = []
Output: []
Explanation: The graph is empty.



# Clone Graph: My Thought Process

## 1. Clarify the prompt

I want to make sure I understand the problem correctly.
I'm given a reference to one node in a connected, undirected graph.
Each node has a value and a list of neighbors.
I need to return a deep copy of the whole graph.
That means brand new nodes, with the same values and the same connections.

Quick questions:
- Can the input be None? I'll assume yes, and return None.
- Is the graph connected? I'll assume yes, so I can reach every node from this one.
- Can there be cycles? Yes, since it's undirected, every edge goes both ways.
- Are node values unique? I'll assume yes, but I won't rely on it.
  I'll match nodes by reference, not by value.

So I need to copy every node once,
and rebuild every edge between the copies, not the originals.

## 2. Test cases

```
1 --- 2
|     |
4 --- 3
```
Each node has two neighbors.
The answer is a new graph with the same shape,
where no new node points to an old node.

- None input: return None.
- Single node with no neighbors: return one new node, with an empty list.
- Two nodes pointing at each other: a cycle of length 2.
- A node reached from several paths: it must be copied only once.

## 3. Brute force

My first idea is to copy nodes as I walk the graph,
and keep a list of (original, copy) pairs I've made.
Before copying a node, I search that list to see if it's already copied.

The search is required.
Without it, a cycle like 1 -> 2 -> 1 would copy forever,
and a node reached by two paths would get two different copies.

Time: O(V * (V + E)).
- Every edge leads to a lookup.
- Each lookup scans a list of up to V pairs.

Space: O(V) for the list of pairs.

Why it's slow:
- The lookup "have I copied this node already?" is a linear scan.
- I do it once per edge.

## 4. Optimal solution

Instead of scanning a list to find a node's copy,
I can store the copies in a hash map, keyed by the original node.

The data structure I will use is a hash map from original node to copy,
because it answers "have I copied this node?" in O(1) on average,
and it also hands me the copy when I need it.

It does two jobs at once.
It acts as my visited set, so cycles don't loop forever.
And it makes sure every node is copied exactly once.

As I go through the graph with DFS, I look up the current node in the map.

When it's already there, I return its copy right away.

When it's not, I create a new node with the same value,
and put it in the map right away, before visiting any neighbors.
Then I copy each neighbor, and add those copies to the new node's list.

At the end, I return the copy of the starting node.

Time: O(V + E)
- Each node is copied once.
- Each neighbor list is walked once, and the lists add up to 2E.

Space: O(V)
- The map holds one entry per node.
- The call stack can go V deep for a long chain.
- The cloned graph itself is the output, so I don't count it.

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

First I make a class called Solution.

Then I make a function called cloneGraph that takes self and node.

Before anything else, I check if node is empty.
If so, I return None, because there's no graph to copy.

Then I create an empty dictionary called copies.
It maps each original node to its new copy.
I'm using the node objects themselves as keys, not their values,
so it works even if two nodes had the same value.

Now I define an inner function called dfs that takes old.
It returns the copy of old, creating it if needed.

First thing inside it, I check if old is already in copies.
If so, I return copies[old].
That's my base case.
It stops cycles from looping forever,
and makes sure every path to this node gets the same copy.

If it's not copied yet, I create a new Node with old.val,
and store it in new.

Then I set copies[old] to new, right away.
I do this before visiting any neighbors.
If a neighbor points back to old, the lookup finds this copy,
instead of starting another one.

Then I loop over each nei in old.neighbors.
For each one, I call dfs on nei, which gives me the neighbor's copy.
I append that copy to new.neighbors.
So the new node only ever points to new nodes, never the originals.

After the loop, I return new.

Finally, outside dfs, I return dfs called on node.
That's the copy of the starting node,
and through its neighbors, the whole cloned graph.

## 7. Testing

Before I finish, I'll run my test cases.
- Square example: dfs(1) makes copy 1, then goes to 2.
  dfs(2) makes copy 2, and its neighbor 1 is already in copies,
  so it gets copy 1 back.
  It continues to 3 and 4 the same way.
  Every node is copied once, and every edge points to copies.
- None input: returns None right away.
- Single node: one copy is made, the loop doesn't run, its list is empty.
- Two nodes pointing at each other: the second lookup hits the map,
  so there's no infinite loop.
- Node reached by two paths:
"""
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        copies = {}

        def dfs(old):
            if old in copies:
                return copies[old]

            new = Node(old.val)
            copies[old] = new

            for nei in old.neighbors:
                new.neighbors.append(dfs(nei))

            return new

        return dfs(node)