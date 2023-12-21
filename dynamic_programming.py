class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

def shortest_path(graph, start, end, memo={}):
    if start == end:
        return 0

    if (start, end) in memo:
        return memo[(start, end)]

    if start not in graph.graph:
        return float('inf')

    min_path = float('inf')
    for neighbor, weight in graph.graph[start]:
        candidate = shortest_path(graph, neighbor, end, memo) + weight
        min_path = min(min_path, candidate)

    memo[(start, end)] = min_path
    return min_path

# Example usage:
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 4)
g.add_edge(1, 3, 1)
g.add_edge(3, 4, 2)
g.add_edge(4, 3, 3)

start_vertex = 0
end_vertex = 4

result = shortest_path(g, start_vertex, end_vertex)

if result == float('inf'):
    print(f"There is no path from {start_vertex} to {end_vertex}.")
else:
    print(f"Shortest path from {start_vertex} to {end_vertex}: {result}")
