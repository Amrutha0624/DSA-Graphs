class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def prim_mst(self):
        visited = set()
        start_vertex = next(iter(self.graph))
        min_heap = [(0, start_vertex)]
        mst_cost = 0
        mst_edges = []

        while min_heap:
            weight, current_vertex = min_heap.pop(0)

            if current_vertex not in visited:
                visited.add(current_vertex)
                mst_cost += weight

                for neighbor, edge_weight in self.graph[current_vertex]:
                    if neighbor not in visited:
                        min_heap.append((edge_weight, neighbor))
                        mst_edges.append((current_vertex, neighbor, edge_weight))

                min_heap.sort()

        return mst_edges, mst_cost

# Example usage:
# Create an undirected graph
graph = Graph()
graph.add_edge('A', 'B', 2)
graph.add_edge('A', 'D', 5)
graph.add_edge('B', 'C', 4)
graph.add_edge('B', 'E', 3)
graph.add_edge('E', 'D', 1)

# Find the minimum spanning tree using Prim's algorithm
mst_edges, mst_cost = graph.prim_mst()

# Print the minimum spanning tree edges and cost
print("Minimum Spanning Tree Edges:")
for edge in mst_edges:
    print(f"{edge[0]} -- {edge[1]} : {edge[2]}")
print(f"Total Cost of MST: {mst_cost}")
