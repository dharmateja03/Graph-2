TimeComplexity:O(v+e)
SpaceComplexity:O(v+e)
"""
Time Complexity
Graph building: O(V + E) — you touch each vertex and each edge once to create the adjacency list.

DFS traversal: O(V + E) — each vertex is visited once, and each edge is explored exactly twice (once from each endpoint).

Updating lowest/discovery values: O(1) work per edge.

Overall: O(V + E)

Space Complexity
Graph storage: O(V + E) for adjacency list.

Arrays (discovery, lowest): O(V)

Recursion stack: O(V) in the worst case (graph is a long chain).

Answer list: O(E) worst case if all edges are bridges.

Overall: O(V + E)


"""

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        this is related to https://en.wikipedia.org/wiki/Tarjan's_strongly_connected_components_algorithm
        >observations
            if you are part of cycle you are definetly not part of critical compo (because even if connection is gone you can be reached form a different path)
            
            so you need to find connections in which they are not part of cycle

            based of tarjans algo 
            lets have 2 things for each node
            discovery natural order
            lowest lets say you are at nodei ,,j will become lowestif out of all reachable nobes form nodei j will earliest in dfs order
            typical dfs+lowest + discovery 

            once one of dfs is terminated while coming back updated lowest and add critcal compo to path
            if lowest of child is > parent than its critical component
            why?
            if child and parent are in cycle than , lowest would be same 

            sudo:
                build graph
                initate discovery and lowest 
        """
        graph=defaultdict(list)
        def buildGraph(connections):
            for c0,c1 in connections:
                graph[c0].append(c1)
                graph[c1].append(c0)
        lowest,discovery=[0 for _ in range(n)],[-1 for _ in range(n)]
        
        ans=[]
        buildGraph(connections)
        l=0
        def dfs(curr,par,l):
            if discovery[curr]!=-1:return  #v,u
            lowest[curr]=l
            discovery[curr]=l
            
            
            for node in graph[curr]:
                if node==par:continue #this is imporatant
                
                dfs(node,curr,l+1)
                # print(lowest[node],discovery[curr])
                if lowest[node]>discovery[curr]:ans.append([node,curr]) #not in cycle
                lowest[curr]=min(lowest[curr],lowest[node])
           
        
        dfs(0,0,0)
        print(discovery)
        print(lowest)
        return ans
        
