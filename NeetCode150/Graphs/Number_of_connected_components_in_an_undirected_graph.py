"""
Number of Connected Components In An Undirected Graph - Medium

You have an undirected graph of n nodes labeled from 0 to n - 1. 
You are given an integer n and an array edges where 
edges[i] = [aᵢ, bᵢ] indicates that there is an edge between aᵢ and bᵢ in the graph.
Return the number of connected components in the graph.

Example 1:
Input:
n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Example 2:
Input:
n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
"""
class Solution:
    def components(self, n, edges):
        adj = []
        visited = set()
        for i in range(n):
            adj.append([])
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def dfs(node):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1
        return count