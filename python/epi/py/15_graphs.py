#%% [markdown]
'''
A directed acyclic graph (DAG) is a directed graph in which there are no cycles, 
i.e., paths which contain one or more edges and which begin and end at the same vertex.

A topological ordering of the vertices in a DAG is an ordering of the vertices 
in which each edge is from a vertex earlier in the ordering to a vertex later in the ordering.

If G is an undirected graph, vertices u and v are said to be connected if G contains a path from u to v;
otherwise, u and v are said to be disconnected.
A graph is said to be connected if every pair of vertices in the graph is connected.
A connected component is a maximal set of vertices C such that each pair of vertices in C is connected in G.

A graph can be implemented in two ways, using adjacency lists or adjacency matrix.

A tree is a special sort of graph, it is an undirected graph that is connected but has no cycles.
Equivalent definitions,e.g., a graph is a free tree if and only if there exists a unique path between every pair of vertices.

Graphs are ideal for modeling and analyzing relationships between pairs of objects.

### Tips
- Use a graph when the problem involves spatially connected objects, e.g., road segments between cities.
- Use a graph when you need to analyze binary relationship, between objects, such as interlinked webpages, followers in a social graph.
- Analyzing structure,e.g.,looking for cycles or connected components. DFS works well for these applications.
- Some graph problems are related to optimization, e.g. find the shortest path. BFS, Dijkstra's shortest path, minimum spanning tree.

### Graph search
- depth-first search (DFS), can be used to check for the presence of cycles.
- breadth-first search (BFS), can be used to compute distances from the start vertex.

'''
