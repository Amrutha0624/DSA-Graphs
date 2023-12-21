class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        if start not in visited:
            print(start, end=' ')
            visited.add(start)

            for neighbor in self.graph.get(start, []):
                self.dfs(neighbor, visited)

# Example usage:
# Create a directed graph
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

# Perform DFS starting from vertex 2
print("DFS starting from vertex 2:")
graph.dfs(2)
